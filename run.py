from fastapi import FastAPI
from pydantic import BaseModel
from langchain_core.messages import HumanMessage, SystemMessage
from agent import recruitment_agent, support_satisfaction_agent

# FastAPI app
app = FastAPI(title="AI Agent API", description="LangChain Agent API for Q&A", version="1.0")

# Request body schema
class QueryRequest(BaseModel):
    query: str

# Response schema
class QueryResponse(BaseModel):
    response: str

@app.post("/recruitment_agent", response_model=QueryResponse)
def ask_agent(request: QueryRequest):
    """API endpoint to query the agent"""
    result = recruitment_agent(request.query)
    return QueryResponse(response=result)

@app.post("/support_agent", response_model=QueryResponse)
def ask_support_agent(request: QueryRequest):
    """API endpoint to query the support agent"""
    result = support_satisfaction_agent(request.query)
    return QueryResponse(response=result)

# Run using: uvicorn run:app --reload



# Show me all candidates with at least 5 years of experience in Software Engineering located in Paris.
# Find candidates from LinkedIn who have worked as Project Managers in London.
# List fresh graduate candidates (0–2 years of experience) available in India.
# Which candidates have Marketing backgrounds and are located in New York?
# Show me senior candidates (7+ years experience) applying for Finance-related positions.
# Show me candidates with Data Science or AI experience based in France