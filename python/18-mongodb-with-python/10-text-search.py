import pymongo

def text_search():
    mongo_client = pymongo.MongoClient("mongodb://localhost:27017")
    database = mongo_client['library']
    collection = database['books']
    # Create a text index on the 'title' field (change if needed)
    collection.create_index([("title", "text")])
    text_search_output = collection.find({
        "$text": {"$search": "War"}
    })
    for item in text_search_output:
        print(item)

text_search()