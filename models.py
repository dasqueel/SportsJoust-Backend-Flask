from pymongo import MongoClient
from bson.objectid import ObjectId

class User():

    def __init__(self, username, balance, id):
        self.username = username
        self.balance = balance
        self.id = id

    def display(self):
      print user.username, user.balance

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return unicode(self.id)

    @staticmethod
    def get(userid):
        col = User._get_col()
        return col.find_one({'_id':userid})

    @staticmethod
    def _get_col():
        client = MongoClient()
        db = client['smash']
        col = db['dasqueel']
        return col

'''
class User():
    client = MongoClient()
    db = client['smash']
    col = db['dasqueel']
    user_id = None

    def __init__(self, dic):
        self.dic = dic

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def is_active(self):
        return True

    def get_id(self):
        return unicode(str(self.user_id))

    def save(self):
        self.user_id = self.col.insert(self.dic)
        print "Debug:" + str(self.user_id)


    @staticmethod
    def _get_col():
        client = MongoClient()
        db = client['test']
        col = db['user']
        return col

    @staticmethod
    def get(userid):
        col = User._get_col()
        return col.find_one({'_id':userid})

user = User()
'''