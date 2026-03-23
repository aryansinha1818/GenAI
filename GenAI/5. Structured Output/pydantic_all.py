from pydantic import BaseModel
from typing import Optional

class Student(BaseModel):
    # by-default
    # name: str = 'Aryan'

# optional
    name: str = "Aryan"
    age : Optional[int] = None

new_student = { }

student = Student(**new_student)

print(student)