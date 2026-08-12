"""
Reader/Scraper Agent: Extracts and reads content from URLs.
"""

import requests
from bs4 import BeautifulSoup
from typing import Dict, Any, List

from ..core.state import MultiAgentState


def extract_text_from_url(url: str, max_chars: int = 5000) -> str:
    """
    Extract readable text content from a URL.
    """
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }
        response = requests.get(url, timeout=10, headers=headers)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Remove script and style tags
        for tag in soup(["script", "style", "nav", "footer", "header"]):
            tag.decompose()
        
        # Get text
        text = soup.get_text(separator="\n")
        
        # Clean up whitespace
        lines = [line.strip() for line in text.split("\n") if line.strip()]
        content = "\n".join(lines)
        
        # Truncate to max_chars
        if len(content) > max_chars:
            content = content[:max_chars] + "... [truncated]"
        
        return content
    except Exception as e:
        return f"[Error extracting content: {str(e)}]"


def reader_agent(state: MultiAgentState, llm) -> MultiAgentState:
    """
    Reader agent that takes search results and extracts full content.
    """
    search_results = state.get("search_results", [])
    
    if not search_results:
        state["raw_content"] = []
        state["agent_logs"].append({
            "agent": "Reader",
            "status": "error",
            "message": "No search results to read"
        })
        return state
    
    raw_content = []
    for result in search_results:
        url = result.get("url", "")
        if url:
            content = extract_text_from_url(url)
            raw_content.append({
                "url": url,
                "title": result.get("title", ""),
                "content": content
            })
    
    state["raw_content"] = raw_content
    state["agent_logs"].append({
        "agent": "Reader",
        "urls_processed": len(raw_content),
        "status": "success"
    })
    
    return state
