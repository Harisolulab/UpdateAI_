from langchain_openai import AzureChatOpenAI
from langchain.tools import tool
from langgraph.prebuilt import create_react_agent
import os
#from langchain import OpenAI #tanul

from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# 1. Define Azure OpenAI LLM
llm = AzureChatOpenAI(
        deployment_name=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
        azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION")
    )

# OpenAI LLM
#llm = OpenAI(
#    model="gpt-4o",
#    api_key=os.getenv("OPENAI_API_KEY")
#)

def build_agent(tools):
    # 4. Create the agent graph
    agent = create_react_agent(
        model=llm,
        tools=tools
    )
    return agent

def run_agent(agent, query):
    result = agent.invoke({"messages": query})
    return result["messages"][-1].content
