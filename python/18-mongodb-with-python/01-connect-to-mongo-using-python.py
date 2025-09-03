import pymongo
if __name__=="__main__":
    mongo_client=pymongo.MongoClient('mongodb://localhost:27017')
    print("mongo_client",mongo_client)
    school_database=mongo_client['school']
    student_collection=school_database['school']
    student_collection.insert_one({'name':'john','age':15})
    student_collection.insert_one({'name':'mr-wick','age':20})
    student_collection.insert_one({'name':'rahul','age':'12'})