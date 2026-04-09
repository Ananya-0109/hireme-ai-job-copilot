

from groq import Groq
import os
from dotenv import load_dotenv

# ---------------------------
# Load environment variables
# ---------------------------
load_dotenv()

# Get API key securely
groq_api_key = os.getenv("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")

# ---------------------------
# Groq-based Tailored Resume
# ---------------------------
client = Groq(api_key=groq_api_key)

def generate_tailored_resume(resume_text, job_desc):
    prompt = f"""
Rewrite this resume to better match the job description.

- Add relevant keywords
- Improve bullet points
- Keep it realistic
- Do NOT add fake experience

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_desc}
"""
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"