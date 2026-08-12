"""
Multi-Agent Orchestrator using LCEL sequential chain.

Pipeline: Searcher -> Reader -> Writer -> Critic
"""

import os
from typing import Dict, Any
from langchain_core.runnables import RunnablePassthrough, RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from langchain_mistralai import ChatMistralAI

from .state import MultiAgentState, create_initial_state
from ..agents.searcher import searcher_agent
from ..agents.reader import reader_agent
from ..agents.writer import writer_agent
from ..agents.critic import critic_agent


class MultiAgentOrchestrator:
    """Orchestrates the sequential multi-agent pipeline using LCEL."""
    
    def __init__(self, api_key: str):
        self.llm = ChatMistralAI(
            model="mistral-small-latest",
            api_key=api_key,
            temperature=0.3
        )
        self._build_chain()
    
    def _build_chain(self):
        """Build the LCEL sequential chain."""
        
        # Step 1: Searcher
        searcher_step = RunnableLambda(
            lambda state: searcher_agent(state, self.llm)
        )
        
        # Step 2: Reader
        reader_step = RunnableLambda(
            lambda state: reader_agent(state, self.llm)
        )
        
        # Step 3: Writer
        writer_step = RunnableLambda(
            lambda state: writer_agent(state, self.llm)
        )
        
        # Step 4: Critic
        critic_step = RunnableLambda(
            lambda state: critic_agent(state, self.llm)
        )
        
        # Chain them sequentially
        self.chain = (
            RunnablePassthrough()
            | searcher_step
            | reader_step
            | writer_step
            | critic_step
        )
    
    def run(self, query: str) -> Dict[str, Any]:
        """Run the multi-agent pipeline on a query."""
        initial_state = create_initial_state(query)
        final_state = self.chain.invoke(initial_state)
        return final_state


def run_multi_agent_pipeline(query: str, api_key: str) -> Dict[str, Any]:
    """Convenience function to run the pipeline."""
    orchestrator = MultiAgentOrchestrator(api_key)
    return orchestrator.run(query)
