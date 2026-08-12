from datetime import datetime
from langchain_mistralai import ChatMistralAI
from langgraph.prebuilt import create_react_agent
from core.skill_registry import get_all_skills

def build_agent_executor(mistral_api_key: str):
    """Builds and returns a modern LangGraph ReAct agent executor with date awareness."""
    llm = ChatMistralAI(
        model="mistral-small-latest",
        mistral_api_key=mistral_api_key,
        temperature=0.1
    )
    
    skills = get_all_skills()
    
    current_date = datetime.now().strftime("%B %Y")
    system_prompt = f"You are a helpful assistant with real-time skills. The current date is {current_date}. Always ensure search queries for news, sports, or events include the relevant current year/month."
    
    agent = create_react_agent(
        model=llm,
        tools=skills,
        state_modifier=system_prompt
    )
    
    return agent
