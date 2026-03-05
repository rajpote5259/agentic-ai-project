from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

llm = ChatOpenAI(model="gpt-5-mini", temperature=0)

prompt_template = ChatPromptTemplate.from_messages([
    ("system","You are a polite assistant"),
    ("user","Write a fun fact about {topic}")
])

user_input = input("Enter a topic for fun fact: ")

ready_prompt = prompt_template.invoke({"topic": user_input})

response = llm.invoke(ready_prompt.messages)

print(response.content)