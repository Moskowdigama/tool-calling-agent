from typing import List, Dict, Any, Optional
from typing_extensions import TypedDict


class MultiAgentState(TypedDict):
    """Shared state passed sequentially through the agent pipeline."""
    
    # Input
    query: str
    
    # Searcher output
    search_results: Optional[List[Dict[str, Any]]]
    
    # Reader/Scraper output
    raw_content: Optional[List[Dict[str, str]]]
    
    # Writer output
    draft_report: Optional[str]
    
    # Critic output
    critic_score: Optional[int]         # 1-10
    critic_feedback: Optional[str]
    revised_report: Optional[str]
    
    # Final output
    final_output: Optional[str]
    
    # Debug/observability
    agent_logs: List[Dict[str, Any]]


def create_initial_state(query: str) -> MultiAgentState:
    """Initialize a fresh state for a new query."""
    return MultiAgentState(
        query=query,
        search_results=None,
        raw_content=None,
        draft_report=None,
        critic_score=None,
        critic_feedback=None,
        revised_report=None,
        final_output=None,
        agent_logs=[]
    )
