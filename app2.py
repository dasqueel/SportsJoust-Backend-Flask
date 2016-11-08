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
from flask.ext.login import LoginManager
from flask.ext.login import login_user
from models import User

# create the application object
app = Flask(__name__)
app.secret_key = os.urandom(24)
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "users.login"

### Supporting funcs ###
def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            return redirect(url_for('login'))
    return wrap

@login_manager.user_loader
def load_user(userid):
    return User.get(userid)
### ROUTES ###

###negotiation of potential contests code
@app.route('/potential_contest')
@login_required
def potential_contest():
    contest = 'nfl1'
    #get matchId from url
    matchId = request.args.get('matchId')
    session['matchId'] = matchId
    match = dbContests[contest].find_one({'matchId':matchId})
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
        opTeam = match['team2']
        userTeam = match['team1']
    else:
        opUserName = match['team1user']
        opTeam = match['team1']
        userTeam = match['team2']

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

###matchups functions
@app.route('/matchups', methods=['GET','POST'])
@login_required
def matchups():
    error = None
    contest = 'nfl1'
    contestDoc = dbContests[contest].find_one({'contest':contest})
    userName = session['userName']
    userDoc = db[userName].find_one({'contest':contest})
    if userDoc:
        userRankings = {'user':userName,'qb':userDoc['qbr'],'rb':userDoc['rbr'],'wr':userDoc['wrr'],'te':userDoc['ter'],'def':userDoc['defr']}
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
                pool = contestDoc['pool']
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
                    opRankings = {'qb':opDoc['qbr'],'rb':opDoc['rbr'],'wr':opDoc['wrr'],'te':opDoc['ter'],'def':opDoc['defr']}
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
                        opRankings = {'user':opUserName,'qb':opDoc['qbr'],'rb':opDoc['rbr'],'wr':opDoc['wrr'],'te':opDoc['ter'],'def':opDoc['defr']}
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
                opRankings = {'qb':opDoc['qbr'],'rb':opDoc['rbr'],'wr':opDoc['wrr'],'te':opDoc['ter'],'def':opDoc['defr']}
                userTeam, opTeam = createSmallMatchup(userRankings,opRankings)
                session['userTeam'] = userTeam
                session['opTeam'] = opTeam
                session['opUserName'] = opUserName
                return render_template('matchups.html', userTeam = userTeam, opTeam=opTeam, userName=userName,
                    opUserName=opUserName)
    else:
        return redirect(url_for('rankings'))

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

##rankings stuff
@app.route('/rankings')
@login_required
def rankings():
    contest = 'nfl1'
    week = 'NFL Week 1 Rankings'
    user = session['userName']
    #if user already has rankings made
    if db[user].find_one({'contest':contest}):
        rankings = {'qbr':[],'rbr':[],'wrr':[],'ter':[],'defr':[]}
        userDoc = db[user].find_one({'contest':contest})
        rankings['qbr'] = userDoc['qbr']
        rankings['rbr'] = userDoc['rbr']
        rankings['wrr'] = userDoc['wrr']
        rankings['ter'] = userDoc['ter']
        rankings['defr'] = userDoc['defr']

        return render_template('rankings.html', rankings=rankings,week=week)
    #grab default rankings for the week
    else:
        rankings = {'qbr':[],'rbr':[],'wrr':[],'ter':[],'defr':[]}
        defaultDoc = dbContests[contest].find_one({'contest':contest})
        rankings['qbr'] = defaultDoc['qb']
        rankings['rbr'] = defaultDoc['rb']
        rankings['wrr'] = defaultDoc['wr']
        rankings['ter'] = defaultDoc['te']
        rankings['defr'] = defaultDoc['def']

        return render_template('rankings.html', rankings=rankings,week=week)

@app.route('/setRankings',methods=['POST'])
@login_required
def setRankings():
    if request.method == 'POST':
        rankings = request.json
        qbr = rankings['qbr']
        rbr = rankings['rbr']
        wrr = rankings['wrr']
        ter = rankings['ter']
        defr = rankings['defr']
        contest = 'nfl1'

        userCol = db[session['userName']]
        if userCol.find_one({'contest':contest}):
            #update users week lineup
            userCol.update({'contest':contest},
                {'$set':{'qbr':qbr,'rbr':rbr,'wrr':wrr,'ter':ter,'defr':defr,'potential':[],'rejected':[],'accepted':[]}})
            return 'you are good'
        else:
            doc = {
                'qbr': qbr,
                'rbr': rbr,
                'wrr': wrr,
                'ter': ter,
                'defr': defr,
                'contest': contest,
                'potential': [],
                'rejected': [],
                'accepted': []
            }
            userCol.insert(doc)
            #add user to pool
            #adminDoc = dbContests[contest].find_one({'type':admin})
            dbContests[contest].update({'type':'admin'},{'$push':{'pool':session['userName']}})
            return 'you are good'

@app.route('/')
@login_required
def home():
    return redirect(url_for('rankings'))

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
                #session['logged_in'] = True
                #session['userName'] = userName
                doc = db[userName].find_one({'userName':userName})
                #session['balance'] = doc['balance']

                user = User(userName,doc['balance'],doc['_id'])
                login_user(user)
                #if rankings have been sent, redirect to find match
                #else redirect to set rankings
                return redirect(url_for('rankings'))
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

# start the server with the 'run()' method
if __name__ == '__main__':
    app.run(host='localhost',debug=True)