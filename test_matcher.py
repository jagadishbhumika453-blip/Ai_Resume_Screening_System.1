from jd_matcher import analyze_resume

resume = """
BCA Student
Skills: Python, Flask, SQL
Projects:
- AI Resume Screening System
"""

job_description = """
Looking for a Python Developer.

Required Skills:
- Python
- Flask
- SQL
- Git
"""

result = analyze_resume(resume, job_description)

print(result)