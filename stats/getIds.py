from bs4 import BeautifulSoup
import requests

gameIdDict = {
    'Minnesota':'',
    'Green Bay':'',
    'Detroit':'',
    'Chicago':'',
    'Tampa Bay':'',
    'Carolina':'',
    'Atlanta':'',
    'New Orleans':'',
    'New York Giants':'',
    'Dallas':'',
    'Philadelphia':'',
    'Washington':'',
    'St. Louis':'',
    'San Francisco':'',
    'Seattle':'',
    'Arizona':'',
    'Denver':'',
    'Kansas City':'',
    'San Diego':'',
    'Oakland':'',
    'Baltimore':'',
    'Pittsburgh':'',
    'Cincinnati':'',
    'Cleveland':'',
    'New England':'',
    'Miami':'',
    'Buffalo':'',
    'New York Jets':'',
    'Indianapolis':'',
    'Houston':'',
    'Tennessee':'',
    'Jacksonville':''
}


r = requests.get("http://espn.go.com/nfl/schedule/_/week/4")
html = r.text

soup = BeautifulSoup(html, 'html.parser')
anchors = soup.find_all('a')

tables = soup.find_all('table')


for k,v in gameIdDict.iteritems():
	for table in tables:
		trs = table.find_all('tr')
		for tr in trs:
			if k in str(tr):
				for a in tr.find_all('a', href=True):
					if 'gameId' in a['href']:
						gameIdStr = a['href']
						gameIdPos = a['href'].find('gameId=')
						gameId = gameIdStr[gameIdPos+7:]
						gameId = gameId[:9]
						gameIdDict[k] = gameId

print gameIdDict
'''
for a in soup.find_all('a', href=True):
	if 'gameId' in a['href']:
		print a['href']
'''