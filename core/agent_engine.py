from langchain_mistralai import ChatMistralAI
from langgraph.prebuilt import create_react_agent
from core.skill_registry import get_all_skills

def build_agent_executor(mistral_api_key: str):
    """Builds and returns a modern LangGraph ReAct agent executor without keyword parameter conflicts."""
    llm = ChatMistralAI(
        model="mistral-small-latest",
        mistral_api_key=mistral_api_key,
        temperature=0.1
    )
    
    skills = get_all_skills()
    
    # Pure positional instantiation to prevent parameter name exceptions across LangGraph versions
    agent = create_react_agent(llm, skills)
    
    return agent
