import pymongo
def find_document():
    mongo_client = pymongo.MongoClient('mongodb://localhost:27017')
    database = mongo_client['organisation']
    collection = database['employee']
    result = collection.find_one({
        "salary": {"$gte": 50000}
    })
    print("result is ", result)
    salary_less_than_30000 = collection.find({
        "salary": {"$lte": 30000}
    })
    print("salary less than 30000:")
    for doc in salary_less_than_30000:
        print(doc)
find_document()