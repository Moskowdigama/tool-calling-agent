"""
Critic Agent: Reviews and scores the draft report, suggests improvements.
"""

from typing import Dict, Any
from langchain_core.messages import HumanMessage, SystemMessage

from ..core.state import MultiAgentState


def critic_agent(state: MultiAgentState, llm) -> MultiAgentState:
    """
    Critic agent that reviews the draft report and provides feedback + score.
    """
    draft = state.get("draft_report", "")
    
    if not draft or draft == "No content available to write a report.":
        state["critic_score"] = 0
        state["critic_feedback"] = "No draft to review."
        state["final_output"] = draft
        state["agent_logs"].append({
            "agent": "Critic",
            "status": "error",
            "message": "No draft to review"
        })
        return state
    
    system_prompt = """You are a rigorous research critic. Review the provided report and provide:
1. A score from 1-10 (10 being perfect)
2. Constructive feedback on strengths and weaknesses
3. Specific suggestions for improvement
4. A revised version that addresses the feedback

Be critical but fair. Focus on:
- Completeness and accuracy
- Clarity and structure
- Use of source material
- Logical flow
- Actionable insights"""

    human_prompt = f"""
Original Report:
{draft}

Provide your critique with score, feedback, and a revised version.
Format your response as:
SCORE: [1-10]
FEEDBACK: [your detailed feedback]
REVISED REPORT: [improved version]
"""
    
    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=human_prompt)
    ]
    
    response = llm.invoke(messages)
    critique = response.content
    
    # Parse the response
    score = 0
    feedback = ""
    revised = draft
    
    lines = critique.split("\n")
    for line in lines:
        if line.startswith("SCORE:"):
            try:
                score = int(line.replace("SCORE:", "").strip())
            except:
                score = 5
        elif line.startswith("FEEDBACK:"):
            feedback = line.replace("FEEDBACK:", "").strip()
        elif line.startswith("REVISED REPORT:"):
            revised = "\n".join(lines[lines.index(line)+1:]).strip()
            break
    
    # If revised is empty, use original draft
    if not revised:
        revised = draft
    
    state["critic_score"] = score
    state["critic_feedback"] = feedback
    state["revised_report"] = revised
    state["final_output"] = revised  # Final output is the revised version
    state["agent_logs"].append({
        "agent": "Critic",
        "score": score,
        "status": "success"
    })
    
    return state
