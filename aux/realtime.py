import config
from pymongo import MongoClient
import requests
from datetime import *
import time
from boxscore import *

#between noon game time slot, query espn every 10 seconds

contest = 'nfl1'

#get all noon games
games = [
	{'id':'230945','players':[{'name':'','team',''}]}
]

#loop through all games and update relevant players stats to the contestStatDoc
for game in games:
	r = requests.get("http://espn.go.com/nfl/boxscore?gameId="+game['id'])
	html = r.text
	soup = BeautifulSoup(html, 'html.parser')

	for player in games['players']
		#get players stats
		#check to see if its a defesnive player # what about jets and giants??
		if len(play) <= 4:
			playerStats, playerPts = getDefStats(player,game['id'])
			#update data in mongo stats collection
			#dbStats[contest].update({'contest':contest},{'$set':{'players.'+player['name']:''}})
			dbStats['nfl1'].update({'players.name':player['name']}, {'$set': {'players.$.statStr':playerStats,'players.$.pts':playerPts}})
		else:
			getNflStats(player['name'],player['team'],game['id'])
			#update data in mongo stats collection
			dbStats['nfl1'].update({'players.name':player['name'],'players.team':player['team8']}, {'$set': {'players.$.statStr':playerStats,'players.$.pts':playerPts}})

'''
#date_object = datetime.strptime(june, '%b %d %Y %I:%M%p')
gameStart = datetime.strptime(datetime(2015, 8, 29, 10, 0,0).ctime(), "%a %b %d %H:%M:%S %Y")
gameEnd = datetime.strptime(datetime(2015,8,29,10,7,10).ctime(), "%a %b %d %H:%M:%S %Y")
now = datetime.strptime(time.ctime(), "%a %b %d %H:%M:%S %Y")

#if the query is made during the game
if gameStart < now < gameEnd:
	#print 'yes'
else:
	print 'no'
'''