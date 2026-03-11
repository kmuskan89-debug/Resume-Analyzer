# AI Resume Analyzer

A powerful web application that analyzes resumes against job descriptions using natural language processing and machine learning. Upload your resume, paste a job description, and get instant feedback on your match score, identified skills, missing competencies, and personalized recommendations.

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red?style=flat&logo=streamlit)
![spaCy](https://img.shields.io/badge/spaCy-3.x-green?style=flat)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## Features

### Core Functionality
- ** Multi-Format Support** - Upload and parse PDF and DOCX resume files
- ** Match Scoring** - Calculate resume-job compatibility using TF-IDF and cosine similarity
- ** Skills Extraction** - Automatically identify technical skills from resume text using NLP
- ** Missing Skills Analysis** - Identify gaps between your skills and job requirements
- ** Smart Suggestions** - Get actionable recommendations to improve your resume

### Advanced Features
- ** Job Role Detection** - Automatically detect job roles from job descriptions
- ** Role-Based Analysis** - Specialized analysis for roles including:
  - White Hat Hacker / Ethical Hacker
  - Web Developer
  - Full Stack Developer
  - Data Scientist
  - AI Engineer
  - Software Engineer
  - DevOps Engineer
  - Data Analyst
  - Cybersecurity Specialist

## Quick Start

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/resume-analyzer.git
cd resume-analyzer
```

2. **Create a virtual environment (recommended)**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Download spaCy model**
```bash
python -m spacy download en_core_web_sm
```

### Running the Application

```bash
streamlit run app.py
```

The application will open in your browser at `http://localhost:8501`

## Usage

1. **Upload Resume** - Click the file uploader and select your resume (PDF or DOCX format)
2. **Paste Job Description** - Copy and paste the job description into the text area
3. **Analyze** - Click the "Analyze Resume" button
4. **Review Results** - View your match score, skills analysis, and recommendations

## Project Structure

```
Resume Analyzer/
├── app.py                  # Streamlit web application
├── resume_extractor.py     # Core extraction and analysis module
├── requirements.txt        # Python dependencies
├── .gitignore             # Git ignore file
└── README.md              # This file
```

## Technology Stack

| Component | Technology |
|-----------|------------|
| Frontend | Streamlit |
| NLP Processing | spaCy |
| Machine Learning | scikit-learn (TF-IDF, Cosine Similarity) |
| PDF Parsing | PyPDF2 |
| DOCX Parsing | python-docx |
| Language | Python |

## Dependencies

```
streamlit>=1.28.0
PyPDF2>=3.0.0
python-docx>=1.1.0
spacy>=3.7.0
scikit-learn>=1.3.0
```

## Configuration

### Supported Skills Categories

The analyzer recognizes skills across multiple categories:

- **Programming Languages**: Python, Java, C++, JavaScript, TypeScript, Ruby, Go, Rust, etc.
- **Web Development**: React, Angular, Vue, Node.js, Django, Flask, etc.
- **Databases**: SQL, MySQL, PostgreSQL, MongoDB, Redis, etc.
- **Data Science & ML**: TensorFlow, PyTorch, Pandas, NumPy, scikit-learn, etc.
- **Cloud & DevOps**: AWS, Azure, GCP, Docker, Kubernetes, Jenkins, etc.
- **Security**: Cybersecurity, Penetration Testing, OWASP, etc.

### Customizing Skills List

Edit the `SKILLS_LIST` in `resume_extractor.py` to add or modify recognized skills.

## How It Works

### 1. Text Extraction
- Reads PDF files using PyPDF2
- Reads DOCX files using python-docx
- Cleans and normalizes extracted text

### 2. Skills Extraction
- Uses spaCy NLP for phrase matching
- Performs case-insensitive matching with word boundaries
- Cross-references against a predefined skills database

### 3. Match Score Calculation
- Applies TF-IDF vectorization to both resume and job description
- Calculates cosine similarity between vectors
- Returns a percentage score (0-100%)

### 4. Role Detection
- Analyzes job description for role-specific keywords
- Matches against predefined role templates
- Provides confidence score for detection

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Streamlit](https://streamlit.io/) - For the amazing web framework
- [spaCy](https://spacy.io/) - For industrial-strength NLP
- [scikit-learn](https://scikit-learn.org/) - For ML algorithms

##  Sample Output

```
Analysis Results
Match Score: 75% - Great Match!

Your Skills
✓ python ✓ machine learning ✓ tensorflow ✓ sql ✓ docker

Missing Skills
✗ kubernetes ✗ aws ✗ redis

Suggestions
1. Your resume has a strong match! Consider highlighting your relevant experience more prominently.
2. Consider adding these skills to your resume: kubernetes, aws, and 1 more
3. Tailor your resume's keywords to match the job description more closely for better ATS compatibility.

Role-Based Analysis: Data Scientist
Role Match: 80% - Excellent!
```

---

<p align="center">Made for job seekers everywhere</p>

