import requests
from bs4 import BeautifulSoup

r = requests.get("http://espn.go.com/nfl/matchup?gameId=400791678")
html = r.text
#print type(html)
def getDefStats(player,htmlText):

	htmlUni = unicode(htmlText)
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

#playerStats, playerPts = getDefStats('Green Bay',html)
#print playerStats, playerPts

#print getDefStats('MIN','400791148')

#return statStr and pts

def getNflStats(player,playerTeam,gameId):
	r = requests.get("http://espn.go.com/nfl/boxscore?gameId="+gameId)
	html = r.text
	soup = BeautifulSoup(html, 'html.parser')
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
					print 'new york can pass'
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
		return statStr, pts

playerStats, playerPts = getNflStats('Odell Beckham Jr.','New York','400791678')
print playerStats, playerPts

#return statStr and pts
def getNcaaStats(player,playerTeam,gameId):
	'''
	r = requests.get("http://espn.go.com/ncf/boxscore?gameId="+gameId)
	html = r.text
	'''
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

#print getNcaaStats('Jeff Jones','Minnesota','400763398')

#####
'''
#if box score or player isnt up yet -- set all stats to a blank string
def getDefStats(player,gameId):

	r = requests.get("http://espn.go.com/nfl/matchup?gameId="+gameId)
	html = r.text
	soup = BeautifulSoup(html, 'html.parser')
	statStr = ''
	pts = 0
	field = None
	#the game hasnt started, return the empty statStr and 0.0 pts
	if 'No Boxscore Available' in str(soup):
		return str(statStr),pts
	#the game is in session or completed
	else:
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
				ptsAlwStr = homeTds[5].text
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
			else:
				field = 'home'
				ptsAlwStr = awayTds[5].text
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

			for table in soup.find_all('table', {'class':'mod-data'}):
				if '1st Downs' in str(table):
					trs = table.find_all('tr')

					if field == 'away':

						#get defs sacks
						sackTds = trs[15].find_all('td')
						sacks = sackTds[2].text[0]
						if sacks != '0':
							statStr = statStr + sacks +' sack '
							pts = pts + float(sacks)
						#get defs fmbls
						fmblTds = trs[22].find_all('td')
						fmbls = fmblTds[2].text
						if fmbls != '0':
							statStr = statStr + fmbls +' fmbl '
							pts = pts + 2.0*float(fmbls)
						#get defs ints
						intTds = trs[23].find_all('td')
						ints = intTds[2].text
						if ints != '0':
							statStr = statStr + ints +' int '
							pts = pts + 2.0*float(ints)
						#get defs spectial team and defensive touchdowns
						tdTds = trs[24].find_all('td')
						tds = tdTds[1].text
						if tds != '0':
							statStr = statStr + tds +' tds'
							pts = pts + 6.0*float(tds)
					else:

						#get defs sacks
						sackTds = trs[15].find_all('td')
						sacks = sackTds[1].text[0]
						if sacks != '0':
							statStr = statStr + sacks +' sack '
							pts = pts + float(sacks)
						#get defs fmbls
						fmblTds = trs[22].find_all('td')
						fmbls = fmblTds[1].text
						if fmbls != '0':
							statStr = statStr + fmbls +' fmbl '
							pts = pts + 2.0*float(fmbls)
						#get defs ints
						intTds = trs[23].find_all('td')
						ints = intTds[1].text
						if ints != '0':
							statStr = statStr + ints +' int '
							pts = pts + 2.0*float(ints)
						#get defs spectial team and defensive touchdowns
						tdTds = trs[24].find_all('td')
						tds = tdTds[2].text
						if tds != '0':
							statStr = statStr + tds +' tds'
							pts = pts + 6.0*float(tds)
			return str(statStr), pts
'''