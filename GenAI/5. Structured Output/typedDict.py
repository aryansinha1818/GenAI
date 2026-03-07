from typing import TypedDict

class Person(TypedDict):
    name: str
    age: int

p1 : Person = {'name':"Aryan", 'age' : 25}

print(p1)