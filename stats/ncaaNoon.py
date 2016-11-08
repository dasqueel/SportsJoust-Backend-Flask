from pymongo import MongoClient
import requests
import time

#connect to mongo
client = MongoClient('localhost')
dbStats = client.Stats

#return statStr and pts
def getNcaaStats(player,playerTeam,gameId):
	r = requests.get("http://espn.go.com/ncf/boxscore?gameId="+gameId)
	html = r.text
	soup = BeautifulSoup(html, 'html.parser')
	statStr = ''
	pts = 0

	#the game hasnt started, return the empty statStr and 0.0 pts
	if 'No Boxscore Available' in str(soup):
		return str(statStr),pts
	#the game is in session or completed
	else:
		#passing statas
		for table in soup.find_all('table', {'class':'mod-data'}):
			if playerTeam+' Passing' in str(table):
				#get players passing stats, if available
				if player in str(table):
					for tr in table.find_all('tr'):
					    tds = tr.find_all('td')
					    if len(tds) == 7:
					    	if tds[0].text == player:
						    	row = []
						    	i = 0
						    	while (i<5):
						    		if i == 2:
						    			#row.append(tds[i].text)
						    			if tds[i].text != '0':
						    				#add rush yds to statStr
						    				statStr = statStr+str(tds[i].text)+'pYds '

						    				#summation of points
						    				pts = pts+float(tds[i].text)*0.04
						    			else:
						    				pass
						    		if i == 4:
						    			if tds[i].text != '0':
							    			#add rush touchdowns
							    			statStr = statStr+str(tds[i].text)+'pTds '
							    			pts = pts+float(tds[i].text)*4.0
							    		else:
							    			pass
						    		i += 1

		#rushing stats
		for table in soup.find_all('table', {'class':'mod-data'}):
			if playerTeam+' Rushing' in str(table):
				#get players rushing stats, if available
				if player in str(table):
					for tr in table.find_all('tr'):
					    tds = tr.find_all('td')
					    if len(tds) == 6:
					    	if tds[0].text == player:
						    	row = []
						    	i = 0
						    	while (i<5):
						    		if i == 2:
						    			#row.append(tds[i].text)
						    			if tds[i].text != '0':
						    				#add rush yds
						    				statStr = statStr+str(tds[i].text)+'ruYds '
						    				pts = pts+float(tds[i].text)*0.1
						    			else:
						    				pass
						    		if i == 4:
						    			if tds[i].text != '0':
							    			#add rush touchdowns
							    			statStr = statStr+str(tds[i].text)+'ruTds '
							    			pts = pts+float(tds[i].text)*6.0
							    		else:
							    			pass
						    		i += 1
		#receiving statas
		for table in soup.find_all('table', {'class':'mod-data'}):
			if playerTeam+' Receiving' in str(table):
				#get players rushing stats, if available
				if player in str(table):
					for tr in table.find_all('tr'):
					    tds = tr.find_all('td')
					    if len(tds) == 6:
					    	if tds[0].text == player:
						    	row = []
						    	i = 0
						    	while (i<5):
						    		if i == 2:
						    			#row.append(tds[i].text)
						    			if tds[i].text != '0':
						    				#add rush yds
						    				statStr = statStr+str(tds[i].text)+'reYds '
						    				pts = pts+float(tds[i].text)*0.1
						    			else:
						    				pass
						    		if i == 4:
						    			if tds[i].text != '0':
							    			#add rush touchdowns
							    			statStr = statStr+str(tds[i].text)+'reTds'
							    			pts = pts+float(tds[i].text)*6.0
							    		else:
							    			pass
						    		i += 1
		pts = "{0:.2f}".format(pts)
		return statStr, pts

#between noon game time slot, query espn every 10 seconds

contest = 'ncaa1'

#get all noon games
#newGames.py produces the games syntax
games = [{'id':'','players':[{'name':'','team':''}]}]

#loop through all games and update relevant players stats to the contestStatDoc
for game in games:
	r = requests.get("http://espn.go.com/ncaa-football/boxscore?gameId="+game['id'])
	html = r.text
	soup = BeautifulSoup(html, 'html.parser')

	for player in game['players']:
		#get players stats
		playerStats, playerPts = getNcaaStats(player['name'],player['team'],game['id'])
		#update data in mongo stats collection
		dbStats[contest].update({'players.name':player['name']}, {'$set': {'players.$.statStr':playerStats,'players.$.pts':playerPts}})
