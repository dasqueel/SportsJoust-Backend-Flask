from pymongo import MongoClient

#connect to mongo
client = MongoClient('localhost')
#connect to users database
db = client.smash
dbContests = client.Contests
dbStats = client.Stats