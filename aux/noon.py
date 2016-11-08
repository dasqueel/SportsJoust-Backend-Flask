from config import *
from pymongo import MongoClient
import requests
import time
from funcs import *

#between noon game time slot, query espn every 10 seconds

contest = 'nfl1'

#get all noon games
games = [{'players': [{'name': 'Tom Brady', 'team': 'New England'}, {'name': 'Cam Newton', 'team': 'Carolina'}, {'name': 'Julian Edelman', 'team': 'New England'}, {'name': 'Rob Gronkowski', 'team': 'New England'}, {'name': 'Greg Olsen', 'team': 'Carolina'}, {'name': 'New England'}], 'id': '400791739'}, {'players': [{'name': 'Matthew Stafford', 'team': 'Detroit'}, {'name': 'Joique Bell', 'team': 'Detroit'}, {'name': 'Calvin Johnson', 'team': 'Detroit'}, {'name': 'Golden Tate', 'team': 'Detroit'}, {'name': 'Julius Thomas', 'team': 'Jacksonville'}, {'name': 'Eric Ebron', 'team': 'Detroit'}], 'id': '400790307'}, {'players': [{'name': 'Jamaal Charles', 'team': 'Kansas City'}, {'name': 'Bishop Sankey', 'team': 'Tennessee'}, {'name': 'Jeremy Maclin', 'team': 'Kansas City'}, {'name': 'Travis Kelce', 'team': 'Kansas City'}], 'id': '400791788'}]

##### if the jets play the giants, test it out to make sure it works!
teams = [
	'Minnesota',
	'Green Bay',
	'Chicago',
	'Detroit',
	'Tampa Bay',
	'Carolina',
	'Atlanta',
	'New Orleans',
	'New York',
	'Philadelphia',
	'Dallas'
	'Washington',
	'San Francisco',
	'Seattle',
	'St. Louis',
	'Arizona',
	'Pittsburgh',
	'Cincinnati',
	'Cleveland',
	'Baltimore',
	'New England',
	'Miami',
	'Buffalo',
	'Indianapolis',
	'Houston',
	'Tennessee',
	'Jacksonville',
	'Denver',
	'Oakland',
	'San Diego',
	'Kansas City'
]


#loop through all games and update relevant players stats to the contestStatDoc
for game in games:
	r = requests.get("http://espn.go.com/nfl/boxscore?gameId="+game['id'])
	html = r.text
	soup = BeautifulSoup(html, 'html.parser')

	for player in game['players']:
		#get players stats
		#check to see if its a defesnive player # what about jets and giants??
		if player['name'] in teams:
			playerStats, playerPts = getDefStats(player,game['id'])
			#update data in mongo stats collection
			#dbStats[contest].update({'contest':contest},{'$set':{'players.'+player['name']:''}})
			dbStats['nfl1'].update({'players.name':player['name']}, {'$set': {'players.$.statStr':playerStats,'players.$.pts':playerPts}})
		#else insert a non-Def players stats and points
		else:
			playerStats, playerPts = getNflStats(player['name'],player['team'],game['id'])
			#update data in mongo stats collection
			dbStats['nfl1'].update({'players.name':player['name']}, {'$set': {'players.$.statStr':playerStats,'players.$.pts':playerPts}})
