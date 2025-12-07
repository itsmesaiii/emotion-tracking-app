# EmotionS - Emotion Tracking Application

![EmotionS](https://img.shields.io/badge/EmotionS-Emotion%20Tracker-D4A574?style=for-the-badge)

**Track your feelings, one moment at a time** 💭

A beautiful GenAI-powered emotion journal that helps you understand and track your emotional wellbeing using Groq AI and LangGraph.

## ✨ Features

- 🎨 **Creamy Aesthetic UI** - Warm beige/tan gradient design
- 🤖 **AI-Powered Analysis** - Uses Groq's Llama 3.1 for emotion detection
- 🔄 **LangGraph Workflow** - 4-step emotion analysis pipeline
- 📊 **Interactive Charts** - Real-time Plotly visualizations
- 💾 **Data Export** - Download journal entries as JSON
- 🔒 **Privacy First** - All data stored locally in memory
- 🚨 **Crisis Detection** - Automatic mental health resource display for suicidal thoughts

## 🎯 What It Does

EmotionS analyzes your written thoughts through a 4-step AI workflow:

1. **Emotion Detection** - Identifies primary emotion from 8 categories
2. **Score Generation** - Rates Mood, Energy, and Stress (1-5 scale)
3. **Keyword Extraction** - Finds top 3 emotional keywords
4. **Supportive Message** - Generates short, natural, friend-like validation

## 📋 Requirements

- Python 3.10+
- Groq API Key (free from [Groq Console](https://console.groq.com/keys))

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Set Up API Key

Create a `.env` file:

```env
GROQ_API_KEY=your_actual_api_key_here
```

**Get your free Groq API key:**
1. Go to https://console.groq.com/keys
2. Sign up (free, no credit card needed)
3. Click "Create API Key"
4. Copy and paste into `.env`

### 3. Run the App

```bash
streamlit run app.py
```

Opens at `http://localhost:8501`

## 📁 Project Structure

```
EmotionSApp/
│
├── app.py                     # Main Streamlit application
│
├── ai/
│   ├── graph.py               # LangGraph workflow orchestration
│   └── nodes.py               # Groq AI analysis nodes
│
├── utils/
│   ├── charts.py              # Plotly chart generation
│   └── storage.py             # In-memory storage & JSON export
│
├── requirements.txt           # Python dependencies
├── .env                       # API key (create this)
└── README.md                  # This file
```

## 🎨 Emotion Categories

- 😊 Happy
- 😢 Sad
- 😠 Angry
- 😰 Anxious
- 😫 Stressed
- 😴 Tired
- 🎉 Excited
- 😔 Lonely

## 🚨 Crisis Support

If you mention suicidal thoughts or self-harm, the app automatically displays:
- **India:** AASRA (91-9820466726), Vandrevala Foundation (1860-2662-345)
- **USA:** 988 Suicide & Crisis Lifeline
- **UK:** 116 123 (Samaritans)

## 📊 Analytics Features

- **Mood Timeline** - Track mood progression over time
- **Emotion Distribution** - Visualize emotion frequency
- **Smart Insights** - AI-generated pattern observations
- **JSON Export** - Download all entries

## 🔧 Customization

### Change AI Model

Edit `ai/nodes.py`:
```python
model="llama-3.1-8b-instant"  
# Options: llama-3.1-70b-versatile, mixtral-8x7b-32768
```

### Customize Colors

Edit `app.py` CSS (lines 22-25):
```css
:root {
    --primary-color: #D4A574;      /* Tan */
    --secondary-color: #B8956A;    /* Darker tan */
    --accent-color: #E8D5B7;       /* Light cream */
}
```

Main gradient (line 30):
```css
background: linear-gradient(135deg, #D4A574 0%, #B8956A 100%);
```

### Modify Emotions

Edit `ai/nodes.py`, function `extract_emotion()`:
```python
valid_emotions = ["Happy", "Sad", "Angry", ...]
```

## 🛠️ Troubleshooting

### API Key Issues
- Ensure `.env` file exists with `GROQ_API_KEY=your_key`
- No spaces before/after the key
- Restart app after changing `.env`

### Import Errors
```bash
pip install -r requirements.txt --upgrade
```

### Charts Not Displaying
```bash
streamlit cache clear
```

## 📝 Usage Tips

1. **Be detailed** - More context = better analysis
2. **Track regularly** - Daily entries reveal patterns
3. **Review analytics** - Check trends in the charts
4. **Export data** - Download JSON as backup

## 🌐 Deploy to Streamlit Cloud

1. Push code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect repository
4. Add secret:
   ```toml
   GROQ_API_KEY = "your_key_here"
   ```
5. Deploy!

## 🙏 Acknowledgments

- **Streamlit** - Web framework
- **Groq** - Lightning-fast AI inference
- **LangGraph** - Workflow orchestration
- **Plotly** - Interactive visualizations

---

**Made with 💜 for emotional wellbeing**

*Remember: It's okay to feel. EmotionS is here to help you understand your emotional journey.*
