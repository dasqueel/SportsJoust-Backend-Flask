#reset every usersname contest rankings and matchup data

from pymongo import MongoClient

#connect to mongo
client = MongoClient('localhost')
#connect to users database
db = client.smash
dbContests = client.Contests

contest = 'nfl1'
colNames = db.collection_names()
'''
#all data
for name in colNames:
	if name != 'system.indexes':
		db[name].update({'contest':contest},{'$set':{'defr':[],'qbr':[],'rbr':[],'wrr':[],'ter':[],
			'accepted':[],'potential':[],'rejected':[]}})


#reset contest pool
dbContests[contest].update({'contest':contest},{'$set':{'pool':[]}})



#remove all userContestDocs for a contest
for name in colNames:
	if name != 'system.indexes':
		if db[name].find_one({'contest':contest}):
			db[name].remove({'contest':contest})
'''
#reset all users matchup data for a contest
for name in colNames:
	if name != 'system.indexes':
		db[name].update({'contest':contest},{'$set':{'accepted':[],'potential':[],'rejected':[]}})

#remove all matches in a contest
contestCol = dbContests[contest]
contestDoc = dbContests[contest].find_one({'contest':contest})

#reset contest pool
#contestCol.update({'contest':contest},{'$set':{'pool':[]}})

#remove all matches in contest Collection
for matchDoc in contestCol.find():
	try:
		contestCol.remove({'matchId':matchDoc['matchId']})
	except Exception:
		pass