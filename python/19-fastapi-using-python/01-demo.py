from fastapi import FastAPI

# Create an instance of the FastAPI application
app = FastAPI()

# Terminolgy of the fast api
# 1. '/' is called the "path" or "route"
# 2. get('/') specifies the HTTP method (GET) for the path
# 3. @app.get('/') is called a "path operation decorator"
# 4. The function below is called a "path operation function" or "endpoint function"

@app.get('/')
def base_url():
    return {"message": "Hello to the base url route"}

@app.get('/aboutme')
def aboutme():
    return {"name":"godwin","age":'23'}
