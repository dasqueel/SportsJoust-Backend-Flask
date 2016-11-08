import requests
import pprint
from dateutil import parser
from players import *
from pymongo import MongoClient
from config import *

pp = pprint.PrettyPrinter(indent=4)

nflkey = 'sdhss2v7kxhj8vqefcnb2b73'
cfbkey = '5mubn7fjryjqs8uxa3ehw4y7'

schedUrl = 'http://api.sportradar.us/nfl-t1/2015/REG/1/schedule.json?api_key='+nflkey

r = requests.get(schedUrl)
res = r.json()
games = res['games']

#get times and opponents for each player
for game in games:
	for qb in qbs:
		if qb['team'] == str(game['home']):
			qb['opp'] = str(game['away'])
			qb['time'] = parser.parse(game['scheduled']).strftime("%A-%I")
		elif qb['team'] == str(game['away']):
			qb['opp'] = '@'+str(game['home'])
			qb['time'] = parser.parse(game['scheduled']).strftime("%A-%I")
		else:
			pass
	for rb in rbs:
		if rb['team'] == str(game['home']):
			rb['opp'] = str(game['away'])
			rb['time'] = parser.parse(game['scheduled']).strftime("%A-%I")
		elif rb['team'] == str(game['away']):
			rb['opp'] = '@'+str(game['home'])
			rb['time'] = parser.parse(game['scheduled']).strftime("%A-%I")
		else:
			pass
	for wr in wrs:
		if wr['team'] == str(game['home']):
			wr['opp'] = str(game['away'])
			wr['time'] = parser.parse(game['scheduled']).strftime("%A-%I")
		elif wr['team'] == str(game['away']):
			wr['opp'] = '@'+str(game['home'])
			wr['time'] = parser.parse(game['scheduled']).strftime("%A-%I")
		else:
			pass
	for te in tes:
		if te['team'] == str(game['home']):
			te['opp'] = str(game['away'])
			te['time'] = parser.parse(game['scheduled']).strftime("%A-%I")
		elif te['team'] == str(game['away']):
			te['opp'] = '@'+str(game['home'])
			te['time'] = parser.parse(game['scheduled']).strftime("%A-%I")
		else:
			pass
	for defst in defsts:
		if defst['team'] == str(game['home']):
			defst['opp'] = str(game['away'])
			defst['time'] = parser.parse(game['scheduled']).strftime("%A-%I")
		elif defst['team'] == str(game['away']):
			defst['opp'] = '@'+str(game['home'])
			defst['time'] = parser.parse(game['scheduled']).strftime("%A-%I")
		else:
			pass

nfl1 = {'contest':'nfl1','pool':[],'qbs':[],'rbs':[],'wrs':[],'tes':[],'defsts':[]}
#nfl1noon = {'contest':'nfl1noon','pool':[],'qbs':[],'rbs':[],'wrs':[],'tes':[],'defsts':[]}
#nfl1mid = {'contest':'nfl1mid','pool':[],'qbs':[],'rbs':[],'wrs':[],'tes':[],'defsts':[]}
#nfl1night = {'contest':'nflnight','pool':[],'qbs':[],'rbs':[],'wrs':[],'tes':[],'defsts':[]}

#get each contests players
for qb in qbs:
	#set nfl1all
	nfl1['qbs'].append({'name':qb['name'],'opp':qb['opp']})

for rb in rbs:
#set nfl1all
	nfl1['rbs'].append({'name':rb['name'],'opp':rb['opp']})

for wr in wrs:
#set nfl1all
	nfl1['wrs'].append({'name':wr['name'],'opp':wr['opp']})

for te in tes:
	#set nfl1all
	nfl1['tes'].append({'name':te['name'],'opp':te['opp']})

for defst in defsts:
	#set nfl1all
	nfl1['defsts'].append({'name':defst['name'],'opp':defst['opp']})

#pp.pprint(nfl1)

dbContests['nfl1'].insert(nfl1)
'''
for game in games:
	#pp.pprint(game)
	date = parser.parse(game['scheduled'])
	start = date.strftime("%A-%I")
	print game['home'], game['away']

def playerPool():
	#loop thru games and update each player from there
	for game in games:
		for qb in qbs:
			if qb['team'] == game['home']:
				qb['opp'] == game['away']
				qb['time'] = parser.parse(game['scheduled']).strftime("%A-%I")
			elif qb['team'] == game['away']:
				qb['opp'] == game['home']
				qb['time'] = parser.parse(game['scheduled']).strftime("%A-%I")
			else:
				pass
		return qbs
'''