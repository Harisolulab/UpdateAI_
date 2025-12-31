from tools import Recruitment_Agent, Content_Agent,Support_Agent,Crm_Agent
from prompt import recruitment_agent_prompt, content_agent_prompt,support_agent_prompt, crm_agent_prompt
from build_agent import build_agent, run_agent
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

########################################
# 1. Define Behavioral Prompt
########################################

def recruitment_agent(query):
    user_prompt = f"User query: {query}"
    prompt = recruitment_agent_prompt #hari
    tools_list = [Recruitment_Agent] #hari
    agent = build_agent(tools_list)
    response = run_agent(agent, prompt)
    return response

def Content_agent(query):
    user_prompt = f"User query: {query}"
    prompt = content_agent_prompt #hari
    tools_list = [Content_Agent] #hari
    agent = build_agent(tools_list)
    response = run_agent(agent, prompt)
    return response


def Support_agent(query):
    user_prompt = f"User query: {query}"
    prompt = support_agent_prompt #hari
    tools_list = [Support_Agent] #hari
    agent = build_agent(tools_list)
    response = run_agent(agent, prompt)
    return response
    

def CRM_agent(query):
    user_prompt = f"User query: {query}"
    prompt = crm_agent_prompt #hari
    tools_list = [Crm_Agent] #hari
    agent = build_agent(tools_list)
    response = run_agent(agent, prompt)
    return response
    
prompt = "Screen candidate 789 for the Data Scientist role and provide a hiring recommendation."
print(recruitment_agent(prompt))

"""prompt = "Create a short LinkedIn post announcing an opening for a Data Scientist position."
print(content_agent(prompt))

prompt = "Respond to a candidate asking about the interview process timeline for the Data Scientist role."
print(Support_Agent(prompt))

prompt = "Respond to a candidate asking about the interview process timeline for the Data Scientist role."
print(CRM_agent(prompt))"""