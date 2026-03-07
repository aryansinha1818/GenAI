from pydantic import BaseModel, EmailStr, Field
from typing import Optional

# we make classes
class Student(BaseModel):
    name : str
    age : int = 18  # default value for age
    id : Optional[int] = None
    email: Optional[EmailStr] = Field(default=None, description="Email address of the student")
    cgpa: float = Field(default=0.0, ge=0.0, le=4.0, description="GPA must be between 0.0 and 4.0")

# dict form
new_student = {'name':'Aryan'}

# unpacks the dict new stud into these keyword arguments
# Without **, Pydantic would treat the entire dictionary as a single value for the first field (e.g., name), causing a validation error because name expects a str, not a dict
stud = Student(**new_student)
# When to Use **:
# Always when passing a dictionary to match a Pydantic model’s fields.

# Not needed if you pass values directly:
print(stud)
print(stud.name)
print(stud.age)

print("New value")
stud2 = {'name': 'Sinha', 'age': 20}
val2 = Student(**stud2)
print(val2)
print(val2.name)
print(val2.age)

stud3 = Student(name='Aryan', age=19, email="abc@gmail.com")
print(stud3)
print(stud3.name)
print(stud3.age)
print(stud3.email)