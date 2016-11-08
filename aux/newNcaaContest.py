from pymongo import MongoClient
from ncaaPlayers import *
from config import *

### make sure to set nflPlayers and ncaaPlayers before running this script ###

###create and insert contest doc
contest = ''

contestDoc = {
	'contest':contest,
	'pool':[],
	'qbs':[],
	'rbs':[],
	'wrs':[],
	'tes':[]
}

for qb in weeksqbs:
	doc['qbs'].append(qb)
for rb in weeksrbs:
	doc['rbs'].append(rb)
for wr in weekswrs:
	doc['wrs'].append(wr)
for te in weekstes:
	doc['tes'].append(te)

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