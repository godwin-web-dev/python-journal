from pydantic import BaseModel
from typing import List ,Optional,Dict

class EmployeeModel(BaseModel):
    id:int
    name:str
    department:Optional[str]="General"
    salary:float
    emp_details:Dict[str,int|str] # syntax explained in dict the keys was supposed to be string and values was supposed to be int since we have used optional value can be int or str 

data={"id":1,"name":"Godwin","department":'IT',"salary":55000.211,"emp_details":{
    "project_name":"confidential",
    "project":1
}}

result=EmployeeModel(**data)
print(result)
