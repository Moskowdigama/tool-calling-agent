from langchain_mistralai import ChatMistralAI
from langgraph.prebuilt import create_react_agent
from core.skill_registry import get_all_skills

def build_agent_executor(mistral_api_key: str):
    """Builds agent without optional keyword arguments to maintain compatibility across LangGraph versions."""
    llm = ChatMistralAI(
        model="mistral-small-latest",
        mistral_api_key=mistral_api_key,
        temperature=0.1
    )
    
    skills = get_all_skills()
    
    # Pure positional arguments only
    agent = create_react_agent(llm, skills)
    
    return agent
