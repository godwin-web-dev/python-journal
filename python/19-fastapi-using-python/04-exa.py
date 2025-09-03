from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()

@app.get("/")
def root():
    return {"Root user":"Godwin"}

class Template(BaseModel):
    id:int
    title:str
    completed:bool

todo_app=[
    Template(id=1,title="Read books",completed=False),
    Template(id=2,title="Practice code",completed=False),
    Template(id=3,title="Go For Walk ",completed=False)
]
@app.get("/list_todo")
async def todo():
    return todo_app

