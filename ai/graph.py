"""
LangGraph workflow for emotion analysis
Orchestrates the multi-step emotion analysis process using Gemini AI
"""

from typing import TypedDict, Annotated
from langgraph.graph import StateGraph, END
from ai.nodes import (
    extract_emotion,
    generate_scores,
    extract_keywords,
    generate_reflection
)


class EmotionState(TypedDict):
    """State object passed through the workflow"""
    user_input: str
    emotion: str
    mood_score: int
    energy_score: int
    stress_score: int
    keywords: list[str]
    reflection: str


def create_emotion_graph():
    """
    Creates and compiles the LangGraph workflow for emotion analysis
    
    Workflow:
    1. Extract primary emotion
    2. Generate numeric scores (mood, energy, stress)
    3. Extract top 3 emotional keywords
    4. Generate supportive reflection message
    
    Returns:
        Compiled StateGraph ready for execution
    """
    # Initialize the graph
    workflow = StateGraph(EmotionState)
    
    # Add nodes
    workflow.add_node("extract_emotion", extract_emotion)
    workflow.add_node("generate_scores", generate_scores)
    workflow.add_node("extract_keywords", extract_keywords)
    workflow.add_node("generate_reflection", generate_reflection)
    
    # Define the flow
    workflow.set_entry_point("extract_emotion")
    workflow.add_edge("extract_emotion", "generate_scores")
    workflow.add_edge("generate_scores", "extract_keywords")
    workflow.add_edge("extract_keywords", "generate_reflection")
    workflow.add_edge("generate_reflection", END)
    
    # Compile and return
    return workflow.compile()
