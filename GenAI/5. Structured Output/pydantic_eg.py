from pydantic import BaseModel

class Id(BaseModel):
    id: int
    name: str

# dict form
emp1 = Id(id= 1, name='Aryan')
emp2 = Id(id=2, name="Sinha")

print(emp1)
print(emp2)