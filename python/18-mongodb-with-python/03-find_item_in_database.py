import pymongo

def creating_database():
    # Connect to MongoDB
    mongo_client = pymongo.MongoClient('mongodb://localhost:27017')
    print("mongo_client", mongo_client)

    # Select database and collection
    my_database = mongo_client['organisation']
    collection = my_database['employee']

    # -------------------- Without Field Filter --------------------
    print("\n--- Without Field Filter ---")
    find_one_item = collection.find_one({"name": 'Alice'})
    print("find one item ==> ", find_one_item)

    find_all_item = collection.find({"name": 'Alice'})
    print("find all item ", find_all_item)  # Cursor object
    for item in find_all_item:
        print("items are as follow ", item)

    # -------------------- With Field Filter --------------------
    print("\n--- With Field Filter (Only 'name' & 'salary') ---")
    find_all_item_filtered = collection.find({"name": 'Alice'}, {"salary": 1, "name": 1})
    print("find all item (filtered) ", find_all_item_filtered)  # Cursor object
    for item in find_all_item_filtered:
        print("items are as follow ", item)


creating_database()

# IMPORTANT NOTE:
# In MongoDB projections, if you set a field value to 1 (to include it), all other fields are excluded (set to 0) by default, except for the '_id' field, which is included unless explicitly excluded.
# If you set a field value to 0 (to exclude it), all other fields are included (set to 1) by default, except for the '_id' field.
# You cannot mix inclusion (1) and exclusion (0) in the same projection, except for the '_id' field.
    
# mongo_client MongoClient(host=['localhost:27017'], document_class=dict, tz_aware=False, connect=True)

# --- Without Field Filter ---
# find one item ==>  {'_id': 1, 'name': 'Alice', 'department': 'HR', 'salary': 55000}
# find all item  <pymongo.synchronous.cursor.Cursor object at 0x000001B5E7260470>
# items are as follow  {'_id': 1, 'name': 'Alice', 'department': 'HR', 'salary': 55000}
# items are as follow  {'_id': 7, 'name': 'Alice', 'department': 'HR', 'salary': 55000}

# --- With Field Filter (Only 'name' & 'salary') ---
# find all item (filtered)  <pymongo.synchronous.cursor.Cursor object at 0x000001B5E7260470>
# items are as follow  {'_id': 1, 'name': 'Alice', 'salary': 55000}
# items are as follow  {'_id': 7, 'name': 'Alice', 'salary': 55000}
