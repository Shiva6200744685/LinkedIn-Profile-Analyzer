import streamlit as st
import re
import os
from collections import Counter
import nltk
import spacy

# Download NLTK data
try:
    nltk.download('punkt', quiet=True)
    nltk.download('stopwords', quiet=True)
    nltk.download('averaged_perceptron_tagger', quiet=True)
except:
    pass

# Load spaCy model
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    st.error("Install spaCy model: python -m spacy download en_core_web_sm")
    st.stop()

# Gemini AI setup
try:
    import google.generativeai as genai
    genai.configure(api_key="AIzaSyCIYTx2zPmnJHc3wN36akGCN1FDMkjPsoA")
    model = genai.GenerativeModel("gemini-1.5-flash")
    AI_ENABLED = True
except:
    AI_ENABLED = False

# Setup
st.set_page_config(page_title="LinkedIn Profile Analyzer", page_icon="🧠")
st.title("🧠 LinkedIn Profile Analyzer")
st.markdown("### AI-powered career insights with NLP analysis")

# Status indicators
col1, col2, col3 = st.columns(3)
with col1:
    if AI_ENABLED:
        st.success("🤖 Gemini AI Enabled")
    else:
        st.warning("🤖 AI Disabled")
with col2:
    st.info("🧠 spaCy + NLTK")
with col3:
    st.info("📄 PDF Support")

# Input
input_type = st.radio("Input Method:", ["Paste Text", "Upload PDF", "LinkedIn URL"])

profile_text = ""

if input_type == "Upload PDF":
    st.info("📄 Export your LinkedIn profile: Profile → More → Save to PDF")
    uploaded_file = st.file_uploader("Upload LinkedIn Profile PDF:", type="pdf", help="Upload the PDF file exported from your LinkedIn profile")
    if uploaded_file:
        try:
            try:
                import PyPDF2
            except ImportError:
                import subprocess
                import sys
                subprocess.check_call([sys.executable, "-m", "pip", "install", "PyPDF2"])
                import PyPDF2
            
            pdf_reader = PyPDF2.PdfReader(uploaded_file)
            pdf_text = ""
            for page in pdf_reader.pages:
                pdf_text += page.extract_text() + "\n"
            profile_text = pdf_text.strip()
            if profile_text:
                st.success("✅ PDF text extracted successfully!")
                st.text_area("Extracted PDF Content:", value=profile_text, height=200)
            else:
                st.warning("⚠️ No text found in PDF. Try a different file.")
        except Exception as e:
            st.error(f"❌ PDF processing failed: {str(e)}")
            st.info("💡 Try restarting the app or use manual text input")
elif input_type == "LinkedIn URL":
    url = st.text_input("LinkedIn Profile URL:")
    st.info("💡 LinkedIn blocks scraping. Copy profile text manually.")
    profile_text = st.text_area("LinkedIn Profile Content:", height=300)
else:
    profile_text = st.text_area("LinkedIn Profile Content:", height=300)

def analyze_profile(text):
    if not text:
        return {}, [], 0, [], []
    
    # Use spaCy for NLP processing
    doc = nlp(text)
    
    # Extract entities and technical terms
    entities = [ent.text.lower() for ent in doc.ents if ent.label_ in ["ORG", "PRODUCT", "PERSON"]]
    
    # Use NLTK for tokenization and POS tagging
    from nltk.corpus import stopwords
    from nltk.tokenize import word_tokenize
    
    try:
        stop_words = set(stopwords.words('english'))
    except:
        stop_words = {'the', 'and', 'for', 'are', 'but', 'not', 'you', 'all', 'can', 'had', 'her', 'was', 'one', 'our', 'out', 'day', 'get', 'has', 'him', 'his', 'how', 'man', 'new', 'now', 'old', 'see', 'two', 'way', 'who', 'boy', 'did', 'its', 'let', 'put', 'say', 'she', 'too', 'use', 'that', 'have', 'with', 'this', 'will', 'from', 'they', 'know', 'want', 'been', 'good', 'much', 'some', 'time', 'very', 'when', 'come', 'here', 'just', 'like', 'long', 'make', 'many', 'over', 'such', 'take', 'than', 'them', 'well', 'were', 'what', 'your'}
    
    # Extract meaningful tokens using spaCy
    meaningful_tokens = [token.lemma_.lower() for token in doc 
                        if token.is_alpha and not token.is_stop and len(token.text) > 2]
    
    # Extract noun phrases for skills
    noun_phrases = [chunk.text.lower() for chunk in doc.noun_chunks if len(chunk.text.split()) <= 3]
    
    # Technical terms database
    tech_terms = {'python', 'java', 'javascript', 'react', 'nodejs', 'aws', 'azure', 'docker', 'sql', 'mongodb', 'git', 'machine learning', 'data science', 'analytics', 'tensorflow', 'pytorch', 'kubernetes', 'devops', 'agile', 'scrum', 'artificial intelligence', 'deep learning'}
    
    # Combine all extracted terms
    all_terms = meaningful_tokens + noun_phrases + entities
    
    # Filter for technical keywords
    tech_keywords = [term for term in all_terms if any(tech in term for tech in tech_terms)]
    other_keywords = [term for term in meaningful_tokens if term not in stop_words and len(term) > 3]
    
    # Prioritize technical terms
    keywords = tech_keywords + other_keywords
    keyword_freq = Counter(keywords)
    top_keywords = [word.title() for word, _ in keyword_freq.most_common(10)]
    
    # Enhanced skills detection using spaCy entities and patterns
    skills_db = ["python", "java", "javascript", "sql", "react", "aws", "machine learning", "data science", "project management", "leadership", "communication", "teamwork", "agile", "scrum", "docker", "kubernetes"]
    
    # Use both exact matching and spaCy similarity
    matched_skills = []
    text_lower = text.lower()
    
    for skill in skills_db:
        if skill in text_lower:
            matched_skills.append(skill.title())
    
    # Remove duplicates
    matched_skills = list(set(matched_skills))
    
    # Score calculation
    score = min(100, len(text.split()) // 10 + len(matched_skills) * 5 + len(set(keywords)) // 5)
    
    # Suggestions
    tips = []
    if len(text.split()) < 100: tips.append("Add more content")
    if len(matched_skills) < 3: tips.append("Include more skills")
    if not any(w in text.lower() for w in ["achieved", "led", "improved"]): tips.append("Add achievements")
    
    # Career roles
    roles = []
    if any(s in text.lower() for s in ["python", "java", "javascript"]): roles.append("Software Developer")
    if any(s in text.lower() for s in ["data", "machine learning"]): roles.append("Data Scientist")
    if any(s in text.lower() for s in ["management", "leadership"]): roles.append("Project Manager")
    
    return keyword_freq, matched_skills, score, tips, roles

# Analysis
if st.button("🔍 Analyze Profile"):
    if profile_text:
        keyword_freq, skills, score, tips, roles = analyze_profile(profile_text)
        
        # Results
        col1, col2, col3 = st.columns(3)
        with col1: st.metric("Score", f"{score}/100")
        with col2: st.metric("Skills", len(skills))
        with col3: st.metric("Words", len(profile_text.split()))
        
        # Keywords
        st.subheader("🔑 Keywords")
        keywords = [word.title() for word, _ in keyword_freq.most_common(8)]
        st.write(", ".join(keywords) if keywords else "No technical keywords found")
        
        # Skills
        st.subheader("✅ Skills")
        st.write(", ".join(skills) if skills else "No specific skills detected")
        
        # Career insights
        st.subheader("🎯 Career Roles")
        for role in roles: st.write(f"• {role}")
        if not roles: st.write("• Add more skills for suggestions")
        
        # Improvement tips
        st.subheader("💡 Tips")
        for tip in tips: st.write(f"• {tip}")
        if not tips: st.write("• Profile looks good!")
        
        # AI insights with Gemini
        if AI_ENABLED:
            with st.spinner("Getting Gemini AI insights..."):
                try:
                    prompt = f"""Analyze this LinkedIn profile and provide:
                    1. Top 3 suitable career roles based on skills and experience
                    2. Specific improvement suggestions for better recruiter visibility
                    3. Missing skills that would enhance career prospects
                    4. Industry trends relevant to this profile
                    
                    Profile content: {profile_text[:1500]}
                    Detected skills: {', '.join(skills)}
                    
                    Provide actionable, specific advice in a professional tone."""
                    
                    response = model.generate_content(prompt)
                    st.subheader("🤖 Gemini AI Career Insights")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"AI analysis failed: {str(e)}")
                    st.info("💡 Check your internet connection")
    else:
        st.warning("Enter profile content")

# Instructions and Sample
st.markdown("---")
st.markdown("### 📋 How to Get Your LinkedIn Profile")

with st.expander("📄 PDF Export Method (Recommended)"):
    st.markdown("""
    1. Go to your LinkedIn profile
    2. Click **"More"** button (three dots)
    3. Select **"Save to PDF"**
    4. Upload the downloaded PDF file above
    """)

with st.expander("📝 Manual Copy Method"):
    st.markdown("""
    1. Go to your LinkedIn profile
    2. Copy your About/Summary section
    3. Copy your Experience descriptions
    4. Copy your Skills list
    5. Paste everything in the text area
    """)

if st.button("📄 Load Sample Profile"):
    sample = """John Smith - Senior Software Engineer
5+ years Python, JavaScript, React development. Led team of 5, improved performance 40%.
Skills: Python, AWS, Machine Learning, Leadership, Project Management
Built scalable applications, managed CI/CD pipelines."""
    st.text_area("Sample Profile:", value=sample, height=100)
    st.info("💡 Copy this sample to test the analyzer!")