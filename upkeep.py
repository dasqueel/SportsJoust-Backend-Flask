from config import *

qbs = [
	'Aaron Rodgers',
	'Andrew Luck',
	'Drew Brees',
	'Peyton Manning',
	'Russell Wilson',
	'Matthew Stafford',
	'Tom Brady',
	'Cam Newton',
	'Tony Romo',
	'Ben Roethlisberger',
	'Matt Ryan',
	'Derek Carr',
	'Phillip Rivers',
	'Johnny Manziel',
	'Jay Cutler',
	'Andy Dalton',
	'Nick Foles',
	'Sam Bradford',
	'Teddy Bridgewater',
	'Ryan Tannehill',
	'Carson Palmer',
	'E.J. Manuel',
	'Jameis Winston'
]

rbs = [
	'Adrian Peterson',
	'LeSean McCoy',
	'Eddie Lacy',
	'LeVeon Bell',
	'DeMarco Murray',
	'Matt Forte',
	'Jamaal Charles',
	'Marshawn Lynch',
	'Arian Foster',
	'Tre Mason',
	'Mark Ingram',
	'Justin Forsett',
	'C.J. Anderson',
	'Joique Bell',
	'Carlos Hyde',
	'Lamar Miller',
	'Andre Ellington',
	'Jeremy Hill',
	'Alfred Morris',
	'Latavius Murray',
	'Isaiah Crowell',
	'Rashad Jennings',
	'Branden Oliver',
	'Giovani Bernard',
	'Fred Jackson',
	'Bishop Sankey'
]

wrs = [
	'Calvin Johnson',
	'Odell Beckham',
	'Alshon Jeffery',
	'Antonio Brown',
	'Demaryius Thomas',
	'Jordy Nelson',
	'Julio Jones',
	'A.J. Green',
	'T.Y. Hilton',
	'Jeremy Maclin',
	'Randall Cobb',
	'Emmanuel Sanders',
	'Mike Evans',
	'Kelvin Benjamin',
	'DeAndre Hopkins',
	'Brandon Marshall',
	'Jordan Matthews',
	'Sammy Watkins',
	'Golden Tate',
	'Julian Edelman',
	'Keenan Allen',
	'Vincent Jackson',
	'Kenny Stills',
	'Mike Wallace',
	'Davante Adams',
	'Martavis Bryant',
	'Brandin Cooks',
	'Jarvis Landry'
]

tes = [
	'Rob Gronkowski',
	'Jimmy Graham',
	'Julius Thomas',
	'Mychal Rivera',
	'Dwayne Allen',
	'Travis Kelce',
	'Greg Olsen',
	'Vernon Davis',
	'Coby Fleener',
	'Martellus Bennett',
	'Eric Ebron',
	'Dennis Pitta',
	'Austin Seferian-Jenkins',
	'Kyle Rudolph',
	'Maxx Williams'
]

defs = [
	'SEA',
	'STL',
	'HOU',
	'PHI',
	'MN',
	'GB',
	'NE',
	'NYJ',
	'BAL',
	'ARI'
]
def update(contest):
	#contestDoc = dbContests[contest].find_one({'contest':contest})
	dbContests[contest].update({'contest':contest}, {'$set':{
		'qb': qbs,
		'rb': rbs,
		'wr': wrs,
		'te': tes,
		'def': defs,
		}})

def createContest(contest):
	#create contest collection
	doc = {
		'contest':contest,
		'pool':[],
		'qb':[],
		'rb':[],
		'wr':[],
		'te':[],
		'def':[],
		'type':'admin'
	}