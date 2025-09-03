from fastapi import FastAPI

app = FastAPI()

fruits = ["apple", "mango", "banana", "orange", "kiwi"]

# Query parameters are parameters that are not part of the route path.
# They are passed in the URL after the '?' symbol, like /fruit?limit=3.
@app.get("/fruit")
def base_url(limit: int):
    return {"Fruits with the limit": fruits[:limit]}

# We created an array of fruits.
# The 'limit' query parameter (default is 3) controls how many fruits are returned.
# For example, /fruit?limit=2 will return the first 2 fruits.

# ==================================================================
# query params with the sort as the params

@app.get("/fruits_with_limit_sort")
def base_url(sort:bool=False):
    result=fruits[:]
    if sort:
         result.sort()
    return {"sorted fruits":result}

# if u access the route like this http://127.0.0.1:8000/fruits_with_limit_sort?sort=True then  u will be getting sorted list such as this 

# {
#   "sorted fruits": [
#     "apple",
#     "banana",
#     "kiwi",
#     "mango",
#     "orange"
#   ]
# }

# note always start the query params with "?" if u want to keep the additional params then use the "&" as the seperator


    
