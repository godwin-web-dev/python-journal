from pydantic import BaseModel
from typing import Optional

class Types(BaseModel):
    id:int
    name:str
    description:str
    is_student:Optional[bool]

data={"id":"1","name":"Godwin","description":"My name is Godwin","is_student":False}
result=Types(**data)
print(result)

data2={"id":1,"name":21,"description":"My name is Godwin","is_student":False}
result2=Types(**data2)
print(result2)

# here it does not throw error because pydantic does internal type coercion from the string to int 

# note it does not allow you to insert the number when u define the type as the string to the int then pydantic will throw error such as this Input should be a valid string [type=string_type, input_value=21, input_type=int] 
