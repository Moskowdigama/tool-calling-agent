"""
Searcher Agent: Uses Tavily API to search for information.
"""

import os
from typing import Dict, Any, List
from tavily import TavilyClient

from ..core.state import MultiAgentState


def searcher_agent(state: MultiAgentState, llm) -> MultiAgentState:
    """
    Searcher agent that takes a query and returns search results.
    
    Uses Tavily API for web search.
    """
    query = state["query"]
    
    # Get Tavily API key from environment
    tavily_key = os.getenv("TAVILY_API_KEY")
    if not tavily_key:
        raise ValueError("TAVILY_API_KEY not set in environment variables")
    
    tavily = TavilyClient(api_key=tavily_key)
    
    # Perform search
    response = tavily.search(
        query=query,
        search_depth="basic",  # Use "advanced" for more thorough search
        max_results=5
    )
    
    search_results = [
        {
            "title": result.get("title", ""),
            "url": result.get("url", ""),
            "content": result.get("content", ""),
            "score": result.get("score", 0.0)
        }
        for result in response.get("results", [])
    ]
    
    # Update state
    state["search_results"] = search_results
    state["agent_logs"].append({
        "agent": "Searcher",
        "query": query,
        "results_count": len(search_results),
        "status": "success"
    })
    
    return state
