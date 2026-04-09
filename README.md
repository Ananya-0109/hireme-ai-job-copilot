# hireme-ai-job-copilot# HireBot - AI Job Copilot

**HireBot** is an AI-powered web app designed to help job seekers:

- Find job openings relevant to their uploaded resume
- Generate **tailored resumes** optimized for each job
- Get **career guidance** and a **study roadmap** for target roles through an interactive chatbot

---

## 🌟 Features

1. **Resume Upload**
   - Upload PDF resumes and extract text automatically
2. **Job Matching**
   - Search and find jobs relevant to your role and experience
3. **Tailored Resume**
   - AI-generated tailored resume for each job description
   

---

## 🛠 Technologies Used

- **Backend / Logic:** Python, scikit-learn
- **Frontend:** Streamlit
- **PDF Handling:** pdfplumber
- **AI :** Placeholder functions 
- **Version Control:** Git & GitHub

---

## Project Structure
job‑copilot/
├─ app.py
├─ requirements.txt
├─ README.md
├─ utils/
│ ├─ parser.py
│ ├─ jobs_api.py
│ ├─ matcher.py
│ └─ llm.py
## 🚀 How to Run Locally

1. Clone the repository:

```bash
git clone https://github.com/Ananya-0109/hireme-ai-job-copilot.git


cd hireme-ai-job-copilot
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate      # Windows
pip install -r requirements.txt
streamlit run app.py
