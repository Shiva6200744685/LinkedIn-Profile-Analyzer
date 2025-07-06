# 🧠 LinkedIn Profile Analyzer

AI-powered LinkedIn profile analysis tool that provides career insights, profile scoring, and improvement recommendations using Google Gemini AI, spaCy, and NLTK.

## ✨ Features

- **📄 Multiple Input Methods** - Text paste, PDF upload, LinkedIn URL
- **🧠 Advanced NLP Analysis** - spaCy + NLTK for keyword extraction
- **🤖 Gemini AI Integration** - Career insights and improvement suggestions
- **📊 Profile Scoring** - Comprehensive 0-100 scoring algorithm
- **🎯 Career Suggestions** - Job role recommendations based on skills
- **💡 Improvement Tips** - Actionable profile optimization advice
- **📈 Skills Detection** - Technical and soft skills identification

## 🚀 Quick Start

### Installation

```bash
# Clone or download the project
git clone <repository-url>
cd SMARRTIF-AI

# Install dependencies
pip install -r requirements_nlp.txt

# Download spaCy model
python -m spacy download en_core_web_sm

# Install additional packages
pip install google-generativeai PyPDF2
```

### Run the Application

```bash
streamlit run linkedin_analyzer_complete.py
```

Open your browser and navigate to `http://localhost:8501`

## 📋 How to Use

### 1. Choose Input Method
- **Paste Text** - Copy LinkedIn profile content manually
- **Upload PDF** - Export LinkedIn profile as PDF and upload
- **LinkedIn URL** - Enter profile URL (manual extraction required)

### 2. Get Your LinkedIn Content
**PDF Method (Recommended):**
1. Go to your LinkedIn profile
2. Click "More" → "Save to PDF"
3. Upload the PDF file

**Manual Method:**
1. Copy About/Summary section
2. Copy Experience descriptions
3. Copy Skills list
4. Paste everything in the text area

### 3. Analyze Profile
- Click "🔍 Analyze Profile"
- Review your profile score and insights
- Get AI-powered career suggestions
- Follow improvement recommendations

## 🔧 Technical Details

### Architecture
- **Frontend**: Streamlit web interface
- **NLP Processing**: spaCy + NLTK for text analysis
- **AI Engine**: Google Gemini 1.5 Flash
- **PDF Processing**: PyPDF2 for text extraction

### Analysis Components
1. **Keyword Extraction** - Technical terms prioritization
2. **Skills Matching** - Against 16+ professional skills database
3. **Entity Recognition** - Organizations, products, people
4. **Profile Scoring** - Multi-factor algorithm:
   - Text length (0-25 points)
   - Skills coverage (0-35 points)
   - Keyword diversity (0-20 points)
   - Professional terms (0-20 points)

### AI Features
- **Career Role Suggestions** - Top 3 suitable positions
- **Improvement Tips** - Recruiter visibility enhancements
- **Missing Skills Analysis** - Career growth recommendations
- **Industry Trends** - Market insights and advice

## 📦 Dependencies

```
streamlit>=1.28.0
nltk>=3.8.0
spacy>=3.6.0
google-generativeai>=0.3.0
PyPDF2>=3.0.0
python-dotenv>=1.0.0
```

## 🔑 API Configuration

The application uses Google Gemini AI with a pre-configured API key. For production use, consider:

1. Setting up your own Gemini API key
2. Using environment variables for security
3. Implementing rate limiting

## 📊 Sample Output

```
Profile Score: 85/100
Skills Detected: Python, JavaScript, AWS, Leadership, Project Management
Career Roles: Software Developer, Data Scientist, Project Manager
```

## 🛠️ Troubleshooting

### Common Issues

**spaCy Model Error:**
```bash
python -m spacy download en_core_web_sm
```

**PDF Upload Issues:**
```bash
pip install PyPDF2 --upgrade
```

**Gemini API Errors:**
```bash
pip install google-generativeai --upgrade
```

### Performance Tips
- Use PDF upload for best text extraction
- Include complete LinkedIn sections for accurate analysis
- Add quantified achievements for higher scores

## 📁 Project Structure

```
SMARRTIF AI/
├── main.py    # Main application
├── requirements.txt             # Dependencies
├── api_test.py                      # Gemini API test
├── README.md                        # This file
└── .gitignore                       # Git ignore rules
```

## 🎯 Use Cases

- **Job Seekers** - Optimize LinkedIn profiles for better visibility
- **Career Coaches** - Analyze client profiles and provide recommendations
- **Recruiters** - Quickly assess candidate profiles
- **Students** - Improve professional online presence

## 🔮 Future Enhancements

- [ ] Multiple AI model support (OpenAI, Claude)
- [ ] Batch profile analysis
- [ ] Industry-specific skill databases
- [ ] Profile comparison features
- [ ] Export to multiple formats

## 📄 License

This project is developed for the SMARRTIF AI assignment.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📞 Support

For issues or questions:
1. Check the troubleshooting section
2. Review dependencies and installation
3. Test with the sample profile

---

**Built with ❤️ using Streamlit, spaCy, NLTK, and Google Gemini AI**