from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv
import os

load_dotenv()

# FastAPI app
app = FastAPI()

# LangChain setup
llm = ChatOpenAI(model="gpt-4o", temperature=0.7)
memory = ConversationBufferMemory(return_messages=True)
chain = ConversationChain(llm=llm, memory=memory)

# Request model
class RecipeRequest(BaseModel):
    type: str  # veg / non-veg
    ingredients: List[str]
    time: str

# POST endpoint
@app.post("/generate-recipe")
def generate_recipe(data: RecipeRequest):
    prompt = f"""
You are a helpful AI chef.

The user wants a {data.type} recipe.

Available ingredients: {", ".join(data.ingredients)}.
Time available: {data.time}.

Generate:
1. Title of the dish
2. Ingredients list
3. Step-by-step instructions
4. At the end of the instructions, include macros like:
   - Calories
   - Protein
   - Carbs

Write everything clearly in plain text.
"""

    # Run prompt through LangChain conversation chain
    response = chain.run(prompt)

    # Basic response parsing
    lines = response.strip().split("\n")
    title = lines[0].strip()
    ingredients = []
    instructions_lines = []
    started_instructions = False

    for line in lines[1:]:
        if "Ingredients" in line:
            continue
        elif "Instructions" in line or "Step" in line:
            started_instructions = True
            continue
        elif started_instructions:
            instructions_lines.append(line.strip())
        else:
            ingredients.append(line.strip())

    return {
        "title": title,
        "ingredients": [i for i in ingredients if i],
        "instructions": " ".join(instructions_lines),
        "time": data.time
    }
