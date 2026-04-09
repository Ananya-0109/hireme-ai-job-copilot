# utils/llm.py

from groq import Groq
import os

# ---------------------------
# Groq-based Tailored Resume
# ---------------------------
client = Groq(api_key="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")

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
            model="llama-3.3-70b-versatile",  # ✅ Fixed model
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"

# ---------------------------
# Chatbot: Recommend Skills
# ---------------------------
def recommend_skills(role):
    """
    Returns recommended skills/topics for a given role.
    Replace with AI calls if needed.
    """
    skills_dict = {
        "Data Analyst": "- Python\n- SQL\n- Excel\n- Tableau\n- Statistics\n- Power BI",
        "Software Engineer": "- Python/Java\n- Algorithms\n- Data Structures\n- Git\n- REST APIs",
        "Data Scientist": "- Python\n- Machine Learning\n- Statistics\n- Pandas\n- Scikit-learn\n- SQL",
        "Product Manager": "- Agile/Scrum\n- Product Roadmap\n- Market Research\n- Jira\n- Communication Skills"
    }
    return skills_dict.get(role, "- Research skills and domain knowledge for this role")

# ---------------------------
# Chatbot: Resume Analysis
# ---------------------------
def analyze_resume(resume_text, role):
    """
    Returns feedback on resume for a target role.
    """
    roadmap = recommend_skills(role)
    feedback = f"Resume Analysis for {role}:\n\n" \
               f"- Ensure you mention these skills:\n{roadmap}\n" \
               "- Highlight relevant projects, achievements, and experience.\n" \
               "- Tailor keywords to match the job description."
    return feedback