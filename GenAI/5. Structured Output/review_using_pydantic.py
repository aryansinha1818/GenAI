from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# Initialize model
model = ChatOpenAI(model="gpt-4o")

# ✅ JSON Schema (instead of Pydantic)
review_schema = {
    "name": "Review",
    "description": "Extract structured information from a product review",
    "parameters": {
        "type": "object",
        "properties": {
            "key_themes": {
                "type": "array",
                "items": {"type": "string"},
                "description": "All key themes discussed in the review"
            },
            "summary": {
                "type": "string",
                "description": "A brief summary of the review"
            },
            "sentiment": {
                "type": "string",
                "enum": ["positive", "negative"],
                "description": "Sentiment of the review"
            }
        },
        "required": ["key_themes", "summary", "sentiment"]
    }
}

# Structured output using JSON schema
structured_model = model.with_structured_output(review_schema)

# Invoke model
result = structured_model.invoke(
    "The hardware is great, but the software feels bloated..."
)

# ✅ Outputs
print(type(result))      # dict
print(result)            # full structured output

# Access fields
print(result["summary"])
print(result["sentiment"])
print(result["key_themes"])