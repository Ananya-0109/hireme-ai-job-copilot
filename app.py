import streamlit as st
from utils.parser import extract_text_from_pdf
from utils.jobs_api import fetch_jobs
from utils.matcher import match_jobs
from utils.llm import generate_tailored_resume

# 🔥 Page Config
st.set_page_config(page_title="HireMe", page_icon="🤖", layout="wide")

# 🔥 Custom Styling
st.markdown("""
<style>
/* Background & typography */
body {
    background-color: #0f172a;
    color: #f1f5f9;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
h1, h2, h3, h4, h5 {
    color: #f8fafc;
}

/* Buttons */
.stButton>button {
    border-radius: 12px;
    padding: 10px 25px;
    font-weight: 600;
    background: linear-gradient(90deg, #2563eb, #60a5fa);
    color: white;
    border: none;
    transition: 0.3s;
}
.stButton>button:hover {
    background: linear-gradient(90deg, #1d4ed8, #3b82f6);
}

/* Job Card */
.job-card {
    padding: 20px;
    border-radius: 14px;
    background-color: #1e293b;
    margin-bottom: 20px;
    transition: 0.3s;
    border-left: 6px solid #60a5fa;
}
.job-card:hover {
    background-color: #334155;
    transform: scale(1.02);
}
.job-badge {
    display: inline-block;
    padding: 3px 10px;
    border-radius: 8px;
    background-color: #2563eb;
    color: white;
    font-size: 12px;
    margin-right: 5px;
}

/* Links */
a {
    color: #60a5fa;
    text-decoration: none;
    font-weight: bold;
}
a:hover {
    text-decoration: underline;
}

/* Tailored Resume Area */
.stTextArea textarea {
    background-color: #1e293b;
    color: #f1f5f9;
    border-radius: 10px;
    padding: 10px;
    font-family: 'Courier New', monospace;
}

/* Columns spacing */
.css-1d391kg {
    gap: 20px;
}
</style>
""", unsafe_allow_html=True)

# 🔹 Title
st.markdown("<h1 style='color:#60a5fa;'>🤖 HireMe</h1>", unsafe_allow_html=True)
st.markdown("<p style='color:#cbd5e1; font-size:16px;'>Find jobs and generate tailored resumes instantly</p>", unsafe_allow_html=True)

# 📂 Upload Section
st.subheader("Upload Your Resume")
uploaded_file = st.file_uploader("", type=["pdf"])

if uploaded_file:
    resume_text = extract_text_from_pdf(uploaded_file)

    # 🔹 Input Columns
    col1, col2 = st.columns(2)
    with col1:
        role = st.text_input("Desired Job Role", "")  # Empty by default
    with col2:
        experience_options = ["Select experience", "Fresher", "0-1 years", "1-2 years", "3-5 years", "5+ years"]
        experience = st.selectbox("Experience Level", experience_options, index=0)

    # Session state initialization
    if "jobs" not in st.session_state:
        st.session_state.jobs = []
    if "tailored" not in st.session_state:
        st.session_state.tailored = {}

    # 🔍 Find Jobs Button
    if st.button("🔍 Find Jobs"):
        if not role or experience == "Select experience":
            st.warning("Please fill in all fields before searching.")
        else:
            with st.spinner("Fetching jobs..."):
                jobs = fetch_jobs(role, experience=experience)  # Location removed
                if jobs:
                    st.session_state.jobs = match_jobs(resume_text, jobs)
                    st.success(f"✅ Found {len(jobs)} jobs")
                else:
                    st.warning("No jobs found")

    # 📋 Display Jobs
    if st.session_state.jobs:
        st.subheader("💼 Top Job Matches")
        for i, job in enumerate(st.session_state.jobs[:5]):
            # Job badges for experience (location removed)
            badges = f"<span class='job-badge'>{job.get('experience', 'N/A')}</span>"

            st.markdown(f"""
            <div class="job-card">
                <h4>{job['title']}</h4>
                <p><b>Company:</b> {job['company']}</p>
                <p>{badges}</p>
            </div>
            """, unsafe_allow_html=True)

            col1, col2 = st.columns([1, 1])
            with col1:
                st.markdown(f"[ Apply Here]({job['apply_link']})")
            with col2:
                if st.button(" Tailor Resume", key=f"tailor_{i}"):
                    with st.spinner("Optimizing resume..."):
                        result = generate_tailored_resume(
                            resume_text,
                            job.get("description", "")
                        )
                        st.session_state.tailored[i] = result

            # Show tailored resume
            if i in st.session_state.tailored:
                st.text_area(
                    "📄 Tailored Resume",
                    st.session_state.tailored[i],
                    height=250
                )

    else:
        st.info("Upload your resume and click 'Find Jobs' to see results.")

else:
    st.info("Please upload your resume to get started.")