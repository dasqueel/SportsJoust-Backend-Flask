from config import *

contest = 'nfl1'
gameId = '400791485'
#loop thru default contest and remove players with a certain gameId
contestDoc = dbContests[contest].find_one({'contest':contest})
qbs = contestDoc['qbs']
rbs = contestDoc['rbs']
wrs = contestDoc['wrs']
tes = contestDoc['tes']
defsts = contestDoc['defsts']

for qb in qbs:
	if qb['gameId'] == gameId:
		qbs.remove(qb)
dbContests[contest].update({'contest':contest},{'$set':{'qbs':qbs}})

for rb in rbs:
	if rb['gameId'] == gameId:
		rbs.remove(rb)
dbContests[contest].update({'contest':contest},{'$set':{'rbs':rbs}})

for wr in wrs:
	if wr['gameId'] == gameId:
		wrs.remove(wr)
dbContests[contest].update({'contest':contest},{'$set':{'wrs':wrs}})

for te in tes:
	if te['gameId'] == gameId:
		tes.remove(te)
dbContests[contest].update({'contest':contest},{'$set':{'tes':tes}})

for defst in defsts:
	if defst['gameId'] == gameId:
		defsts.remove(defst)
dbContests[contest].update({'contest':contest},{'$set':{'defsts':defsts}})