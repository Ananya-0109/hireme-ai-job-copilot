import requests
import os

# API KEYS
JSEARCH_API_KEY = os.getenv("RAPIDAPI_KEY") or "0924df69e6msh3efe2425fe84c98p16245djsn2564d9651917"
ADZUNA_APP_ID = "b2eee73e"
ADZUNA_APP_KEY = "dde90406c2191c2c0154ff270064c7b3"



# 🔹 Experience keyword mapping (search + filtering)
exp_map = {
    "Fresher": ["fresher", "entry", "graduate"],
    "0-1 years": ["0 year", "1 year", "junior"],
    "1-2 years": ["1 year", "2 year"],
    "3-5 years": ["3 year", "4 year", "5 year", "mid"],
    "5+ years": ["5 year", "senior", "lead"]
}


# 🔹 JSearch (global fallback)
def fetch_jsearch_jobs(role, experience):
    url = "https://jsearch.p.rapidapi.com/search"

    query = f"{role}"

    headers = {
        "X-RapidAPI-Key": JSEARCH_API_KEY,
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }

    params = {
        "query": query,
        "page": "1",
        "num_pages": "2"
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return []

    data = response.json()
    jobs = []

    for job in data.get("data", []):
        apply_link = job.get("job_apply_link", "")

        # ❌ Skip invalid links
        if not apply_link or not apply_link.startswith("http"):
            continue

        desc = job.get("job_description", "").lower()

        # ✅ Experience filtering
        keywords = exp_map.get(experience, [])
        if keywords and not any(k in desc for k in keywords):
            continue

        location_text = f"{job.get('job_city', '')}, {job.get('job_country', '')}".strip(", ")

        jobs.append({
            "title": job.get("job_title", "N/A"),
            "company": job.get("employer_name", "N/A"),
            "description": job.get("job_description", ""),
            "apply_link": apply_link,
            "location": location_text if location_text else "Global"
        })

    return jobs


# 🔹 Adzuna (India-focused)
def fetch_adzuna_jobs(role, experience):
    url = "https://api.adzuna.com/v1/api/jobs/in/search/1"

    params = {
        "app_id": ADZUNA_APP_ID,
        "app_key": ADZUNA_APP_KEY,
        "what": role,
        "results_per_page": 20
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return []

    data = response.json()
    jobs = []

    for job in data.get("results", []):
        apply_link = job.get("redirect_url", "")

        # ❌ Skip invalid links
        if not apply_link or not apply_link.startswith("http"):
            continue

        desc = job.get("description", "").lower()

        # ✅ Experience filtering
        keywords = exp_map.get(experience, [])
        if keywords and not any(k in desc for k in keywords):
            continue

        jobs.append({
            "title": job.get("title", "N/A"),
            "company": job.get("company", {}).get("display_name", "N/A"),
            "description": job.get("description", ""),
            "apply_link": apply_link,
            "location": job.get("location", {}).get("display_name", "India")
        })

    return jobs


# 🔥 MAIN FUNCTION
def fetch_jobs(role, location="India", experience="Fresher"):

    adzuna_jobs = fetch_adzuna_jobs(role, experience)
    jsearch_jobs = fetch_jsearch_jobs(role, experience)

    # ✅ Combine
    all_jobs = adzuna_jobs + jsearch_jobs

    # ✅ Remove duplicates
    seen = set()
    unique_jobs = []

    for job in all_jobs:
        key = job["title"] + job["company"]

        if key not in seen:
            seen.add(key)
            unique_jobs.append(job)

    return unique_jobs