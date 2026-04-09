# hireme-ai-job-copilot# HireBot - AI Job Copilot

**HireBot** is an AI-powered web app designed to help job seekers:

- Find job openings relevant to their uploaded resume
- Generate **tailored resumes** optimized for each job
- Get **career guidance** and a **study roadmap** for target roles through an interactive chatbot

---

## IMAGES
<img width="1901" height="878" alt="image" src="https://github.com/user-attachments/assets/48c23e36-28ae-4868-8d8b-a5c237c7a2d4" />

<img width="1912" height="696" alt="image" src="https://github.com/user-attachments/assets/8d484e51-5829-4d4e-b15f-fa8f9055476d" />

<img width="1884" height="889" alt="image" src="https://github.com/user-attachments/assets/115c9df4-b9bc-4349-b107-f9104259c0a0" />



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
