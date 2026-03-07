from langchain_openai import ChatOpenAI
from langchain.tools import tool
from langchain.agents import initialize_agent, AgentType

@tool
def get_weather(city: str) -> str:
    """Gives weather for given city."""
    return f"Weather for {city}"

llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo")
agent = initialize_agent(
    tools=[get_weather],
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True
)

response = agent.invoke("What's the weather in Bhubaneswar today?")
print(response)