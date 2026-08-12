from langchain_mistralai import ChatMistralAI
from langchain.agents import create_react_agent, AgentExecutor
from langchain_core.prompts import PromptTemplate
from core.skill_registry import get_all_skills

def build_agent_executor(mistral_api_key: str):
    """Builds and returns a ReAct agent executor wired with registered skills."""
    llm = ChatMistralAI(
        model="mistral-small-latest",
        mistral_api_key=mistral_api_key,
        temperature=0.1
    )
    
    skills = get_all_skills()
    
    template = """Answer the following questions as best as you can. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought:{agent_scratchpad}"""

    prompt = PromptTemplate.from_template(template)
    
    agent = create_react_agent(
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
