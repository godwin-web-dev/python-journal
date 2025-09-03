import pymongo 
def update_document():
    mongo_client=pymongo.MongoClient('mongodb://localhost:27017')
    my_database = mongo_client['organisation']
    collection = my_database['employee']

    # to update the salary of the Alice from 55000 to 90,000
    collection.update_one(
        {'name': 'Alice'},
        {"$set":{
             'salary': 90000
        }}
    )

    # to increment the salary of the bob from 70000 to 
    collection.update_one(
        {'name':'Bob'},
        {'$inc':{
            'salary':1000
        }}
    )

    # to change the department of the jaden from the finance to IT
    collection.update_one(
        {'name':'Jaden'},
        {'$set':{
            'department':'IT'
        }}
    )

    # Decrease the salary of the Alice due to the tax
    collection.update_one(
        {'name':'Alice'},
        {"$inc":{
            'salary':-10000
        }}
    )
    # note do not use the desc if u want to decrement the value just do negative and it will reduce that
    # if u use the update_many it will update all the records corresponding to that key 

update_document()