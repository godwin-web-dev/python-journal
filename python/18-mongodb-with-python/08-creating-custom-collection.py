import pymongo
def create_collection():
    mongo_client=pymongo.MongoClient("mongodb://localhost:27017")
    database=mongo_client['library']
    collection=database['books']
    collection1=create_collection()
    print("collection object isas follow ",collection)
    output=collection.find()
    for i in output:
        print(i)
    print(output)
create_collection()