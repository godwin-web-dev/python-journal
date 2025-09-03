# MongoDB Shell → PyMongo Cheat Sheet

---

## 1. Connect to Database

**Mongo Shell**
```shell
use organisation
```

**PyMongo**
```python
import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["organisation"]
```

---

## 2. Create / Use a Collection

**Mongo Shell**
```shell
db.createCollection("employee")
```

**PyMongo**
```python
collection = db["employee"]  # auto-created when first used
```

---

## 3. Insert Documents

**Mongo Shell**
```shell
db.employee.insertOne({name: "Alice", age: 25})
db.employee.insertMany([{...}, {...}])
```

**PyMongo**
```python
collection.insert_one({"name": "Alice", "age": 25})
collection.insert_many([{...}, {...}])
```

---

## 4. Find Documents

**Mongo Shell**
```shell
db.employee.findOne()
db.employee.find({age: {$gt: 25}})
db.employee.find({}, {name: 1, _id: 0})  # projection
```

**PyMongo**
```python
collection.find_one()
collection.find({"age": {"$gt": 25}})
collection.find({}, {"name": 1, "_id": 0})  # projection
```

---

## 5. Update Documents

**Mongo Shell**
```shell
db.employee.updateOne({name: "Alice"}, {$set: {age: 30}})
db.employee.updateMany({dept: "IT"}, {$inc: {salary: 1000}})
```

**PyMongo**
```python
collection.update_one({"name": "Alice"}, {"$set": {"age": 30}})
collection.update_many({"dept": "IT"}, {"$inc": {"salary": 1000}})
```

---

## 6. Delete Documents

**Mongo Shell**
```shell
db.employee.deleteOne({name: "Alice"})
db.employee.deleteMany({age: {$lt: 25}})
```

**PyMongo**
```python
collection.delete_one({"name": "Alice"})
collection.delete_many({"age": {"$lt": 25}})
```

---

## 7. Comparison Operators

| Meaning                  | Mongo Shell                | PyMongo                        |
|--------------------------|---------------------------|--------------------------------|
| Greater than             | `{age: {$gt: 25}}`        | `{"age": {"$gt": 25}}`         |
| Less than                | `{age: {$lt: 25}}`        | `{"age": {"$lt": 25}}`         |
| Greater than or equal    | `{age: {$gte: 25}}`       | `{"age": {"$gte": 25}}`        |
| Less than or equal       | `{age: {$lte: 25}}`       | `{"age": {"$lte": 25}}`        |
| Equal                    | `{age: 25}`               | `{"age": 25}`                  |
| Not equal                | `{age: {$ne: 25}}`        | `{"age": {"$ne": 25}}`         |

---

## 8. Sorting & Limiting

**Mongo Shell**
```shell
db.employee.find().sort({age: 1})
db.employee.find().sort({age: -1})
db.employee.find().limit(5)
```

**PyMongo**
```python
collection.find().sort("age", 1)
collection.find().sort("age", -1)
collection.find().limit(5)
```

---

## 9. Drop Collection / Database

**Mongo Shell**
```shell
db.employee.drop()
db.dropDatabase()
```

**PyMongo**
```python
collection.drop()
client.drop_database("organisation")
```

---

## 10. Aggregation Example

**Mongo Shell**
```javascript
db.employee.aggregate([
  {$match: {dept: "IT"}},
  {$group: {_id: "$dept", avgSalary: {$avg: "$salary"}}}
])
```

**PyMongo**
```python
collection.aggregate([
    {"$match": {"dept": "IT"}},
    {"$group": {"_id": "$dept", "avgSalary": {"$avg": "$salary"}}}
])
```

---

💡 **Tip:** When you see `{}` in shell, it’s the same in PyMongo — only the method names and parameters change.

📌 Keep this cheat sheet handy to follow any shell tutorial and instantly write the Python version without restarting
