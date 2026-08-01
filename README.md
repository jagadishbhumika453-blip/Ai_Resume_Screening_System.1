# AI Resume Screening System

## Project Overview

AI Resume Screening System is a web-based application that analyzes a candidate's resume against a Job Description (JD).

The system extracts text from a PDF resume and uses AI to compare the candidate's skills and experience with the requirements of the Job Description.

It generates an ATS-style analysis containing the match score, resume summary, skills found, missing skills, candidate strengths, and suggestions for improvement.

## Features

- Upload resume in PDF format
- Enter Job Description
- Extract text from resume
- Compare resume with Job Description
- Generate ATS match score
- Identify skills found
- Identify missing skills
- Generate candidate strengths
- Provide improvement suggestions
- Simple and user-friendly web interface
- AI-based resume analysis

## Technologies Used

- Python
- Flask
- Google Gemini API
- LangChain
- PyMuPDF
- HTML
- CSS
- python-dotenv

## Project Structure

```text
AI_Resume_Screening_System/
│
├── screenshots/
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── uploads/
│
├── app.py
├── jd_matcher.py
├── prompts.py
├── resume_parser.py
├── check_models.py
├── test_matcher.py
├── test_parser.py
├── requirements.txt
├── .gitignore
└── README.md
```

## How It Works

1. User uploads a PDF resume.
2. User enters the Job Description.
3. The system extracts text from the resume.
4. The extracted resume text and Job Description are sent for AI analysis.
5. The AI compares the resume with the Job Description.
6. The system generates an ATS match score.
7. The results display the resume summary, skills found, missing skills, strengths, and suggestions.

## Resume Analysis

The system provides the following analysis:

### ATS Match Score

Shows how closely the candidate's resume matches the Job Description.

### Resume Summary

Provides a short summary of the candidate's background and relevant experience.

### Skills Found

Displays the skills identified from the resume that are relevant to the Job Description.

### Missing Skills

Displays important skills required by the Job Description that are not found in the resume.

### Candidate Strengths

Highlights the candidate's relevant skills, education, projects, and experience.

### Suggestions for Improvement

Provides suggestions to improve the resume and increase its relevance to the Job Description.

## Example Output

### ATS Resume Analysis

**ATS Match Score:** 85%

### Resume Summary

- Candidate has experience in Python and AI/ML.
- Has completed relevant technical projects.

### Skills Found

- Python
- Machine Learning
- LangChain
- Flask

### Missing Skills

- SQL
- Data Analysis

### Candidate Strengths

- Relevant project experience
- Python development skills

### Suggestions for Improvement

- Improve SQL knowledge.
- Develop stronger data analysis skills.

## Installation

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd AI_Resume_Screening_System
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

### 3. Activate Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

## API Key Setup

Create a `.env` file in the project folder.

Add your Gemini API key:

```env
GEMINI_API_KEY=your_api_key_here
```

Do not share your API key or upload the `.env` file to GitHub.

## Run the Application

Start the Flask application:

```bash
python app.py
```

Open the local URL shown in the terminal.

Usually:

```text
http://127.0.0.1:5000/
```

## Testing

### Test Resume Parser

```bash
python test_parser.py
```

### Test Resume Matcher

```bash
python test_matcher.py
```

### Check Available Gemini Models

```bash
python check_models.py
```

## Screenshots

Screenshots of the application are stored in the `screenshots` folder.

The screenshots demonstrate the application interface, resume upload, Job Description input, and resume analysis results.

## Security


```text
.env
venv/
__pycache__/
*.pyc
uploads/*
```

## Future Improvements

- Support for DOCX resumes
- Improved ATS scoring
- Resume analysis report download
- Candidate comparison
- Resume improvement recommendations
- Resume analysis history
- User authentication
- Cloud deployment

## Project Goals

The main goals of this project are:

- Automate the initial resume screening process.
- Reduce the time required for manual resume comparison.
- Identify relevant candidate skills.
- Identify missing job requirements.
- Provide useful resume improvement suggestions.
- Demonstrate the use of AI in resume screening.

## Author

**Bhumika M J**



## License

This project is developed for educational and learning purposes.