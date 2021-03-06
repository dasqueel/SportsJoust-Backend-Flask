# import the Flask class from the flask module
import os
from flask import *
from funcs import *
from config import *
from pymongo import MongoClient
from random import randint
from passlib.hash import pbkdf2_sha256
from functools import wraps
import string
from datetime import timedelta
import collections
import json

# create the application object
app = Flask(__name__)
app.secret_key = '\x1f\xb1A\x01\x95\x8d\xc5\xdb\xe6\xf9\xb5\xf1\x93\xa5\x86\x07\xb9\x89\xbci\x99\xaaz\x82'

### Supporting funcs ###
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrap

#this is usable, chagne it
def mlogin_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'mlogged_in' in session:
            return test(*args, **kwargs)
        else:
            return 'have to log in'
    return wrap

### ROUTES ###
### wager handler from potential_contest
@app.route('/wagerBack', methods=['GET','POST'])
@login_required
def wagerBack():
    if request.method == 'GET':
        contest = 'nfl1'
        userName = session['userName']
        #matchId = request.args.get('matchId')
        matchId = session['matchId']
        wager = request.args.get('wager')
        wager = int(wager)
        #wager = float("{0:.2f}".format(wager))
        opUserName = None
        matchDoc = dbContests[contest].find_one({'matchId':matchId})
        if userName == matchDoc['team1user']:
            opUserName = matchDoc['team2user']
        else:
            opUserName = matchDoc['team1user']
        dbContests[contest].update({'matchId':matchId},{'$set':{'wager':wager,'turn':opUserName}})
        return jsonify(wager=wager)

@app.route('/potential_contest')
@login_required
def potential_contest():
    contest = 'nfl1'
    #get matchId from url
    matchId = request.args.get('matchId')
    match = dbContests[contest].find_one({'matchId':matchId})
    if match['state'] == 'potential':
        session['matchId'] = matchId
        userName = session['userName']
        opUserName = None
        userTeam = None
        opTeam = None
        turn = match['turn']
        if userName == match['team1user']:
            opUserName = match['team2user']
            opTeam = match['team2']
            userTeam = match['team1']
        else:
            opUserName = match['team1user']
            opTeam = match['team1']
            userTeam = match['team2']

        return render_template('potential_contest.html', match=match, opUserName=opUserName,userTeam=userTeam,opTeam=opTeam)
    else:
        return redirect(url_for('contest', matchId=matchId))

@app.route('/contest')
@login_required
def contest():
    contest = 'nfl1'
    #get matchId from url
    matchId = request.args.get('matchId')
    match = dbContests[contest].find_one({'matchId':matchId})
    userName = session['userName']
    opUserName = None
    userTeam = None
    opTeam = None
    if userName == match['team1user']:
        opUserName = match['team2user']
        opTeam = convert(match['team2'])
        userTeam = convert(match['team1'])
    else:
        opUserName = match['team1user']
        opTeam = convert(match['team1'])
        userTeam = convert(match['team2'])

    return render_template('contest.html', match=match, opUserName=opUserName,userTeam=userTeam,opTeam=opTeam)

@app.route('/current')
@login_required
def current():
    #get all potential mutually agreed matches
    contest = 'nfl1'
    userName = session['userName']
    #matches = dbContests[contest].find({'$or':[{'team1user':userName},{'team2user':userName}]})
    matches = dbContests[contest].find( {
        '$and' : [
            { '$or' : [ { 'team1user' : userName }, { 'team2user' : userName } ] },
            { 'state' : 'accepted' }
        ]
    } )

    #get opUserName
    return render_template('current.html', matches=matches)

@app.route('/potential')
@login_required
def potential():
    #get all potential mutually agreed matches
    contest = 'nfl1'
    userName = session['userName']
    #matches = dbContests[contest].find({'$or':[{'team1user':userName},{'team2user':userName}]})
    matches = dbContests[contest].find( {
        '$and' : [
            { '$or' : [ { 'team1user' : userName }, { 'team2user' : userName } ] },
            { 'state' : 'potential' }
        ]
    } )

    #get opUserName
    return render_template('potential.html', matches=matches)

#finalize comes from potential_contest
@app.route('/finalize', methods=['GET','POST'])
@login_required
def finalize():
    if request.method == 'GET':
        #matchId = request.form['matchId']
        matchId = request.args.get('matchId')
        #matchId = request.form['matchId']
        #this backend code runes when 2nd team accepts the deal

        contest = 'nfl1'
        match = dbContests[contest].find_one({'matchId':matchId})
        wager = match['wager']
        #check to see both parties have sufficient funds for match
        userName = session['userName']
        opUserName = None
        if userName == match['team1user']:
            opUserName = match['team2user']
        else:
            opUserName = match['team1user']

        userDoc = db[userName].find_one({'userName':userName})
        opUserDoc = db[opUserName].find_one({'userName':opUserName})
        userBal = userDoc['balance']
        opUserBal = opUserDoc['balance']

        if wager <= userBal or wager <= opUserBal:
            #change state of contest to accepted anc close it
            newUserBal = userBal-wager
            newOpUserBal = opUserBal-wager
            session['balance'] = newUserBal
            db[userName].update({'userName':userName},{'$set':{'balance':newUserBal}})
            db[opUserName].update({'userName':opUserName},{'$set':{'balance':newOpUserBal}})
            dbContests[contest].update({'matchId':matchId},{'$set':{'state':'accepted','open':False}})
            print 'match finalized'
            return jsonify(funds=True)
        else:
            #return a party doesnt have sufficient funds
            print 'insufficient funds'
            return jsonify(funds=False)

@app.route('/matchBack', methods=['GET','POST'])
@login_required
def matchBack():
    if request.method == 'POST':
        contest = 'nfl1'
        userName = session['userName']
        opUserName = session['opUserName']
        #get wager and matchId and send message to opUser the wager
        wager = request.form['wager']
        wager = int(wager)
        #wager = float("{0:.2f}".format(wager))
        matchId = request.form['matchId']

        #set wager to amount set my first user
        matchDoc = dbContests[contest].find_one({'matchId':matchId})
        dbContests[contest].update({'matchId':matchId},{'$set':{'wager':wager,'turn':opUserName}})

        #remove opUser from users potential matches
        db[userName].update({'contest':contest},{'$pull':{'potential':opUserName}})
        #add opUer
        #db[userName].update({'contest':contest},{'$pull':{'potential':opUserName}})

        #update wager
        dbContests[contest].update
        return 'wager completed'

        #send message to opponent of the new offer and have message high light update

@app.route('/acceptBack')
@login_required
def acceptBack():
    contest = 'nfl1'
    #would user session variavles if only doing a weekly nfl games
    outcome = request.args.get('outcome')
    userName = session['userName'] #user stuff
    userDoc = db[userName].find_one({'contest':contest})
    userTeam = session['userTeam']
    #get usersbalance
    userBalDoc = db[userName].find_one({'userName':userName})
    userBal = userBalDoc['balance']

    opTeam = session['opTeam']
    opUserName = session['opUserName'] #opUser stuff
    opDoc = db[opUserName].find_one({'contest':contest})
    #get op users balance
    opUserBalDoc = db[userName].find_one({'userName':userName})
    opUserBal = userBalDoc['balance']

    if opUserName in userDoc['potential']:
        #create matchdoc and add it to contests matches
        match = estabMatch(userTeam,opTeam,userName,opUserName)
        matchId = match['matchId']
        dbContests[contest].insert(match)

        #add opUser to users accepted matches
        db[userName].update({'contest':contest},{'$push':{'accepted':opUserName}})

        maxWager = min(userBal, opUserBal)
        return jsonify(match=True,maxWager=maxWager,matchId=matchId)
    else:
        #add userName to opponents potential games
        db[opUserName].update({'contest':contest},{'$push':{'potential':userName}})
        db[userName].update({'contest':contest},{'$push':{'accepted':opUserName}})
        return jsonify(match=False)

#code to find WORKABLE matchups
@app.route('/matchups', methods=['GET','POST'])
@login_required
def matchups():
    error = None
    contest = 'nfl1'
    contestDoc = dbContests[contest].find_one({'contest':contest})
    userDoc = db[session['userName']].find_one({'contest':contest})
    pool = contestDoc['pool']
    #check to see if rankings have been entered
    if userDoc == None:
        return redirect(url_for('rankings'))
    #check to find if any matches are avaialbe
    elif pool == []:
        error = 'there are no possible matchs at this moment :('
        return render_template('matchups.html', error=error)
    else:
        userName = session['userName']
        userDoc = db[userName].find_one({'contest':contest})
        userRankings = {'user':userName,'qb':userDoc['qbr'],'rb':userDoc['rbr'],'wr':userDoc['wrr'],'te':userDoc['ter'],'defst':userDoc['defstr']}
        userRankings = convert(userRankings)
        if request.method == 'POST':
            outcome = request.form['outcome']
            #when recieving decision on match
            #take opponents name and team and acceptence/rejected outcome
            userTeam = session['userTeam']
            opUserName = session['opUserName']
            opDoc = db[opUserName].find_one({'contest':contest})
            if outcome == 'rejected':
                #if opponent already accpeted and this user then rejects, remove both users from potential
                if userName in opDoc['potential']:
                    db[opUserName].update({'contest':contest},{'$pull':{'potential':userName}})
                if opUserName in userDoc['potential']:
                    db[userName].update({'contest':contest},{'$pull':{'potential':opUserName}})
                db[userName].update({'contest':contest},{'$push':{'rejected':opUserName}})
                db[opUserName].update({'contest':contest},{'$push':{'rejected':userName}})
                return redirect(url_for('matchups'))
                #return render_template('matchups.html')
            elif outcome == 'accepted' and opUserName in userDoc['potential']:
                #remove users from eachotheres potentials
                db[opUserName].update({'contest':contest},{'$pull':{'potential':userName}})
                db[userName].update({'contest':contest},{'$pull':{'potential':opUserName}})
                opTeam = session['opTeam']
                #both parties accept!! 1)insert matchObj, update each players potential pool
                #redirect to a matchups both only with a popup asking to set wager
                match = estabMatch(userTeam,opTeam)
                matchId = match['matchId']
                #inset match into both teams contest matches, also master match doc
                db[userName].update({'contest':contest},{'$push':{'matchups':match}})
                db[opUserName].update({'contest':contest},{'$push':{'matchups':match}})
                ### front end stuff
                #algo to find sugWager
                print 'its a match'
                #return render_template('matchups.html', match=True,userName=session['userName'],opUserName=opUserName, userTeam=session['userTeam'], opTeam=opTeam,sugWager=sugWager)
                return redirect(url_for('contest', matchId=matchId))
            else:
                #add userName to opponents potential games
                db[opUserName].update({'contest':contest},{'$push':{'potential':userName}})
                db[userName].update({'contest':contest},{'$push':{'accepted':opUserName}})
                print 'did it'
                #return redirect(url_for('matchups'))
                return render_template('matchups.html')

        else:
            #check to see if somebody already accepted vs users teamse
            #else grab random player from pool
            #potMatch = db[userName].find_one({'contest':contest})
            potential = userDoc['potential']
            #if no potential matches
            if potential == []:
                #grab available pool and take away users rejected list
                rejected = userDoc['rejected']
                accepted = userDoc['accepted']
                #potential = userDoc['potential']
                #contestDoc = dbContests[contest].find_one({'contest':contest})
                #pool = contestDoc['pool']
                pool.remove(userName)
                #availList is all the pool subtract the users already rejected list
                availList = list(set(pool)-set(rejected)-set(accepted)-set(potential))
                #count of number of people in contest pool
                count = len(availList)-1
                #if count = -1, then render 'no matches available :('
                if len(availList) == 0:
                    error = 'there are no possible matchs at this moment :('
                    return render_template('matchups.html', error=error)
                else:
                    randNum = randint(0,count)
                    #check that random user isnt in rejected pile already
                    opUserName = availList[randNum]
                    #opUserName = 'daCane'
                    opDoc = db[opUserName].find_one({'contest':contest})
                    opRankings = {'qb':opDoc['qbr'],'rb':opDoc['rbr'],'wr':opDoc['wrr'],'te':opDoc['ter'],'defst':opDoc['defstr']}
                    if createSmallMatchup(userRankings,opRankings) == False:
                        #put each users in rejected
                        db[userName].update({'contest':contest},{'$push':{'rejected':opUserName}})
                        db[opUserName].update({'contest':contest},{'$push':{'rejected':userName}})
                        print 'redirected'
                        #return render_template('matchups.html')
                        return redirect(url_for('home'))
                    else:
                        opUserName = opUserName
                        opDoc = db[opUserName].find_one({'contest':contest})
                        opRankings = {'user':opUserName,'qb':opDoc['qbr'],'rb':opDoc['rbr'],'wr':opDoc['wrr'],'te':opDoc['ter'],'defst':opDoc['defstr']}
                        userTeam, opTeam = createSmallMatchup(userRankings, opRankings)
                        session['userTeam'] = userTeam
                        session['opTeam'] = opTeam
                        session['opUserName'] = opUserName
                        print 'did random match'
                        return render_template('matchups.html', userTeam = userTeam, opTeam=opTeam,
                            opUserName=opUserName)
            else:
                #grab first off of potential matches
                opUserName = potential[0]
                opDoc = db[opUserName].find_one({'contest':contest})
                opRankings = {'qb':opDoc['qbr'],'rb':opDoc['rbr'],'wr':opDoc['wrr'],'te':opDoc['ter'],'defst':opDoc['defstr']}
                userTeam, opTeam = createSmallMatchup(userRankings,opRankings)
                session['userTeam'] = userTeam
                session['opTeam'] = opTeam
                session['opUserName'] = opUserName
                return render_template('matchups.html', userTeam = userTeam, opTeam=opTeam, userName=userName,
                    opUserName=opUserName)

@app.route('/rankings')
@login_required
def rankings():
    contest = 'nfl1'
    week = 'NFL Week 1 Rankings'
    user = session['userName']
    #if user already has rankings made
    if db[user].find_one({'contest':contest}):
        rankings = {'qbr':[],'rbr':[],'wrr':[],'ter':[],'defstr':[]}
        userDoc = db[user].find_one({'contest':contest})
        rankings['qbr'] = userDoc['qbr']
        rankings['rbr'] = userDoc['rbr']
        rankings['wrr'] = userDoc['wrr']
        rankings['ter'] = userDoc['ter']
        rankings['defstr'] = userDoc['defstr']

        return render_template('rankings.html', rankings=rankings,week=week)
    #grab default rankings for the week
    else:
        rankings = {'qbr':[],'rbr':[],'wrr':[],'ter':[],'defstr':[]}
        defaultDoc = dbContests[contest].find_one({'contest':contest})
        rankings['qbr'] = defaultDoc['qbs']
        rankings['rbr'] = defaultDoc['rbs']
        rankings['wrr'] = defaultDoc['wrs']
        rankings['ter'] = defaultDoc['tes']
        rankings['defstr'] = defaultDoc['defsts']

        return render_template('rankings.html', rankings=rankings,week=week)

@app.route('/setRankings',methods=['POST'])
@login_required
def setRankings():
    contest = 'nfl1'
    #default player dict objs from mongo
    defaultDoc = dbContests[contest].find_one({'contest':contest})
    qbs = defaultDoc['qbs']
    rbs = defaultDoc['rbs']
    wrs = defaultDoc['wrs']
    tes = defaultDoc['tes']
    defsts = defaultDoc['defsts']
    if request.method == 'POST':
        rankings = convert(request.json)
        qbrList = rankings['qbr']
        rbrList = rankings['rbr']
        wrrList = rankings['wrr']
        terList = rankings['ter']
        defstrList = rankings['defstr']

        #convert rankings from list to dict obj
        qbr = []
        for qbl in qbrList:
            for qbd in qbs:
                if qbd['name'] == qbl:
                    qbr.append({'name':qbl,'opp':qbd['opp']})
                else:
                    pass
        rbr = []
        for rbl in rbrList:
            for rbd in rbs:
                if rbd['name'] == rbl:
                    rbr.append({'name':rbl,'opp':rbd['opp']})
                else:
                    pass
        wrr = []
        for wrl in wrrList:
            for wrd in wrs:
                if wrd['name'] == wrl:
                    wrr.append({'name':wrl,'opp':wrd['opp']})
                else:
                    pass
        ter = []
        for tel in terList:
            for ted in tes:
                if ted['name'] == tel:
                    ter.append({'name':tel,'opp':ted['opp']})
                else:
                    pass
        defstr = []
        for defstl in defstrList:
            for defstd in defsts:
                if defstd['name'] == defstl:
                    defstr.append({'name':defstl,'opp':defstd['opp']})
                else:
                    pass

        userCol = db[session['userName']]
        if userCol.find_one({'contest':contest}):
            #update users week lineup
            userCol.update({'contest':contest},
                {'$set':{'qbr':qbr,'rbr':rbr,'wrr':wrr,'ter':ter,'defstr':defstr,'potential':[],'rejected':[],'accepted':[]}})
            return 'you are good'
        else:
            doc = {
                'qbr': qbr,
                'rbr': rbr,
                'wrr': wrr,
                'ter': ter,
                'defstr': defstr,
                'contest': contest,
                'potential': [],
                'rejected': [],
                'accepted': []
            }
            userCol.insert(doc)
            #add user to pool
            #adminDoc = dbContests[contest].find_one({'type':admin})
            dbContests[contest].update({'contest':contest},{'$push':{'pool':session['userName']}})
            return 'you are good'

@app.route('/')
@login_required
def home():
    return render_template('home.html')

@app.route('/account')
@login_required
def account():
    return render_template('account.html')

@app.route('/login', methods=['GET','POST'])
def login():
    error = None
    if request.method == 'POST':
        userName = request.form['userName']
        if userName not in db.collection_names():
            error = userName+' is not found.'
            return render_template('login.html',error=error)
        else:
            pwd = request.form['pwd']
            res = db[userName].find_one({'userName':userName})
            hashpwd = res['pwd']
            pwdCheck = pbkdf2_sha256.verify(pwd, hashpwd)
            if pwdCheck == False:
                error = 'incorrect password'
                return render_template('login.html', error=error)
            else:
                #set session
                session['logged_in'] = True
                session['userName'] = userName
                doc = db[userName].find_one({'userName':userName})
                session['balance'] = doc['balance']
                session.permanent = True
                app.permanent_session_lifetime = timedelta(minutes=60)
                #if rankings have been sent, redirect to find match
                #else redirect to set rankings
                return redirect(url_for('home'))
    else:
        return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        userName = request.form['userName']
        email = request.form['email']
        pwd = request.form['pwd']
        rpwd = request.form['rpwd']
        hashpwd = pbkdf2_sha256.encrypt(pwd, rounds=20000, salt_size=16)
        #get all registered emails
        emails = []
        for name in db.collection_names():
            userCol = db[name]
            doc = userCol.find_one({'userName':name})
            if type(doc) != dict:
                pass
            else:
                emails.append(doc['email'])
        #start checking user validation
        error = None
        if email=='' or firstName=='' or lastName=='' or pwd=='' or rpwd=='' or userName=='':
            error = 'please fill in all data'
            return render_template('register.html', error=error)
        elif pwd != rpwd:
            error = 'passwords dont match, try again'
            return render_template('register.html', error=error)
        elif userName in db.collection_names():
            error = email+' has already been registered'
            return render_template('register.html', error=error)
        elif email in emails:
            error = userName+' has been taken'
            return render_template('register.html', error=error)
        else:
            #insert the user to database
            userDoc = {
                'userName':userName,
                'firstName':firstName,
                'lastName':lastName,
                'pwd':hashpwd,
                'email':email,
                'balance':100
            }
            #cur.execute("INSERT INTO users(firstName,lastName,email,userName,pwd) VALUES(%s,%s,%s,%s,%s)",[firstName,lastName,email,userName,hashpwd])
            #db.commit()
            #create mongo stuff
            userCol = db[userName]
            userCol.insert(userDoc)
            session['logged_in'] = True
            session['userName'] = userName
            return redirect(url_for('home'))
    else:
        return render_template('register.html')

### Mobile stuff ###
@app.route('/mlogin', methods=['GET','POST'])
def mlogin():
    if request.method == 'POST':
        #userName = request.args.get('userName')
        userName = request.form.get("userName")
        pwd = request.form.get("pwd")
        mtoken = request.form.get("mtoken")
        if userName not in db.collection_names():
            #error = userName+' is not found.'
            #return json.dumps({'passed':'no un'})
            return 'no un'
        else:
            #pwd = request.args.get('pwd')
            userDoc = db[userName].find_one({'userName':userName})
            hashpwd = userDoc['pwd']
            pwdCheck = pbkdf2_sha256.verify(pwd, hashpwd)
            if pwdCheck == False:
                #error = 'incorrect password'
                #return json.dumps({'passed':'no pass'})
                return 'no pass'
            else:
                #mtoken = request.args.get('mtoken')
                #set session
                #session['mlogged_in'] = True
                #session['userName'] = userName
                #userDoc = db[userName].find_one({'userName':userName})
                #userDoc.update({'$set':{'mToken':mtoken}})
                db[userName].update({'userName':userName},{'$set':{'mToken':mtoken}})
                #session['balance'] = doc['balance']
                #session.permanent = True
                #app.permanent_session_lifetime = timedelta(minutes=60)
                #if rankings have been sent, redirect to find match
                #else redirect to set rankings
                #return json.dumps({'passed':'yes'})
                return 'yes'
    else:
        return json.dumps({'passed':'not a page'})

@app.route('/mtest', methods=['GET','POST'])
def mtest():
    if request.method == 'POST':
        number = request.form['number']
        message = request.form['message']
        doc = {'msg':message,'num':number}
        db['dough'].insert(doc)
        return json.dumps({'type':'post'})
    elif request.method == 'GET':
        number = request.args.get('number')
        message = request.args.get('message')
        doc = {'msg':message,'num':number}
        db['dough'].insert(doc)
        return json.dumps({'type':'get'})

@app.route('/mgetBal', methods=['GET','POST'])
def mgetBal():
    if request.method == 'GET':
        userName = request.args.get('userName')
        #un = session['userName']
        userDoc = db[userName].find_one({'userName':userName})
        bal = str(userDoc['balance'])
        #return json.dumps({'bal':bal})
        return bal
    else:
        return 'nopers'

@app.route('/mgetPos', methods=['GET'])
def mgetPos():
    if request.method == 'GET':
        pos = request.args.get('pos')
        mtoken = request.args.get('mtoken')
        for name in db.collection_names():
            userCol = db[name]
            if userCol.find_one({'mToken':mtoken}):
                userDoc = userCol.find_one({'mToken':mtoken})
                userName = userDoc['userName']
                userContestDoc = db[userName].find_one({'contest':'nfl1'})
                posr = userContestDoc[pos+'r']
                posStr = pos+'r'
                return json.dumps({posStr:posr})
            else:
                pass

@app.route('/msetRank',methods=['GET','POST'])
def msetRank():
    #check to see if its first time setting by seeing if user is in contest pool already
    #session['userName'] this needs happen for security reasons
    #contest = 'nfl1'
    #get json array
    if request.method == 'POST':
        #get post json data
        params = convert(request.json)
        pos = params['pos']
        newOrder = params['newOrder']
        mtoken = params['mtoken']
        contest = params['contest']

        #verify token to team !!!!!!! try to figure out sessions cookie method (preferred)
        #also implement a break in for loop, or while loop with a boolean foundVar
        for name in db.collection_names():
            userCol = db[name]
            if userCol.find_one({'mToken':mtoken}):
                doc = userCol.find_one({'mToken':mtoken})
                userName = doc['userName']

                #set new order -- also have to determine if first time setting order
                #an order has been established already
                if userCol.find_one({'contest':contest}):
                    #update positions ranking
                    #create new ranking list of dicts
                    newRank = []
                    posStr = pos+'r'
                    #update ranking
                    if posStr != 'defstr':
                        for lv in newOrder:
                            player, opp = lvToPlayer(lv)
                            newRank.append({'name':player,'opp':opp})
                        db[userName].update({'contest':contest},{'$set':{posStr:newRank}})
                        return 'updated '+posStr
                    #its the def ranking so add the user to the pool if hasnt been already added
                    else:
                        for lv in newOrder:
                            player, opp = lvToPlayer(lv)
                            newRank.append({'name':player,'opp':opp})
                        db[userName].update({'contest':contest},{'$set':{posStr:newRank}})

                        #if its defst and user hasnt been added to pool, then enter the user to the contest pool
                        contestDoc = dbContests[contest].find_one({'contest':contest})
                        contestPool = contestDoc['pool']

                        if userName not in contestPool:
                            dbContests[contest].update({'contest':contest},{'$push':{'pool':userName}})
                            return 'updated defstr AND added user to contest'
                        else:
                            return 'updated defstr'



                #first time entering contest
                else:
                    #create contest doc for users collection
                    defaultDoc = dbContests[contest].find_one({'contest':contest})
                    qbs = []
                    for lv in newOrder:
                        player, opp = lvToPlayer(lv)
                        qbs.append({'name':player,'opp':opp})
                    rbs = defaultDoc['rbs']
                    wrs = defaultDoc['wrs']
                    tes = defaultDoc['tes']
                    defsts = defaultDoc['defsts']
                    #create new contest doc for user BUT dont add them to the pool til
                    #they cick 'enter' after ranking defsts
                    doc = {
                        'qbr': qbs,
                        'rbr': rbs,
                        'wrr': wrs,
                        'ter': tes,
                        'defstr': defsts,
                        'contest': contest,
                        'potential': [],
                        'rejected': [],
                        'accepted': []
                    }
                    userCol.insert(doc)
                    return 'need to build obj'

            else:
                pass

@app.route('/mgetContests',methods=['GET'])
def mgetContests():
    if request.method == 'GET':
        #contests = ['NFL week 1','NCAAF week 1']
        #return json.dumps({'contests':contests})
        return json.dumps({'ncaa':'NCAAF week 1','nfl':'NFL week 1','ncaaCode':'ncaa1','nflCode':'nfl1'})

#code to find WORKABLE matchups
@app.route('/mmatchups', methods=['GET','POST'])
#do token verification
def mmatchups():
    error = None
    contest = 'nfl1'
    if request.method == 'GET':
        token = request.args.get('token')

        #token verification
        for name in db.collection_names():
            userCol = db[name]
            if userCol.find_one({'mToken':token}):
                userDoc = userCol.find_one({'mToken':token})
                userName = userDoc['userName']
                contestDoc = dbContests[contest].find_one({'contest':contest})
                userContestDoc = db[session['userName']].find_one({'contest':contest})
                pool = contestDoc['pool']
                #continue logic to send back a workable matchup
                #check to see if rankings have been entered
                if userContestDoc == None:
                    #redirect to qbDSLV
                    return 'no rankings'
                #check to find if any matches are avaialbe
                elif pool == []:
                    return 'no available'
                else:
                    userName = session['userName']
                    #userDoc = db[userName].find_one({'contest':contest})
                    userRankings = {'user':userName,'qb':userContestDoc['qbr'],'rb':userContestDoc['rbr'],'wr':userContestDoc['wrr'],'te':userContestDoc['ter'],'defst':userContestDoc['defstr']}
                    userRankings = convert(userRankings)
                    if request.method == 'POST':
                        outcome = request.form['outcome']
                        #when recieving decision on match
                        #take opponents name and team and acceptence/rejected outcome
                        userTeam = session['userTeam']
                        opUserName = session['opUserName']
                        opDoc = db[opUserName].find_one({'contest':contest})
                        if outcome == 'rejected':
                            #if opponent already accpeted and this user then rejects, remove both users from potential
                            if userName in opDoc['potential']:
                                db[opUserName].update({'contest':contest},{'$pull':{'potential':userName}})
                            if opUserName in userDoc['potential']:
                                db[userName].update({'contest':contest},{'$pull':{'potential':opUserName}})
                            db[userName].update({'contest':contest},{'$push':{'rejected':opUserName}})
                            db[opUserName].update({'contest':contest},{'$push':{'rejected':userName}})
                            return redirect(url_for('matchups'))
                            #return render_template('matchups.html')
                        elif outcome == 'accepted' and opUserName in userDoc['potential']:
                            #remove users from eachotheres potentials
                            db[opUserName].update({'contest':contest},{'$pull':{'potential':userName}})
                            db[userName].update({'contest':contest},{'$pull':{'potential':opUserName}})
                            opTeam = session['opTeam']
                            #both parties accept!! 1)insert matchObj, update each players potential pool
                            #redirect to a matchups both only with a popup asking to set wager
                            match = estabMatch(userTeam,opTeam)
                            matchId = match['matchId']
                            #inset match into both teams contest matches, also master match doc
                            db[userName].update({'contest':contest},{'$push':{'matchups':match}})
                            db[opUserName].update({'contest':contest},{'$push':{'matchups':match}})
                            ### front end stuff
                            #algo to find sugWager
                            print 'its a match'
                            #return render_template('matchups.html', match=True,userName=session['userName'],opUserName=opUserName, userTeam=session['userTeam'], opTeam=opTeam,sugWager=sugWager)
                            return redirect(url_for('contest', matchId=matchId))
                        else:
                            #add userName to opponents potential games
                            db[opUserName].update({'contest':contest},{'$push':{'potential':userName}})
                            db[userName].update({'contest':contest},{'$push':{'accepted':opUserName}})
                            print 'did it'
                            #return redirect(url_for('matchups'))
                            return render_template('matchups.html')

                    else:
                        #check to see if somebody already accepted vs users teamse
                        #else grab random player from pool
                        #potMatch = db[userName].find_one({'contest':contest})
                        potential = userDoc['potential']
                        #if no potential matches
                        if potential == []:
                            #grab available pool and take away users rejected list
                            rejected = userDoc['rejected']
                            accepted = userDoc['accepted']
                            #potential = userDoc['potential']
                            #contestDoc = dbContests[contest].find_one({'contest':contest})
                            #pool = contestDoc['pool']
                            pool.remove(userName)
                            #availList is all the pool subtract the users already rejected list
                            availList = list(set(pool)-set(rejected)-set(accepted)-set(potential))
                            #count of number of people in contest pool
                            count = len(availList)-1
                            #if count = -1, then render 'no matches available :('
                            if len(availList) == 0:
                                error = 'there are no possible matchs at this moment :('
                                return render_template('matchups.html', error=error)
                            else:
                                randNum = randint(0,count)
                                #check that random user isnt in rejected pile already
                                opUserName = availList[randNum]
                                #opUserName = 'daCane'
                                opDoc = db[opUserName].find_one({'contest':contest})
                                opRankings = {'qb':opDoc['qbr'],'rb':opDoc['rbr'],'wr':opDoc['wrr'],'te':opDoc['ter'],'defst':opDoc['defstr']}
                                if createSmallMatchup(userRankings,opRankings) == False:
                                    #put each users in rejected
                                    db[userName].update({'contest':contest},{'$push':{'rejected':opUserName}})
                                    db[opUserName].update({'contest':contest},{'$push':{'rejected':userName}})
                                    print 'redirected'
                                    #return render_template('matchups.html')
                                    return redirect(url_for('home'))
                                else:
                                    opUserName = opUserName
                                    opDoc = db[opUserName].find_one({'contest':contest})
                                    opRankings = {'user':opUserName,'qb':opDoc['qbr'],'rb':opDoc['rbr'],'wr':opDoc['wrr'],'te':opDoc['ter'],'defst':opDoc['defstr']}
                                    userTeam, opTeam = createSmallMatchup(userRankings, opRankings)
                                    session['userTeam'] = userTeam
                                    session['opTeam'] = opTeam
                                    session['opUserName'] = opUserName
                                    print 'did random match'
                                    return render_template('matchups.html', userTeam = userTeam, opTeam=opTeam,
                                        opUserName=opUserName)
                        else:
                            #grab first off of potential matches
                            opUserName = potential[0]
                            opDoc = db[opUserName].find_one({'contest':contest})
                            opRankings = {'qb':opDoc['qbr'],'rb':opDoc['rbr'],'wr':opDoc['wrr'],'te':opDoc['ter'],'defst':opDoc['defstr']}
                            userTeam, opTeam = createSmallMatchup(userRankings,opRankings)
                            session['userTeam'] = userTeam
                            session['opTeam'] = opTeam
                            session['opUserName'] = opUserName
                            return render_template('matchups.html', userTeam = userTeam, opTeam=opTeam, userName=userName,
                                opUserName=opUserName)

@app.route('/mgetMatch', methods=['GET','POST'])
def mgetMatch():
    if request.method == 'GET':
        mtoken = request.args.get('mtoken')
        contest = request.args.get('contest')
        #contest = 'nfl1'
        contestDoc = dbContests[contest].find_one({'contest':contest})
        pool = contestDoc['pool']

        for name in db.collection_names():
            userCol = db[name]
            if userCol.find_one({'mToken':mtoken}):
                userDoc = userCol.find_one({'mToken':mtoken})
                userName = userDoc['userName']

                contestDoc = dbContests[contest].find_one({'contest':contest})
                userContestDoc = db[userName].find_one({'contest':contest})
                #pool = contestDoc['pool']
                #check to see if rankings have been entered
                if userDoc == None:
                    return 'no rankings entered'
                #check to find if any matches are avaialbe, first to enter
                elif pool == []:
                    return 'no possible matches'
                else:
                    userRankings = {'user':userName,'qb':userContestDoc['qbr'],'rb':userContestDoc['rbr'],'wr':userContestDoc['wrr'],'te':userContestDoc['ter'],'defst':userContestDoc['defstr']}
                    userRankings = convert(userRankings)

                    #check users potential
                    potential = userContestDoc['potential']
                    #if no potential matches
                    if potential == []:
                        #grab available pool and take away users rejected list
                        rejected = userContestDoc['rejected']
                        accepted = userContestDoc['accepted']

                        pool.remove(userName)
                        #availList is all the pool subtract the users already rejected list
                        availList = list(set(pool)-set(rejected)-set(accepted)-set(potential))
                        #count of number of people in contest pool
                        count = len(availList)-1
                        #if count = -1, then render 'no matches available :('
                        if len(availList) == 0:
                            return 'no possible matches'
                        else:
                            #grab random opponent
                            randNum = randint(0,count)
                            #check that random user isnt in rejected pile already
                            opUserName = availList[randNum]
                            #opUserName = 'daCane'
                            opContestDoc = db[opUserName].find_one({'contest':contest})
                            opRankings = {'qb':opContestDoc['qbr'],'rb':opContestDoc['rbr'],'wr':opContestDoc['wrr'],'te':opContestDoc['ter'],'defst':opContestDoc['defstr']}
                            convert(opRankings)

                            #tried to make a match, however its impossible to make a match
                            if createSmallMatchup(userRankings,opRankings) == False:
                                #put each users in rejected
                                db[userName].update({'contest':contest},{'$push':{'rejected':opUserName}})
                                db[opUserName].update({'contest':contest},{'$push':{'rejected':userName}})
                                #return render_template('matchups.html')
                                return 'match not possible'
                            else:
                                #else return the random match
                                #opUserName = opUserName
                                #not needed?#opDoc = db[opUserName].find_one({'contest':contest})
                                #not needed?#opRankings = {'user':opUserName,'qb':opDoc['qbr'],'rb':opDoc['rbr'],'wr':opDoc['wrr'],'te':opDoc['ter'],'defst':opDoc['defstr']}
                                userTeam, opTeam = createSmallMatchup(userRankings, opRankings)
                                #return json of match data
                                data = teamToJson(userTeam,opTeam,userName,opUserName,contest,None)

                                #add match to contestCollection
                                return json.dumps(data)
                    else:
                        #grab already made match by opponent
                        opUserName = potential[0]
                        contestDoc1 = dbContests[contest].find_one({'$and':[{'team1user':userName},{'team2user':opUserName}]})
                        contestDoc2 = dbContests[contest].find_one({'$and':[{'team2user':userName},{'team1user':opUserName}]})

                        #get match and send json to client
                        if contestDoc1:
                            userTeam = contestDoc1['team1']
                            opTeam = contestDoc1['team2']
                            matchId = contestDoc1['matchId']
                            data = teamToJson(userTeam,opTeam,userName,opUserName,contest,matchId)
                            return json.dumps(data)
                        elif contestDoc2:
                            userTeam = contestDoc1['team2']
                            opTeam = contestDoc1['team1']
                            matchId = contestDoc1['matchId']
                            data = teamToJson(userTeam,opTeam,userName,opUserName,contest,matchId)
                            return json.dumps(data)
                        else:
                            #return json saying error
                            return 'error'
            else:
                pass


@app.route('/mpostMatch', methods=['POST'])
def mpostMatch():
    if request.method == 'POST':
        #mtoken = request.form['mtoken']
        jsonData = request.get_json()
        convert(jsonData)
        #return str(json)
        #outcome = request.form['outcome']
        #contest = request.form['contest']
        outcome = jsonData['outcome']
        contest = jsonData['contest']
        mtoken = jsonData['mtoken']

        #return str(outcome)
        for name in db.collection_names():
            userCol = db[name]
            if userCol.find_one({'mToken':mtoken}):
                userDoc = userCol.find_one({'mToken':mtoken})
                userName = userDoc['userName']
                userContestDoc = db[userName].find_one({'contest':contest})
                opUserName = jsonData['opTeam']
                opUserDoc = db[opUserName].find_one({'userName':opUserName})
                opContestDoc = db[opUserName].find_one({'contest':contest})

                if outcome == 'reject':
                    #if opponent already accpeted and this user then rejects, remove both users from potential
                    if userName in opContestDoc['potential']:
                        db[opUserName].update({'contest':contest},{'$pull':{'potential':userName}})
                    if opUserName in userContestDoc['potential']:
                        db[userName].update({'contest':contest},{'$pull':{'potential':opUserName}})
                    db[userName].update({'contest':contest},{'$push':{'rejected':opUserName}})
                    db[opUserName].update({'contest':contest},{'$push':{'rejected':userName}})

                    #delete match doc if there is one
                    #search by username opusername and contest
                    findContest1 = dbContests[contest].find_one({'$and':[{'team1user':userName},{'team2user':opUserName}]})
                    findContest2 = dbContests[contest].find_one({'$and':[{'team2user':userName},{'team1user':opUserName}]})
                    if findContest1:
                        dbContests.remove({'team1user':userName})
                    elif findContest2:
                        dbContests.remove({'team2user':userName})
                    else:
                        pass

                    return json.dumps({'matchResp':'rejection completed','maxWager':None,'matchId':None})
                elif outcome == 'accepted' and opUserName in userContestDoc['potential']:
                    #get max balance between users
                    userBal = userDoc['balance']
                    opUserBal = opUserDoc['balance']
                    maxWager = min(userBal, opUserBal)

                    #remove users from eachotheres potentials
                    db[opUserName].update({'contest':contest},{'$pull':{'potential':userName}})
                    db[userName].update({'contest':contest},{'$pull':{'potential':opUserName}})
                    #both parties accept!! 1)insert matchObj, update each players potential pool
                    #redirect to a matchups both only with a popup asking to set wager
                    match = estabMatch(userTeam,opTeam)
                    matchId = match['matchId']
                    #inset match into both teams contest matches, also master match doc
                    db[userName].update({'contest':contest},{'$push':{'matchups':match}})
                    db[opUserName].update({'contest':contest},{'$push':{'matchups':match}})
                    ### front end stuff

                    #return render_template('matchups.html', match=True,userName=session['userName'],opUserName=opUserName, userTeam=session['userTeam'], opTeam=opTeam,sugWager=sugWager)
                    return json.dumps({'matchResp':'matched','maxWager':maxWager,'matchId':matchId})
                else:
                    #create a match and
                    #add userName to opponents potential games
                    db[opUserName].update({'contest':contest},{'$push':{'potential':userName}})
                    db[userName].update({'contest':contest},{'$push':{'accepted':opUserName}})

                    #establish potential match
                    #match = estabMatch()


                    #return redirect(url_for('matchups'))
                    return json.dumps({'matchResp':'added user to opponents potential','maxWager':None,'matchId':None})
            else:
                pass

@app.route('/mbarter', methods=['GET'])
def mbarter():
    #get barter matchup
    if request.method == 'GET':
        mtoken = request.args.get('mtoken')
        matchId = request.args.get('matchId')
        contest = request.args.get('contest')

        for name in db.collection_names():
            userCol = db[name]
            if userCol.find_one({'mToken':mtoken}):
                userDoc = userCol.find_one({'mToken':mtoken})
                userName = userDoc['userName']

                matchDoc = dbContests[contest].find_one({'matchId':matchId})

                opUserName = None
                opTeam = None
                userTeam = None

                #figure out opUserName
                if userName == matchDoc['team1user']:
                    opUserName = matchDoc['team2user']
                    opTeam = matchDoc['team2']
                    userTeam = matchDoc['team1']
                else:
                    opUserName = matchDoc['team1user']
                    opTeam = matchDoc['team1']
                    userTeam = matchDoc['team2']

                data = teamToJson(userTeam,opTeam,userName,opUserName,contest)

                #get max balance between users
                opUserDoc = db[opUserName].find_one({'userName':opUserName})
                userBal = userDoc['balance']
                opUserBal = opUserDoc['balance']
                maxWager = min(userBal, opUserBal)

                #currentWager
                currentWager = matchDoc['wager']

                #get maxWager
                data['maxWager'] = str(maxWager)
                data['currentWager'] = str(currentWager)
                return json.dumps(data)
            else:
                pass

@app.route('/msetWager', methods=['POST'])
def msetWager():
    #receieve token and matchId, and set matchId to new wager
    #response back with string of 'posted successful'
    if request.method == 'POST':
        jsonData = request.get_json()
        convert(jsonData)

        #get post parameters
        mtoken = jsonData['mtoken']
        matchId = jsonData['matchId']
        wager = jsonData['wager']
        contest = jsonData['contest']

        for name in db.collection_names():
            userCol = db[name]
            if userCol.find_one({'mToken':mtoken}):
                userDoc = userCol.find_one({'mToken':mtoken})
                userName = userDoc['userName']
                opUserName = None

                #get match doc
                matchDoc = dbContests[contest].find_one({'matchId':matchId})
                #figure out opUserName
                if userName == matchDoc['team1user']:
                    opUserName = matchDoc['team2user']
                else:
                    opUserName = matchDoc['team1user']

                #get user and opponents balances & maxWager
                opUserDoc = db[opUserName].find_one({'userName':opUserName})
                userBal = userDoc['balance']
                opUserBal = opUserDoc['balance']
                maxWager = min(userBal, opUserBal)

                if wager > userBal:
                    return json.dumps({'outcome':'user insufficient','maxWager':maxWager})
                elif wager > opUserBal:
                    return json.dumps({'outcome':'opp insufficient','maxWager':maxWager})
                else:
                    dbContests[contest].update({'matchId':matchId},{'$set':{'wager':wager,'turn':opUserName}})
                    return json.dumps({'outcome':'set new wager and turn'})
            else:
                pass

@app.route('/mgetPotential', methods=['GET'])
def mgetPotential():
    if request.method == 'GET':
        mtoken = request.args.get('mtoken')
        for name in db.collection_names():
            userCol = db[name]
            if userCol.find_one({'mToken':mtoken}):
                userDoc = userCol.find_one({'mToken':mtoken})
                userName = userDoc['userName']

                #get all users potential matches || when scaling larger, give each users collection potential match docs
                potMatches = []
                matchIds = []
                contests = ['nfl1']
                #redo contestList better
                contestList = []

                for contest in contests:
                    #dbContests[contest].find('$and':[{'state':'potential'},{'$or':[{'team1user':userName},{'team2user':userName}]}])
                    for matchDoc in dbContests[contest].find({'$and':[{'state':'potential'},{'$or':[{'team1user':userName},{'team2user':userName}]}]}):
                        #potMatches.append(match)
                        opUserName = None
                        if userName == matchDoc['team1user']:
                            opUserName = matchDoc['team2user']
                        else:
                            opUserName = matchDoc['team1user']
                        matchStr = contest+' | '+opUserName+' | $'+str(matchDoc['wager'])
                        potMatches.append(matchStr)
                        matchIds.append(matchDoc['matchId'])
                        contestList.append(contest)
                return json.dumps({'matches':potMatches,'matchIds':matchIds,'contestList':contestList})
            else:
                pass

@app.route('/maccept', methods=['POST'])
def maccept():
    if request.method == 'POST':
        jsonData = request.get_json()
        convert(jsonData)

        #get post parameters
        mtoken = jsonData['mtoken']
        matchId = jsonData['matchId']
        contest = jsonData['contest']

        for name in db.collection_names():
            userCol = db[name]
            if userCol.find_one({'mToken':mtoken}):
                userDoc = userCol.find_one({'mToken':mtoken})
                userName = userDoc['userName']
                opUserName = None

                #get match doc
                matchDoc = dbContests[contest].find_one({'matchId':matchId})
                wager = matchDoc['wager']
                #figure out opUserName
                if userName == matchDoc['team1user']:
                    opUserName = matchDoc['team2user']
                else:
                    opUserName = matchDoc['team1user']

                #get balances & maxWager
                opUserDoc = db[opUserName].find_one({'userName':opUserName})
                userBal = userDoc['balance']
                opUserBal = opUserDoc['balance']
                maxWager = min(userBal, opUserBal)

                #finalize match
                if wager > userBal:
                    return json.dumps({'outcome':'user insufficient','maxWager':str(maxWager)})
                elif wager > opUserBal:
                    return json.dumps({'outcome':'opp insufficient','maxWager':str(maxWager)})
                else:
                    #change state of contest to accepted anc close it
                    newUserBal = userBal-wager
                    newOpUserBal = opUserBal-wager
                    db[userName].update({'userName':userName},{'$set':{'balance':newUserBal}})
                    db[opUserName].update({'userName':opUserName},{'$set':{'balance':newOpUserBal}})
                    dbContests[contest].update({'matchId':matchId},{'$set':{'state':'accepted','open':False}})
                    return json.dumps({'outcome':'match accepted','maxWager':str(maxWager)})
            else:
                pass

@app.route('/test', methods=['POST'])
def test():
    if request.method == 'POST':
        resp = convert(request.json)
        pos = resp['pos']
        newOrder = resp['newOrder']
        #rank = request.form['rank']
        #pos = request.form['pos']
        #doc = {'pos':pos,'rank':newOrder}
        #db['test'].insert(doc)
        newRank = []
        for lv in newOrder:
            player, opp = lvToPlayer(lv)
            newRank.append({'name':player,'opp':opp})
        db['test'].insert({'ranking':newRank})
        return 'inserted'

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(debug=True)