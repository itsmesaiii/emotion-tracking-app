"""
AI nodes for emotion analysis using Groq API
"""

from groq import Groq
import os
import re
from typing import Dict, Any
from dotenv import load_dotenv

load_dotenv()

def get_groq_client():
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key or api_key == "YOUR_GROQ_API_KEY_HERE":
        raise ValueError("GROQ_API_KEY not found in environment variables")
    return Groq(api_key=api_key)


def extract_emotion(state: Dict[str, Any]) -> Dict[str, Any]:
    user_input = state.get("user_input", "")
    
    prompt = f"""Analyze this text and pick ONE emotion from: Happy, Sad, Angry, Anxious, Stressed, Tired, Excited, Lonely

Text: "{user_input}"

Respond with ONLY the emotion word."""
    
    try:
        client = get_groq_client()
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.1-8b-instant",
            temperature=0.3,
            max_tokens=10
        )
        emotion = response.choices[0].message.content.strip()
        
        valid_emotions = ["Happy", "Sad", "Angry", "Anxious", "Stressed", "Tired", "Excited", "Lonely"]
        if emotion not in valid_emotions:
            emotion_lower = emotion.lower()
            for valid in valid_emotions:
                if valid.lower() in emotion_lower:
                    emotion = valid
                    break
            else:
                emotion = "Anxious"
            
        state["emotion"] = emotion
    except Exception as e:
        print(f"Error: {e}")
        state["emotion"] = "Anxious"
    
    return state


def generate_scores(state: Dict[str, Any]) -> Dict[str, Any]:
    user_input = state.get("user_input", "")
    
    prompt = f"""Rate this on 1-5 scale:

"{user_input}"

Format:
Mood: X
Energy: Y  
Stress: Z"""
    
    try:
        client = get_groq_client()
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.1-8b-instant",
            temperature=0.3,
            max_tokens=50
        )
        text = response.choices[0].message.content.strip()
        
        mood_match = re.search(r'Mood:\s*(\d)', text)
        energy_match = re.search(r'Energy:\s*(\d)', text)
        stress_match = re.search(r'Stress:\s*(\d)', text)
        
        state["mood_score"] = int(mood_match.group(1)) if mood_match else 3
        state["energy_score"] = int(energy_match.group(1)) if energy_match else 3
        state["stress_score"] = int(stress_match.group(1)) if stress_match else 3
        
    except Exception as e:
        print(f"Error: {e}")
        state["mood_score"] = 3
        state["energy_score"] = 3
        state["stress_score"] = 3
    
    return state


def extract_keywords(state: Dict[str, Any]) -> Dict[str, Any]:
    user_input = state.get("user_input", "")
    
    prompt = f"""Extract 3 emotional keywords from: "{user_input}"

Format: word1, word2, word3"""
    
    try:
        client = get_groq_client()
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.1-8b-instant",
            temperature=0.5,
            max_tokens=30
        )
        keywords_text = response.choices[0].message.content.strip()
        keywords = [kw.strip() for kw in keywords_text.split(',')][:3]
        
        while len(keywords) < 3:
            keywords.append("reflective")
            
        state["keywords"] = keywords[:3]
        
    except Exception as e:
        print(f"Error: {e}")
        state["keywords"] = ["thoughtful", "reflective", "aware"]
    
    return state


def generate_reflection(state: Dict[str, Any]) -> Dict[str, Any]:
    user_input = state.get("user_input", "")
    
    crisis_keywords = ['suicide', 'suicidal', 'kill myself', 'end it all', 'want to die', 'self-harm', 'hurt myself']
    is_crisis = any(keyword in user_input.lower() for keyword in crisis_keywords)
    
    if is_crisis:
        state["reflection"] = """🚨 If you're having thoughts of suicide or self-harm, please reach out immediately:

**India:** AASRA 91-9820466726 (24/7) | Vandrevala 1860-2662-345 (24/7)
**USA:** 988 | **UK:** 116 123

You don't have to face this alone."""
        return state
    
    prompt = f"""
    You are a supportive friend, not a therapist.
    The user wrote: "{user_input}"

    Write a warm reply that:
    - Validates their feelings clearly
    - Reflects the emotion they expressed using their OWN wording
    - Offers one gentle, universal coping idea (e.g., take a short break, drink water, breathe, write thoughts down, stretch)
    - Encourages self-kindness
    - NEVER diagnose or mention disorders
    - NEVER assume trauma or deep personal history
    - NEVER minimize feelings or say "you'll be fine"
    - Avoid commands like "you should" or "stop worrying"
    - Maximum 3 short sentences, friendly and natural tone

    Good examples:
    - "It makes sense you'd feel overwhelmed with all that happening. Maybe a tiny break or a deep breath could help clear your head. You deserve a little kindness toward yourself today."
    - "Feeling disconnected can be really tough. Doing something small you enjoy might lift you a bit. Take a moment for yourself if you can."

    Your response:
    """

    
    try:
        client = get_groq_client()
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.1-8b-instant",
            temperature=0.7,
            max_tokens=50
        )
        reflection = response.choices[0].message.content.strip().strip('"')
        state["reflection"] = reflection
        
    except Exception as e:
        print(f"Error: {e}")
        state["reflection"] = "That sounds tough. Thanks for sharing."
    
    return state
