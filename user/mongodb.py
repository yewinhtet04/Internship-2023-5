import pymongo
class DB:
    def __init__(self):
        self.connection = pymongo.MongoClient("localhost", 27017)
        self.database = self.connection["my_db1"]
        self.collection = self.database["user_info"]

    def exist_user(self,mail):
        try:
            for d in self.collection.find({'email':mail}):
                return True
            return False
        except Exception as error:
            print(error)

    def insert_user(self,data:dict):
        count=0
        for i in self.collection.find():
            count=i['_id']
        data.update({'_id':count+1})
        self.collection.insert_one(data)
    def retrieve_user(self,email:str):
        try:
            for d in self.collection.find({'email':email}):
                return d
        except Exception as error:
            print(error)


'''
db=DB()
#db.insert_user({'email':'yewin04@gmail.com','name':'Ye','age':22})
print(db.exist_user('yewin04@gmail.com'))
'''