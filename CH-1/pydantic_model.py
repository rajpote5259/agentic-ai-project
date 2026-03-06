import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field

load_dotenv()

llm = ChatOpenAI(model="gpt-5-mini", temperature=0)

class llm_schema(BaseModel):
    setup: str = Field(description="The setup for the joke")
    punchline: str = Field(description="The punchline for the joke")

#obj = llm_schema(**{"setup":"some setup", "punchline":"some puchline"})
#print(obj.setup)

llm_structured_output = llm.with_structured_output(llm_schema)

result = llm_structured_output.invoke("Tell me a joke")

print(result)

