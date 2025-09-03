import pymongo
if __name__=="__main__":
    mongo_client=pymongo.MongoClient('mongodb://localhost:27017')
    database=mongo_client['library']
    collections=database['books']
    output=collections.find()
    in_operator=collections.find({"year":{"$in":[1813,1869]}})
    print("=======================[In operator]=======================")
    for item in in_operator:
        print(item)
    
    equalty_ope = collections.find({"author": {"$eq": "Jane Austen"}})
    print("=======================[Equality operator]=======================")
    for item in equalty_ope:
        print(item)
   
    print("=======================[Logical operator]=======================")
    logical_ope=collections.find({"$and":[
        {"title":{"$eq":"War and Peace"}},
        {"year":{"$eq":1869}}
        ]})
    for item in logical_ope:
        print(item) 

    print("=======================[OR operator]=======================")
    OR_operator=collections.find({"$or":[
        {"title":{"$eq":"To Kill a Mockingbird"}},
        {"author":{"$eq":"Godwin"}}
    ]})
    
    for item in OR_operator:
        print(item)

    print("=======================[Case Sensitive Regex]=======================")
    reg_expression=collections.find({
        "title":{"$regex":"^P"}
    })
    for item in reg_expression:
        print(item)
    
    print("=======================[Case insensitive Regex]=======================")
    case_insensitve_regex = collections.find({
        "title": {
            "$regex": "^p",
            "$options": "i"
        }
    })
    for item in case_insensitve_regex:
        print(item)

