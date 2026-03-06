import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

llm = ChatOpenAI(model="gpt-5-mini", temperature=0)

class llm_schema_td(TypedDict):
    setup: str 
    punchline: str


#if you write ketchup instead of setup below, it will still run, while pydantic will fail, this is advantage difference between pydantic and typeddict
#obj = llm_schema_td({"ketchup":"some setup","punchline":"Some punchline"})
#print(obj)

llm_structured_typedict = llm.with_structured_output(llm_schema_td)

result = llm_structured_typedict.invoke("Tell me a joke")

print(result)

