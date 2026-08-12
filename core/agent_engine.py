from langchain_mistralai import ChatMistralAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from core.skill_registry import get_all_skills

def build_agent_executor(mistral_api_key: str):
    """Builds and returns a Tool-Calling agent executor wired with registered skills."""
    llm = ChatMistralAI(
        model="mistral-small-latest",
        mistral_api_key=mistral_api_key,
        temperature=0.1
    )
    
    skills = get_all_skills()
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an intelligent assistant with access to specialized tools. Use them to answer questions accurately."),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ])
    
    agent = create_tool_calling_agent(
        llm=llm,
        tools=skills,
        prompt=prompt
    )
    
    executor = AgentExecutor(
        agent=agent,
        tools=skills,
        verbose=True,
        handle_parsing_errors=True,
        max_iterations=5
    )
    
    return executor
