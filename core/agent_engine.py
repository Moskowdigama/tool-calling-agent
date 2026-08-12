from datetime import datetime
from langchain_mistralai import ChatMistralAI
from langgraph.prebuilt import create_react_agent
from core.skill_registry import get_all_skills

def build_agent_executor(mistral_api_key: str):
    """Builds and returns a modern LangGraph ReAct agent executor with live system date context."""
    llm = ChatMistralAI(
        model="mistral-small-latest",
        mistral_api_key=mistral_api_key,
        temperature=0.1
    )
    
    skills = get_all_skills()
    
    today_str = datetime.now().strftime("%A, %B %d, %Y")
    system_prompt = f"You are an assistant with tool access. Today's date is strictly {today_str}. When asked for the date or weather, rely on exact facts and tools."
    
    agent = create_react_agent(
        model=llm,
        tools=skills,
        state_modifier=system_prompt
    )
    
    return agent
