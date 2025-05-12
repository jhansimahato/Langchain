from pydantic import BaseModel,EmailStr,Field
from typing import Optional

class Student(BaseModel):
    name: str
    age: Optional[int] = None
    email: Optional[EmailStr] = None
    cgpa: float = Field(gt=0,lt=10,default=5.0,description="CGPA decimal value representing the cgpa of the student")
    

    
new_student = {'name': 'John Doe','email': 'johndoe@gmail.com'}
student = Student(**new_student)
# This will raise a validation error if the data does not match the model.
print(type(student))
print(student)