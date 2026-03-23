from typing import TypedDict

class Person(TypedDict):
    
    name: str
    age: int


p1 : Person = {'name':"Aryan", 'age' : 25}
p2 : Person = {'name':'sinha', 'age': 'forty-two'}


print(p1)

# crossing the type but still prints
print(p2)