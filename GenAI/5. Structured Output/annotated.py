# role we will take the reviews from the client and then based on taht keywords and what us the emotion good or bad
# here we decide to give a statement to llm in-case there is an ambiguity
#  we want to get evrything systematic 
# reviews in one place and cons. if neither then don't
# if talking about a topic then say charging then it should come. the key ideas
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model = ChatOpenAI(model="gpt-4o")

class Review(TypedDict):
    key_themes : Annotated[list[str], "Write down all the key themes discussed in the review"]
    summary: Annotated[str, "The summary of the review"]
    sentiment: Annotated[Literal["positive", "negative"], "The sentiment of the review either negative, positive or neutral"]
    pros: Annotated[Optional[list[str]], "Write down all the pros of the product"]
    cons: Annotated[Optional[list[str]], "Write down all the cons of the product"]
    name: Annotated[Optional[str], "Write the name of the reviewer"]

structured_model = model.with_structured_output(Review)

result = structured_model.invoke('''The hardware is great, but the software feels bloated. There are too many pre-installed apps that I can’t remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this. I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45M fast charging is a lifesaver. The S-Pen integration is a great touch for note-taking and quick sketches, though I don’t use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality. However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow. Pros: Insanely powerful processor (great for gaming and productivity) Stunning 200MP camera with incredible zoom capabilities Long battery life with fast charging S-Pen support is unique and useful Cons: Bulky and heavy—not great for one-handed use Bloatware still exists in One UI Expensive compared to competitors
                                 
                                 review by Aryan Sinha
''')

# print(type(result))
# print(result)
print(result['sentiment'])
print(result['summary'])
print(result['name'])