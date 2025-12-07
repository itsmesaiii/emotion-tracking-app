# EmotionS - Emotion Tracking App

**Track your feelings, one moment at a time** 💭

**🌐 [Live Demo](https://emotion-tracking-app.streamlit.app/)** | AI-powered emotion journal using Groq AI and LangGraph.

## Features

- 🎨 Clean beige/tan aesthetic
- 🤖 AI emotion detection (Groq Llama 3.1)
- 📊 Interactive mood charts
- 🚨 Crisis detection with helpline numbers
- 💾 Export data as JSON

## Quick Start

**1. Install**
```bash
pip install -r requirements.txt
```

**2. Get Groq API Key**
- Go to https://console.groq.com/keys
- Sign up (free)
- Create API key

**3. Create `.env` file**
```env
GROQ_API_KEY=your_key_here
```

**4. Run**
```bash
streamlit run app.py
```

## What It Does

Analyzes your thoughts through 4 steps:
1. Detects emotion (Happy, Sad, Angry, Anxious, Stressed, Tired, Excited, Lonely)
2. Scores mood, energy, stress (1-5)
3. Extracts emotional keywords
4. Generates supportive message


## Troubleshooting

**API Key Error**: Check `.env` file exists with correct key
**Import Error**: Run `pip install -r requirements.txt --upgrade`

---

Made with 💜 using Streamlit, Groq AI, LangGraph, and Plotly
