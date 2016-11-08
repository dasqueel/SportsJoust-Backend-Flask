from pymongo import MongoClient
from nflPlayers import *
from config import *

### make sure to set nflPlayers and ncaaPlayers before running this script ###

###create and insert contest doc
contest = 'nfl4'

contestDoc = {
	'contest':contest,
	'pool':[],
	'qbs':[],
	'rbs':[],
	'wrs':[],
	'tes':[],
	'defsts':[]
}

for qb in weeksqbs:
	contestDoc['qbs'].append(qb)
for rb in weeksrbs:
	contestDoc['rbs'].append(rb)
for wr in weekswrs:
	contestDoc['wrs'].append(wr)
for te in weekstes:
	contestDoc['tes'].append(te)
for dst in weeksdefsts:
	contestDoc['defsts'].append(dst)

#insert the new contest into contests
dbContests[contest].insert(contestDoc)

###create and insert stats doc

players = []

for player in weeksAll:
    players.append({'name':player['name'],'statStr':'','pts':0})

statDoc = {
    'contest':contest,
    'players':players
}

dbStats[contest].insert(statDoc)