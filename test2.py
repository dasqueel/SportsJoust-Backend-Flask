import requests
import collections

r = requests.get('http://api.espn.com/v1/sports/baseball/mlb/athletes?groups=1')

r.status_code

ter = ['Rob Gronkowski', 'Jimmy Graham', 'Julius Thomas', 'Mychal Rivera', 'Dwayne Allen', 'Travis Kelce', 'Greg Olsen', 'Vernon Davis', 'Coby Fleener', 'Martellus Bennett', 'Eric Ebron', 'Dennis Pitta', 'Austin Seferian-Jenkins', 'Kyle Rudolph', 'Maxx Williams']

