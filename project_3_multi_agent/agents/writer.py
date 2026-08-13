"""
Writer Agent: Synthesizes research into a coherent report.
"""

from typing import Dict, Any
from langchain_core.messages import HumanMessage, SystemMessage

from core.state import MultiAgentState


def writer_agent(state: MultiAgentState, llm) -> MultiAgentState:
    """
    Writer agent that takes raw content and produces a well-structured report.
    """
    query = state["query"]
    raw_content = state.get("raw_content", [])
    
    if not raw_content:
        state["draft_report"] = "No content available to write a report."
        state["agent_logs"].append({
            "agent": "Writer",
            "status": "error",
            "message": "No raw content available"
        })
        return state
    
    # Prepare content for LLM
    content_text = "\n\n".join([
        f"Source: {item['title']} ({item['url']})\n{item['content'][:2000]}"
        for item in raw_content[:3]  # Limit to top 3 sources to save context
    ])
    
    system_prompt = """You are a professional research writer. Synthesize the provided information into a clear, well-structured report.

Guidelines:
- Start with an executive summary
- Organize information logically with headings
- Cite sources by title
- Be objective and factual
- Use clear, professional language
- Include key facts, statistics, and insights
- End with a conclusion"""

    human_prompt = f"""
Query: {query}

Information from sources:
{content_text}

Write a comprehensive report answering the query above. Use the information provided and cite your sources.
"""
    
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=human_prompt)
    ]
    
    response = llm.invoke(messages)
    draft = response.content
    
    state["draft_report"] = draft
    state["agent_logs"].append({
        "agent": "Writer",
        "content_length": len(draft),
        "status": "success"
    })
    
    return state
