import pymongo
def delete_document():
    mongo_client = pymongo.MongoClient('mongodb://localhost:27017')
    database = mongo_client['organisation']
    collection = database['employee']

    # delete a document from the collection
    collection.delete_one({'name': 'Alia'})

    # delete documents from the collection using delete_many
    deleted_count = collection.delete_many({'name': 'Alice'}).deleted_count
    print("Number of documents deleted:", deleted_count)

delete_document()