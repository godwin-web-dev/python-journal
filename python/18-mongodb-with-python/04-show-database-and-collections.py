import pymongo

def show_database_collections():
    mongo_client = pymongo.MongoClient('mongodb://localhost:27017')
    print(mongo_client)

    # Show databases inside the mongo_client
    databases = mongo_client.list_database_names()
    print("databases are as follow:", databases)

    # Show the collections inside the 'godwin' database
    godwin_db = mongo_client['godwin']
    collections = godwin_db.list_collection_names()
    print("collections in 'godwin' database are as follow:", collections)

show_database_collections()