import pymongo
class DB:
    def __init__(self):
        self.connection = pymongo.MongoClient("localhost", 27017)
        self.database = self.connection["my_db1"]
        self.collection = self.database["movie_info"]

'''
img=open('bp.png','r')
movie={'name':'My Name','img':img}
db=DB()
db.collection.insert_one(movie)
'''