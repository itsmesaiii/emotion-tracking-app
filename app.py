"""
EmotionS - Emotion Tracking Application
"""

import streamlit as st
from dotenv import load_dotenv
from ai.graph import create_emotion_graph
from utils.storage import EmotionStorage
from utils.charts import create_mood_timeline, create_emotion_donut, create_score_bars

load_dotenv()

st.set_page_config(
    page_title="EmotionS",
    page_icon="💭",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
    :root {
        --primary-color: #D4A574;
        --secondary-color: #B8956A;
        --accent-color: #E8D5B7;
    }
    
    .main-header {
        text-align: center;
        padding: 2rem 0 1rem 0;
        background: linear-gradient(135deg, #D4A574 0%, #B8956A 100%);
        border-radius: 20px;
        margin-bottom: 2rem;
        color: white;
        box-shadow: 0 8px 16px rgba(212, 165, 116, 0.3);
    }
    
    .main-header h1 {
        font-size: 3.5rem;
        margin: 0;
        font-weight: 700;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
    }
    
    .tagline {
        font-size: 1.2rem;
        opacity: 0.95;
        margin-top: 0.5rem;
    }
    
    .stButton>button {
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-weight: 600;
        background: linear-gradient(135deg, #D4A574 0%, #B8956A 100%);
        border: none;
        color: white;
        transition: all 0.3s ease;
        box-shadow: 0 4px 12px rgba(212, 165, 116, 0.3);
    }
    
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(212, 165, 116, 0.4);
    }
    
    .stTextArea textarea {
        border-radius: 15px;
        border: 2px solid #F5EBD9;
        padding: 1rem;
        font-size: 1rem;
        transition: border-color 0.3s ease;
    }
    
    .stTextArea textarea:focus {
        border-color: #D4A574;
        outline: none;
    }
    
    .result-card {
        background: linear-gradient(135deg, #FFF8F0 0%, #F5EBD9 100%);
        border-radius: 20px;
        padding: 2rem;
        margin: 1rem 0;
        border: 2px solid #E8D5B7;
        box-shadow: 0 4px 12px rgba(212, 165, 116, 0.15);
    }
    
    .result-card {
        background: rgba(255, 248, 240, 0.7); /* Translucent */
        backdrop-filter: blur(10px); /* Frosted glass effect */
        border: 1px solid rgba(232, 213, 183, 0.5);
}
    
    .emotion-badge {
        display: inline-block;
        padding: 0.75rem 2rem;
        border-radius: 30px;
        font-size: 1.8rem;
        font-weight: 700;
        background: linear-gradient(135deg, #D4A574 0%, #B8956A 100%);
        color: white;
        margin: 1rem 0;
        box-shadow: 0 4px 12px rgba(212, 165, 116, 0.4);
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    
    .keyword-tag {
        display: inline-block;
        padding: 0.5rem 1.2rem;
        margin: 0.4rem;
        border-radius: 20px;
        background: linear-gradient(135deg, #E8D5B7 0%, #D9C4A0 100%);
        color: #6B5744;
        font-weight: 600;
        font-size: 1rem;
        box-shadow: 0 2px 6px rgba(212, 165, 116, 0.3);
        transition: transform 0.2s ease;
    }
    
    .keyword-tag:hover {
        transform: translateY(-2px);
    }
    
    .stDownloadButton>button {
        border-radius: 25px;
        background: linear-gradient(135deg, #C9A882 0%, #A68B5B 100%);
        color: white;
        font-weight: 600;
        box-shadow: 0 4px 12px rgba(201, 168, 130, 0.3);
    }
    
    .stDownloadButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(201, 168, 130, 0.4);
    }
</style>
""", unsafe_allow_html=True)

if 'storage' not in st.session_state:
    st.session_state.storage = EmotionStorage()

if 'workflow' not in st.session_state:
    st.session_state.workflow = create_emotion_graph()

if 'last_result' not in st.session_state:
    st.session_state.last_result = None

st.markdown("""
<div class="main-header">
    <h1>💭 EmotionS</h1>
    <p class="tagline">Track your feelings, one moment at a time</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 📝 How are you feeling today?")
    st.markdown("Write freely about your emotions, thoughts, and experiences.")
    
    user_input = st.text_area(
        "Your thoughts...",
        height=200,
        placeholder="I'm feeling a bit overwhelmed today. Work has been really stressful and I can't seem to focus...",
        label_visibility="collapsed"
    )
    
    analyze_button = st.button("🔍 Analyze My Mood", width="stretch")
    
    if analyze_button and user_input.strip():
        with st.spinner("✨ Analyzing your emotions..."):
            try:
                initial_state = {"user_input": user_input}
                result = st.session_state.workflow.invoke(initial_state)
                
                st.session_state.storage.add_entry(
                    user_input=result["user_input"],
                    emotion=result["emotion"],
                    mood_score=result["mood_score"],
                    energy_score=result["energy_score"],
                    stress_score=result["stress_score"],
                    keywords=result["keywords"],
                    reflection=result["reflection"]
                )
                
                st.session_state.last_result = result
                st.success("✅ Analysis complete!")
                st.rerun()
                
            except Exception as e:
                st.error(f"❌ Error during analysis: {str(e)}")
                st.info("💡 Make sure your GROQ_API_KEY is set in the .env file")
    
    elif analyze_button:
        st.warning("⚠️ Please write something before analyzing!")

with col2:
    st.markdown("### 🎯 Your Emotional Snapshot")
    
    if st.session_state.last_result:
        result = st.session_state.last_result
        
        st.markdown(f"""
        <div class="result-card">
            <h4 style="margin-top:0;">Detected Emotion</h4>
            <div class="emotion-badge">{result['emotion']}</div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("#### 📊 Emotional Scores")
        fig_scores = create_score_bars(
            result['mood_score'],
            result['energy_score'],
            result['stress_score']
        )
        st.plotly_chart(fig_scores, width="stretch")
        
        st.markdown("#### 🏷️ Emotional Keywords")
        keywords_html = "".join([f'<span class="keyword-tag">{kw}</span>' for kw in result['keywords']])
        st.markdown(keywords_html, unsafe_allow_html=True)
        
        st.markdown("#### 💬 Supportive Message")
        st.info(result['reflection'])
        
    else:
        st.info("👈 Enter your thoughts and click 'Analyze My Mood' to get started!")

st.markdown("---")
st.markdown("## 📈 Your Emotion Analytics")

if st.session_state.storage.get_entry_count() > 0:
    st.markdown("### 💡 Insights")
    st.markdown(st.session_state.storage.get_insights())
    
    chart_col1, chart_col2 = st.columns(2)
    
    with chart_col1:
        st.markdown("#### Mood Timeline")
        mood_data = st.session_state.storage.get_mood_timeline()
        fig_timeline = create_mood_timeline(mood_data)
        st.plotly_chart(fig_timeline, width="stretch")
    
    with chart_col2:
        st.markdown("#### Emotion Distribution")
        emotion_counts = st.session_state.storage.get_emotion_counts()
        fig_donut = create_emotion_donut(emotion_counts)
        st.plotly_chart(fig_donut, width="stretch")
    
    st.markdown("### 💾 Export Your Data")
    json_data = st.session_state.storage.export_to_json()
    st.download_button(
        label="📥 Download Data as JSON",
        data=json_data,
        file_name="journal-entries.json",
        mime="application/json",
        width="stretch"
    )
    
else:
    st.info("📊 Start tracking your emotions to see analytics and insights!")

st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #999; padding: 1rem;">
    <p>Made with 💜 using Streamlit, Groq AI, and LangGraph</p>
    <p style="font-size: 0.9rem;">Your data is stored locally in memory and never sent anywhere except to Groq for analysis.</p>
</div>
""", unsafe_allow_html=True)
