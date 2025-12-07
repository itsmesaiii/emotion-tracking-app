"""
In-memory storage for emotion journal entries
Provides functionality to store entries and export as JSON
"""

import json
from datetime import datetime
from typing import List, Dict, Any


class EmotionStorage:
    """Manages in-memory storage of emotion journal entries"""
    
    def __init__(self):
        """Initialize empty storage"""
        self.entries: List[Dict[str, Any]] = []
    
    def add_entry(self, user_input: str, emotion: str, mood_score: int, 
                  energy_score: int, stress_score: int, keywords: List[str], 
                  reflection: str) -> None:
        """
        Add a new emotion journal entry
        
        Args:
            user_input: Original user text
            emotion: Detected primary emotion
            mood_score: Mood rating (1-5)
            energy_score: Energy rating (1-5)
            stress_score: Stress rating (1-5)
            keywords: List of emotional keywords
            reflection: AI-generated supportive message
        """
        entry = {
            "timestamp": datetime.now().isoformat(),
            "user_input": user_input,
            "emotion": emotion,
            "mood_score": mood_score,
            "energy_score": energy_score,
            "stress_score": stress_score,
            "keywords": keywords,
            "reflection": reflection
        }
        self.entries.append(entry)
    
    def get_all_entries(self) -> List[Dict[str, Any]]:
        """
        Get all stored entries
        
        Returns:
            List of all journal entries
        """
        return self.entries
    
    def get_entry_count(self) -> int:
        """
        Get total number of entries
        
        Returns:
            Count of entries
        """
        return len(self.entries)
    
    def export_to_json(self) -> str:
        """
        Export all entries to JSON string
        
        Returns:
            JSON string of all entries
        """
        return json.dumps(self.entries, indent=2, ensure_ascii=False)
    
    def get_emotion_counts(self) -> Dict[str, int]:
        """
        Get frequency count of each emotion
        
        Returns:
            Dictionary mapping emotion to count
        """
        emotion_counts = {}
        for entry in self.entries:
            emotion = entry.get("emotion", "Unknown")
            emotion_counts[emotion] = emotion_counts.get(emotion, 0) + 1
        return emotion_counts
    
    def get_mood_timeline(self) -> List[Dict[str, Any]]:
        """
        Get mood scores over time for timeline chart
        
        Returns:
            List of dicts with timestamp and mood_score
        """
        return [
            {
                "timestamp": entry["timestamp"],
                "mood_score": entry["mood_score"],
                "emotion": entry["emotion"]
            }
            for entry in self.entries
        ]
    
    def get_insights(self) -> str:
        """
        Generate text insights from stored data
        
        Returns:
            Insight text based on patterns in the data
        """
        if len(self.entries) == 0:
            return "No entries yet. Start tracking your emotions to see insights!"
        
        # Calculate average scores
        avg_mood = sum(e["mood_score"] for e in self.entries) / len(self.entries)
        avg_stress = sum(e["stress_score"] for e in self.entries) / len(self.entries)
        
        # Find most common emotion
        emotion_counts = self.get_emotion_counts()
        most_common = max(emotion_counts.items(), key=lambda x: x[1])[0] if emotion_counts else "Unknown"
        
        # Generate insight
        insights = []
        insights.append(f"You've logged {len(self.entries)} emotion entries.")
        insights.append(f"Your most common emotion is: **{most_common}**")
        insights.append(f"Average mood: **{avg_mood:.1f}/5**")
        insights.append(f"Average stress: **{avg_stress:.1f}/5**")
        
        if avg_stress > 3.5:
            insights.append("💡 Your stress levels seem elevated. Consider relaxation techniques.")
        
        return " | ".join(insights)
