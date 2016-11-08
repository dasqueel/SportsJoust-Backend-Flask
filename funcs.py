import random
from pymongo import MongoClient
import string
#import players
import collections

def id_generator(size=20, chars=string.ascii_uppercase + string.digits):
   return ''.join(random.choice(chars) for _ in range(size))

#returns teams with no backups
def createSmallMatchup(rankings1, rankings2):
	#add userName to team object
	qb1 = rankings1['qb']
	rb1 = rankings1['rb']
	wr1 = rankings1['wr']
	te1 = rankings1['te']
	defst1 = rankings1['defst']
	qb2 = rankings2['qb']
	rb2 = rankings2['rb']
	wr2 = rankings2['wr']
	te2 = rankings2['te']
	defst2 = rankings2['defst']

	#check to see if both rankings have exact rankings for a position
	if qb1 == qb2 or rb1 == rb2 or wr1 == wr2 or te1 == te2 or defst1 == defst2:
		#pass and go to next user
		return False
	else:
		#final team objects
		team1 = {'qb':[],'rb':[],'wr':[],'te':[],'defst':[]}
		team2 = {'qb':[],'rb':[],'wr':[],'te':[],'defst':[]}

		while len(team1['qb']) == 0 and len(team2['qb']) == 0:
			if qb1[0] != qb2[0]:
				team1['qb'].append(qb1[0])
				team2['qb'].append(qb2[0])
			else:
				del qb1[0]
				del qb2[0]

		while len(team1['rb']) == 0 and len(team2['rb']) == 0:
			if rb1[0] != rb2[0]:
				team1['rb'].append(rb1[0])
				team2['rb'].append(rb2[0])
				if team1['rb'][0] in rb2:
					rb2.remove(team1['rb'][0])
				if team2['rb'][0] in rb1:
					rb1.remove(team2['rb'][0])
				del rb1[0]
				del rb2[0]
				while len(team1['rb']) == 1 and len(team2['rb']) == 1:
					if rb1 == [] or rb2 == []:
						return False
					elif rb1[0] != rb2[0]:
						team1['rb'].append(rb1[0])
						team2['rb'].append(rb2[0])
					else:
						del rb1[0]
						del rb2[0]
			else:
				del rb1[0]
				del rb2[0]

		while len(team1['wr']) == 0 and len(team2['wr']) == 0:
			if wr1[0] != wr2[0]:
				team1['wr'].append(wr1[0])
				team2['wr'].append(wr2[0])
				if team1['wr'][0] in wr2:
					wr2.remove(team1['wr'][0])
				if team2['wr'][0] in wr1:
					wr1.remove(team2['wr'][0])
				del wr1[0]
				del wr2[0]
				while len(team1['wr']) == 1 and len(team2['wr']) == 1:
					if wr1 == [] or wr2 == []:
						return False
					elif wr1[0] != wr2[0]:
						team1['wr'].append(wr1[0])
						team2['wr'].append(wr2[0])
					else:
						del wr1[0]
						del wr2[0]
			else:
				del wr1[0]
				del wr2[0]


		while len(team1['te']) == 0 and len(team2['te']) == 0:
			if te1[0] != te2[0]:
				team1['te'].append(te1[0])
				team2['te'].append(te2[0])
			else:
				del te1[0]
				del te2[0]

		while len(team1['defst']) == 0 and len(team2['defst']) == 0:
			if defst1[0] != defst2[0]:
				team1['defst'].append(defst1[0])
				team2['defst'].append(defst2[0])
			else:
				del defst1[0]
				del defst2[0]

		return team1, team2

#returns a matchObj dict
def estabMatch(team1, team2, team1user, team2user):
	matchId = id_generator()
	match = {
		'matchId': matchId,
		'team1user':team1user,
		'team2user':team2user,
		'team1':team1,
		'team2':team2,
		'state':'oneSideAccepted',
		'wager':None,
		'outcome':None,
		'open':True,
		'turn':None
	}
	return match

#convert unicode to string, for when jsonifying ranking data
def convert(data):
    if isinstance(data, basestring):
        return str(data)
    elif isinstance(data, collections.Mapping):
        return dict(map(convert, data.iteritems()))
    elif isinstance(data, collections.Iterable):
        return type(data)(map(convert, data))
    else:
        return data

#parse lv into player name and opp
def lvToPlayer(lv):
	pos = lv.find(' --')
	return lv[:pos], lv[pos+4:]

#go from team dict type to individual json type, along with concatinating player and opp to a lv type
def teamToJson(userTeam,opTeam,userName,opName,contest,matchId):
	if matchId == None:
		matchId = id_generator()
	json = {
		'uQb':userTeam['qb'][0]['name']+' -- '+userTeam['qb'][0]['opp'],
		'uRb1':userTeam['rb'][0]['name']+' -- '+userTeam['rb'][0]['opp'],
		'uRb2':userTeam['rb'][1]['name']+' -- '+userTeam['rb'][1]['opp'],
		'uWr1':userTeam['wr'][0]['name']+' -- '+userTeam['wr'][0]['opp'],
		'uWr2':userTeam['wr'][1]['name']+' -- '+userTeam['wr'][1]['opp'],
		'uTe':userTeam['te'][0]['name']+' -- '+userTeam['te'][0]['opp'],
		'uDef':userTeam['defst'][0]['name']+' -- '+userTeam['defst'][0]['opp'],
		'opTeam':opName,
		'opQb':opTeam['qb'][0]['name']+' -- '+opTeam['qb'][0]['opp'],
		'opRb1':opTeam['rb'][0]['name']+' -- '+opTeam['rb'][0]['opp'],
		'opRb2':opTeam['rb'][1]['name']+' -- '+opTeam['rb'][1]['opp'],
		'opWr1':opTeam['wr'][0]['name']+' -- '+opTeam['wr'][0]['opp'],
		'opWr2':opTeam['wr'][1]['name']+' -- '+opTeam['wr'][1]['opp'],
		'opTe':opTeam['te'][0]['name']+' -- '+opTeam['te'][0]['opp'],
		'opDef':opTeam['defst'][0]['name']+' -- '+opTeam['defst'][0]['opp'],
		'matchId':matchId
	}
	return json

#return each positions stats string, score, and teams total score
def getScores(contest, userTeam, opTeam):
	#get players for match
	#do api call to get real time stats - create stats String - and total the points
	contestStatDoc = dbStats[contest].find_one({'contest':contest})
	players = contestStatDoc['players']

	uQb = filter(lambda player: player['name'] == userTeam['qb'][0]['name'], players)[0]
	uRb1 = filter(lambda player: player['name'] == userTeam['rb'][0]['name'], players)[0]
	uRb2 = filter(lambda player: player['name'] == userTeam['rb'][1]['name'], players)[0]
	uWr1 = filter(lambda player: player['name'] == userTeam['wr'][0]['name'], players)[0]
	uWr2 = filter(lambda player: player['name'] == userTeam['wr'][1]['name'], players)[0]
	uTe = filter(lambda player: player['name'] == userTeam['te'][0]['name'], players)[0]
	uDefst = filter(lambda player: player['name'] == userTeam['defst'][0]['name'], players)[0]

	opQb = filter(lambda player: player['name'] == opTeam['qb'][0]['name'], players)[0]
	opRb1 = filter(lambda player: player['name'] == opTeam['rb'][0]['name'], players)[0]
	opRb2 = filter(lambda player: player['name'] == opTeam['rb'][1]['name'], players)[0]
	opWr1 = filter(lambda player: player['name'] == opTeam['wr'][0]['name'], players)[0]
	opWr2 = filter(lambda player: player['name'] == opTeam['wr'][1]['name'], players)[0]
	opTe = filter(lambda player: player['name'] == opTeam['te'][0]['name'], players)[0]
	opDefst = filter(lambda player: player['name'] == opTeam['defst'][0]['name'], players)[0]

	uTotal = uQb['pts']+uRb1['pts']+uRb2['pts']+uWr1['pts']+uWr2['pts']+uTe['pts']+uDefst['pts']
	opTotal = opQb['pts']+opRb1['pts']+opRb2['pts']+opWr1['pts']+opWr2['pts']+opTe['pts']+opDefst['pts']

	scores = {
		'uQb':uQb['name'],
		'uQbStatStr':uQb['statStr'],
		'uQbPts': str(uQb['pts']),
		'uRb1':uRb1['name'],
		'uRb1StatStr':uRb1['statStr'],
		'uRb1Pts':str(uRb1['pts']),
		'uRb2':uRb2['name'],
		'uRb2StatStr':uRb2['statStr'],
		'uRb2Pts':str(uRb2['pts']),
		'uWr1':uWr1['name'],
		'uWr1StatStr':uWr1['statStr'],
		'uWr1Pts':str(uWr1['pts']),
		'uWr2':uWr2['name'],
		'uWr2StatStr':uWr2['statStr'],
		'uWr2Pts':str(uWr2['pts']),
		'uTe':uTe['name'],
		'uTeStatStr':uTe['statStr'],
		'uTePts':str(uTe['pts']),
		'uDef':uDefst['name'],
		'uDefStatStr':uDefst['statStr'],
		'uDefPts':str(uDefst['pts']),
		'opQb':opQb['name'],
		'opQbStatStr':opQb['statStr'],
		'opQbPts': str(opQb['pts']),
		'opRb1':opRb1['name'],
		'opRb1StatStr':opRb1['statStr'],
		'opRb1Pts':str(opRb1['pts']),
		'opRb2':opRb2['name'],
		'opRb2StatStr':opRb2['statStr'],
		'opRb2Pts':str(opRb2['pts']),
		'opWr1':opWr1['name'],
		'opWr1StatStr':opWr1['statStr'],
		'opWr1Pts':str(opWr1['pts']),
		'opWr2':opWr2['name'],
		'opWr2StatStr':opWr2['statStr'],
		'opWr2Pts':str(opWr2['pts']),
		'opTe':opTe['name'],
		'opTeStatStr':opTe['statStr'],
		'opTePts':str(opTe['pts']),
		'opDef':opDefst['name'],
		'opDefStatStr':opDefst['statStr'],
		'opDefPts':str(opDefst['pts']),
		'uTotal':str(uTotal),
		'opTotal':str(opTotal)
		}
	return json.dumps(scores)