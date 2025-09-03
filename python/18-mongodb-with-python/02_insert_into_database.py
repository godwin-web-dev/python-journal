import pymongo

'''
To create a database in MongoDB:
1. Connect to the MongoDB client.
2. After connecting, create a database (it will be created automatically when you first store data).
3. Inside the created database, create a collection (also created automatically on first use).
4. Insert data into the collection. There are two ways to insert data:
    1. insert_one: Allows you to insert one record (document) at a time.
    2. insert_many: Allows you to insert a list of dictionaries (documents) at a time.
5. If you do not specify the "_id", it will be automatically created like this: _id:ObjectId
   (e.g., 689ed5e091d6319d9d549972). Created IDs are used to identify each record uniquely in large databases.
   You can also give a manual ID based on the requirement.
6. Each time you run the Python script, the records will be inserted again and again into the database.
7. NOTE: If you cannot find the created database, just refresh in MongoDB and later you will be able to see the created records.
'''

def creating_database():
    mongo_client = pymongo.MongoClient('mongodb://localhost:27017')
    print("mongo_client", mongo_client)
    my_database = mongo_client['organisation']
    collection = my_database['employee']
    employee_details = [
        {"_id": 1, "name": 'Alice', 'department': 'HR', "salary": 55000},
        {"_id": 2, "name": 'Bob', 'department': 'IT', "salary": 70000},
        {"_id": 3, "name": 'Jaden', 'department': 'Finance', "salary": 43000},
        {"_id": 4, "name": 'Will Smith', 'department': 'Digital Marketing', "salary": 20000},
        {"_id": 5, "name": 'Ethan Brown', 'department': 'Operations', "salary": 69000},
        {"_id": 6,"name": 'Alia', 'department': 'Devops', "salary": 60000},
        {"_id": 7, "name": 'Alice', 'department': 'HR', "salary": 55000},
    ]
    collection.insert_many(employee_details)

creating_database()