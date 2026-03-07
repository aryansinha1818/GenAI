from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
# a type of runnable multiple chains in parallel could be run
from langchain.schema.runnable import RunnableParallel

load_dotenv()

model1 = ChatOpenAI(model = "gpt-4o", temperature = 0.7)

model2 = ChatOpenAI(model = "gpt-3.5-turbo", temperature = 0.7)

prompt1 = PromptTemplate(
    template = 'Generate short and the simple notes from the following text \n {text}',
    input_variables=['text']
)
prompt2 = PromptTemplate(
    template = 'Generate 5 short question from the following text \n  {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template = 'Merge the provided notes and quiz into a single document  \n notes -> {notes} and quiz',
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

# parallel chain
paralle_chain = RunnableParallel({
    # dictinary
    'notes': prompt1  | model1 | parser,
    'quiz': prompt2 | model2 | parser 
})

final_chain = prompt3 | model1 | parser

chain = paralle_chain | final_chain

text = """
The Solar System consists of the Sun and eight planets: Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, and Neptune. Earth is the only known planet to support life due to its ideal distance from the Sun and presence of water. Jupiter, the largest planet, has a strong magnetic field and dozens of moons. The asteroid belt lies between Mars and Jupiter, containing rocky remnants from the Solar System’s formation. Saturn is famous for its stunning ring system made of ice and dust. Pluto, once considered the ninth planet, was reclassified as a dwarf planet in 2006. The Sun, a yellow dwarf star, makes up 99.8% of the Solar System’s mass. Space exploration has revealed key details about planetary atmospheres and potential for extraterrestrial life.
"""

result = chain.invoke({'text':text})

print(result)