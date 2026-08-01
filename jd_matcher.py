import os
from dotenv import load_dotenv
from google import genai
from prompts import PROMPT_TEMPLATE

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def analyze_resume(resume_text, job_description):
    prompt = PROMPT_TEMPLATE.format(
        resume_text=resume_text,
        job_description=job_description
    )

    response = client.models.generate_content(
        model="gemini-3.1-flash-lite-preview",
        contents=prompt
    )

    return response.text