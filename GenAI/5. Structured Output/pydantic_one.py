# 1️⃣ Basic Example

# Defines a structured schema so LLM always returns data in a fixed format.

'''
from pydantic import BaseModel

class Review(BaseModel):
    name: str
    age: int

data = {"name": "Aryan", "age": 25}
obj = Review(**data)

print(obj)
'''

# 2️⃣ Default Values If a field is missing, Pydantic fills it automatically.

# from pydantic import BaseModel

# class User(BaseModel):
#     name: str
#     age: int = 18   # default

# print(User(name="Aryan"))

# 👉 Output: age becomes 18

# 3️⃣ Optional Fields

# Field may or may not be present.

# from typing import Optional
# from pydantic import BaseModel

# class User(BaseModel):
#     name: str
#     age: Optional[int] = None

# print(User(name="Aryan"))
# 4️⃣ Type Coercion

# Pydantic automatically converts types if possible.

# from pydantic import BaseModel

# class User(BaseModel):
#     age: int

# print(User(age="25"))   # string → int
# 5️⃣ Built-in Validation

# Ensures data follows rules (type, format, etc.)
'''
from pydantic import BaseModel

class User(BaseModel):
    age: int

# User(age="abc") → ❌ error
print(User(age=25))  # ✅

'''
# 6️⃣ Field Function (Advanced Control)

# Add constraints, defaults, descriptions, regex.
'''
from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(..., min_length=2)
    age: int = Field(..., gt=0, lt=100)

print(User(name="Aryan", age=25))
'''
# 7️⃣ Returns Pydantic Object → Convert to Dict/JSON
"""from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int

obj = User(name="Aryan", age=25)

print(obj.dict())   # dict
print(obj.json())   # JSON string"""


'''🧠 Why this matters (important) This is exactly what you use with LangChain structured output:

Ensures clean API responses

Avoids random text

Makes data usable in:

DB

Frontend

APIs'''