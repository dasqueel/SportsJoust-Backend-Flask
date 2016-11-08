#!/usr/bin/env python

from bs4 import BeautifulSoup
from pymongo import MongoClient
import requests
import time

#connect to mongo
client = MongoClient('localhost')
dbStats = client.Stats

#if box score or player isnt up yet -- set all stats to a blank string
def getDefStats(player,htmlText):

	soup = BeautifulSoup(htmlText, 'html.parser')
	statStr = ''
	pts = 0
	field = None

	#the game hasnt started, return the empty statStr and 0.0 pts
	if 'No Boxscore Available' in str(soup):
		return str(statStr),pts
	#the game is in session or completed
	else:
		#determine if team is away or home
		away = soup.find_all('span',{'class':'long-name'})[0].text
		home = soup.find_all('span',{'class':'long-name'})[1].text

		#add a break point to end it when finding the table ??? or find the position of the table fo all tables
		for table in soup.find_all('table',{'class':'mod-data'}):
			#find the matchup table
			if 'Matchup' in str(table):
				#determine the defenses points allowed for the statStr and pts
				table = soup.find('table', {'class':'mod-data'})
				trs = table.find_all('tr')
				awayTds = trs[1].find_all('td')
				homeTds = trs[2].find_all('td')
				away = soup.find_all('span',{'class':'long-name'})[0].text

				if player == away:
					field = 'away'
					#ptsAlwStr = homeTds[5].text
					#ptsAlw = float(ptsAlwStr)
					ptsAlwStr = soup.find('div',{'class':'score icon-font-before'}).text.strip()
					ptsAlw = float(ptsAlwStr)
					statStr = statStr+ptsAlwStr+' allowed '
					if ptsAlw == 0.0:
						pts = pts + 10.0
					elif 1.0 <= ptsAlw <= 6.0:
						pts = pts + 7.0
					elif 7.0 <= ptsAlw <= 13.0:
						pts = pts + 4.0
					elif 14.0 <= ptsAlw <= 20.0:
						pts = pts + 1.0
					elif 21.0 <= ptsAlw <= 27.0:
						pts = pts + 0.0
					elif 28.0 <= ptsAlw <= 34.0:
						pts = pts - 1.0
					elif 35.0 <= ptsAlw:
						pts = pts - 4.0

					#get defs sacks
					sackTds = trs[14].find_all('td')
					sacks = sackTds[2].text.strip().split('-')[0]
					if sacks != '0':
						statStr = statStr + sacks +' sack '
						pts = pts + float(sacks)
					#get defs fmbls
					fmblTds = trs[21].find_all('td')
					fmbls = fmblTds[2].text.strip()
					if fmbls != '0':
						statStr = statStr + fmbls +' fmbl '
						pts = pts + 2.0*float(fmbls)
					#get defs ints
					intTds = trs[22].find_all('td')
					ints = intTds[2].text.strip()
					if ints != '0':
						statStr = statStr + ints +' int '
						pts = pts + 2.0*float(ints)
					#get defs spectial team and defensive touchdowns
					tdTds = trs[23].find_all('td')
					tds = tdTds[1].text.strip()
					if tds != '0':
						statStr = statStr + tds +' tds'
						pts = pts + 6.0*float(tds)
				else:
					field = 'home'
					#ptsAlwStr = awayTds[5].text
					#ptsAlw = float(ptsAlwStr)
					ptsAlwStr = soup.find('div',{'class':'score icon-font-after'}).text.strip()
					ptsAlw = float(ptsAlwStr)
					statStr = statStr+ptsAlwStr+' allowed '
					if ptsAlw == 0.0:
						pts = pts + 10.0
					elif 1.0 <= ptsAlw <= 6.0:
						pts = pts + 7.0
					elif 7.0 <= ptsAlw <= 13.0:
						pts = pts + 4.0
					elif 14.0 <= ptsAlw <= 20.0:
						pts = pts + 1.0
					elif 21.0 <= ptsAlw <= 27.0:
						pts = pts + 0.0
					elif 28.0 <= ptsAlw <= 34.0:
						pts = pts - 1.0
					elif 35.0 <= ptsAlw:
						pts = pts - 4.0

					#get defs sacks
					sackTds = trs[14].find_all('td')
					sacks = sackTds[1].text.strip().split('-')[0]
					if sacks != '0':
						statStr = statStr + sacks +' sack '
						pts = pts + float(sacks)
					#get defs fmbls
					fmblTds = trs[21].find_all('td')
					fmbls = fmblTds[1].text.strip()
					if fmbls != '0':
						statStr = statStr + fmbls +' fmbl '
						pts = pts + 2.0*float(fmbls)
					#get defs ints
					intTds = trs[22].find_all('td')
					ints = intTds[1].text.strip()
					if ints != '0':
						statStr = statStr + ints +' int '
						pts = pts + 2.0*float(ints)
					#get defs spectial team and defensive touchdowns
					tdTds = trs[23].find_all('td')
					tds = tdTds[2].text.strip()
					if tds != '0':
						statStr = statStr + tds +' tds'
						pts = pts + 6.0*float(tds)

				return statStr, pts

#return statStr and pts
def getNflStats(player,playerTeam,htmlText):

	soup = BeautifulSoup(htmlText, 'html.parser')
	statStr = ''
	pts = 0

	#the game hasnt started, return the empty statStr and 0.0 pts
	if 'No Boxscore Available' in str(soup):
		return str(statStr),pts
	#the game is in session or completed
	else:
		#passing stats
		for table in soup.find_all('table', {'class':'mod-data'}):
			if playerTeam+' Passing' in str(table):
				#get players passing stats, if available
				if player in str(table):
					for tr in table.find_all('tr'):
					    tds = tr.find_all('td')
					    #print len(tds)
					    if len(tds) == 9:
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
					    if len(tds) == 7:
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
		return statStr, float(pts)

#between noon game time slot, query espn every 10 seconds

contest = 'nfl4'

#get all noon game players
games = [{'players': [{'name': 'Andrew Luck', 'team': 'Indianapolis'}, {'name': 'Blake Bortles', 'team': 'Jacksonville'}, {'name': 'Frank Gore', 'team': 'Indianapolis'}, {'name': 'T.J. Yeldon', 'team': 'Jacksonville'}, {'name': 'Allen Robinson', 'team': 'Jacksonville'}, {'name': 'Andre Johnson', 'team': 'Indianapolis'}, {'name': 'Julius Thomas', 'team': 'Jacksonville'}, {'name': 'Dwayne Allen', 'team': 'Indianapolis'}, {'name': 'Coby Fleener', 'team': 'Indianapolis'}, {'name': 'Indianapolis'}, {'name': 'Jacksonville'}], 'id': '400791671'}, {'players': [{'name': 'Eli Manning', 'team': 'New York'}, {'name': 'Tyrod Taylor', 'team': 'Buffalo'}, {'name': 'LeSean McCoy', 'team': 'Buffalo'}, {'name': 'Rashad Jennings', 'team': 'New York'}, {'name': 'Odell Beckham Jr.', 'team': 'New York'}, {'name': 'Sammy Watkins', 'team': 'Buffalo'}, {'name': 'Larry Donnell', 'team': 'New York'}, {'name': 'Buffalo'}, {'name': 'New York Giants'}], 'id': '400791678'}, {'players': [{'name': 'Cam Newton', 'team': 'Carolina'}, {'name': 'Jameis Winston', 'team': 'Tampa Bay'}, {'name': 'Jonathan Stewart', 'team': 'Carolina'}, {'name': 'Mike Evans', 'team': 'Tampa Bay'}, {'name': 'Vincent Jackson', 'team': 'Tampa Bay'}, {'name': 'Greg Olsen', 'team': 'Carolina'}, {'name': 'Austin Seferian-Jenkins', 'team': 'Tampa Bay'}, {'name': 'Carolina'}, {'name': 'Tampa Bay'}], 'id': '400791701'}, {'players': [{'name': 'Sam Bradford', 'team': 'Philadelphia'}, {'name': 'DeMarco Murray', 'team': 'Philadelphia'}, {'name': 'Alfred Morris', 'team': 'Washington'}, {'name': 'Jordan Matthews', 'team': 'Philadelphia'}, {'name': 'Pierre Garcon', 'team': 'Washington'}, {'name': 'Zach Ertz', 'team': 'Philadelphia'}, {'name': 'Philadelphia'}, {'name': 'Washington'}], 'id': '400791704'}, {'players': [{'name': 'Jay Cutler', 'team': 'Chicago'}, {'name': 'Derek Carr', 'team': 'Oakland'}, {'name': 'Matt Forte', 'team': 'Chicago'}, {'name': 'Latavius Murray', 'team': 'Oakland'}, {'name': 'Alshon Jeffery', 'team': 'Chicago'}, {'name': 'Amari Cooper', 'team': 'Oakland'}, {'name': 'Martellus Bennett', 'team': 'Chicago'}, {'name': 'Mychal Rivera', 'team': 'Oakland'}, {'name': 'Oakland'}, {'name': 'Chicago'}], 'id': '400791706'}, {'players': [{'name': 'Matt Ryan', 'team': 'Atlanta'}, {'name': 'Alred Blue', 'team': 'Houston'}, {'name': 'Julio Jones', 'team': 'Atlanta'}, {'name': 'DeAndre Hopkins', 'team': 'Houston'}, {'name': 'Houston'}, {'name': 'Atlanta'}], 'id': '400791709'}, {'players': [{'name': 'Andy Dalton', 'team': 'Cincinnati'}, {'name': 'Jamaal Charles', 'team': 'Kansas City'}, {'name': 'Jeremy Hill', 'team': 'Cincinnati'}, {'name': 'Giovani Bernard', 'team': 'Cincinnati'}, {'name': 'A.J. Green', 'team': 'Cincinnati'}, {'name': 'Jeremy Maclin', 'team': 'Kansas City'}, {'name': 'Tyler Eifert', 'team': 'Cincinnati'}, {'name': 'Travis Kelce', 'team': 'Kansas City'}, {'name': 'Kansas City'}, {'name': 'Cincinnati'}], 'id': '400791712'}]
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
	'Dallas',
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
	'Kansas City',
	'New York Jets',
	'New York Giants'
]

#loop through all games and update relevant players stats to the contestStatDoc
for game in games:
	r = requests.get("http://espn.go.com/nfl/boxscore?gameId="+game['id'])
	html = r.text

	rMatch = requests.get("http://espn.go.com/nfl/matchup?gameId="+game['id'])
	htmlMatch = rMatch.text

	for player in game['players']:
		#get players stats
		#check to see if its a defesnive player # what about jets and giants??
		if player['name'] in teams:
			playerStats, playerPts = getDefStats(player['name'],htmlMatch)
			#update data in mongo stats collection
			try:
				dbStats[contest].update({'players.name':player['name']}, {'$set': {'players.$.statStr':playerStats,'players.$.pts':playerPts}})
			except:
				print 'insert error'
		#else insert a non-Def players stats and points
		else:
			playerStats, playerPts = getNflStats(player['name'],player['team'],html)
			#update data in mongo stats collection
			try:
				dbStats[contest].update({'players.name':player['name']}, {'$set': {'players.$.statStr':playerStats,'players.$.pts':playerPts}})
			except:
				print 'def insert error'
