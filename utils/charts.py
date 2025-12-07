"""
Plotly chart generation for emotion analytics
Creates interactive visualizations for mood tracking
"""

import plotly.graph_objects as go
import plotly.express as px
from typing import List, Dict, Any


def create_mood_timeline(mood_data: List[Dict[str, Any]]) -> go.Figure:
    """
    Create a line chart showing mood scores over time
    
    Args:
        mood_data: List of dicts with timestamp, mood_score, and emotion
        
    Returns:
        Plotly Figure object
    """
    if not mood_data:
        # Return empty chart with message
        fig = go.Figure()
        fig.add_annotation(
            text="No data yet. Start tracking your emotions!",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False,
            font=dict(size=16, color="#999")
        )
        fig.update_layout(
            title="Mood Timeline",
            xaxis_title="Time",
            yaxis_title="Mood Score",
            height=300,
            template="plotly_white"
        )
        return fig
    
    # Extract data
    timestamps = [entry["timestamp"] for entry in mood_data]
    mood_scores = [entry["mood_score"] for entry in mood_data]
    emotions = [entry["emotion"] for entry in mood_data]
    
    # Create line chart
    fig = go.Figure()
    
    fig.add_trace(go.Scatter(
        x=timestamps,
        y=mood_scores,
        mode='lines+markers',
        name='Mood',
        line=dict(color='#FF6B9D', width=3),
        marker=dict(size=8, color='#FF6B9D'),
        hovertemplate='<b>%{text}</b><br>Mood: %{y}/5<br>%{x}<extra></extra>',
        text=emotions
    ))
    
    fig.update_layout(
        title="Mood Timeline",
        xaxis_title="Time",
        yaxis_title="Mood Score (1-5)",
        yaxis=dict(range=[0, 6], dtick=1),
        height=350,
        template="plotly_white",
        hovermode='closest',
        font=dict(family="Arial, sans-serif")
    )
    
    return fig


def create_emotion_donut(emotion_counts: Dict[str, int]) -> go.Figure:
    """
    Create a donut chart showing emotion frequency distribution
    
    Args:
        emotion_counts: Dictionary mapping emotion names to counts
        
    Returns:
        Plotly Figure object
    """
    if not emotion_counts:
        # Return empty chart with message
        fig = go.Figure()
        fig.add_annotation(
            text="No data yet. Start tracking your emotions!",
            xref="paper", yref="paper",
            x=0.5, y=0.5, showarrow=False,
            font=dict(size=16, color="#999")
        )
        fig.update_layout(
            title="Emotion Distribution",
            height=300,
            template="plotly_white"
        )
        return fig
    
    # Color palette for emotions (warm, friendly colors)
    color_map = {
        "Happy": "#FFD93D",
        "Sad": "#6BCB77",
        "Angry": "#FF6B6B",
        "Anxious": "#A8DADC",
        "Stressed": "#F4A261",
        "Tired": "#B8B8D1",
        "Excited": "#FF9FF3",
        "Lonely": "#C9ADA7"
    }
    
    emotions = list(emotion_counts.keys())
    counts = list(emotion_counts.values())
    colors = [color_map.get(emotion, "#CCCCCC") for emotion in emotions]
    
    # Create donut chart
    fig = go.Figure(data=[go.Pie(
        labels=emotions,
        values=counts,
        hole=0.4,
        marker=dict(colors=colors),
        textinfo='label+percent',
        hovertemplate='<b>%{label}</b><br>Count: %{value}<br>%{percent}<extra></extra>'
    )])
    
    fig.update_layout(
        title="Emotion Distribution",
        height=350,
        template="plotly_white",
        font=dict(family="Arial, sans-serif"),
        showlegend=True
    )
    
    return fig


def create_score_bars(mood: int, energy: int, stress: int) -> go.Figure:
    """
    Create horizontal bar chart for current scores
    
    Args:
        mood: Mood score (1-5)
        energy: Energy score (1-5)
        stress: Stress score (1-5)
        
    Returns:
        Plotly Figure object
    """
    categories = ['Mood', 'Energy', 'Stress']
    scores = [mood, energy, stress]
    colors = ['#FF6B9D', '#4ECDC4', '#FFE66D']
    
    fig = go.Figure(data=[
        go.Bar(
            y=categories,
            x=scores,
            orientation='h',
            marker=dict(color=colors),
            text=scores,
            textposition='auto',
            hovertemplate='<b>%{y}</b>: %{x}/5<extra></extra>'
        )
    ])
    
    fig.update_layout(
        title="Current Scores",
        xaxis_title="Score (1-5)",
        xaxis=dict(range=[0, 5], dtick=1),
        height=250,
        template="plotly_white",
        font=dict(family="Arial, sans-serif"),
        showlegend=False
    )
    
    return fig
