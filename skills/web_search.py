import os
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.tools import tool

@tool
def search_web(query: str) -> str:
    """Useful for searching the live web for real-time information, news, current events, and facts."""
    search = TavilySearchResults(max_results=3)
    results = search.invoke({"query": query})
    return str(results)
