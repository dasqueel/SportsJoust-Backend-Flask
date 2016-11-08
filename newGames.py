from nflPlayers import *

games = [
	{'id':'400791739','players':[]},
	{'id':'400790307','players':[]},
	{'id':'400791788','players':[]}
]

ids = []

for game in games:
	ids.append(game['id'])


for game in games:
	for qb in weeksqbs:
		if qb['gameId'] == game['id']:
			game['players'].append({'name':qb['name'],'team':qb['team']})
	for rb in weeksrbs:
		if rb['gameId'] == game['id']:
			game['players'].append({'name':rb['name'],'team':rb['team']})
	for wr in weekswrs:
		if wr['gameId'] == game['id']:
			game['players'].append({'name':wr['name'],'team':wr['team']})
	for te in weekstes:
		if te['gameId'] == game['id']:
			game['players'].append({'name':te['name'],'team':te['team']})
	for defst in weeksdefsts:
		if defst['gameId'] == game['id']:
			game['players'].append({'name':defst['name']})

print games