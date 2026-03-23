from pydantic import BaseModel

class Student(BaseModel):
    name: str
    
# new_student = { 'name': 'pankaj'}
new_student = { 'name': 23}

student = Student(**new_student)

print(student.name)