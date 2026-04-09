from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def match_jobs(resume_text, jobs):
    if not jobs:
        return []

    descriptions = [job.get("description", "") for job in jobs]

    vectorizer = TfidfVectorizer(stop_words="english")

    try:
        vectors = vectorizer.fit_transform([resume_text] + descriptions)
        scores = cosine_similarity(vectors[0:1], vectors[1:]).flatten()
    except:
        return jobs

    # 🔹 Internal relevance (not shown to user)
    for i, job in enumerate(jobs):
        job["_relevance"] = scores[i]

    # 🔹 Sort by relevance
    jobs = sorted(jobs, key=lambda x: x["_relevance"], reverse=True)

    # 🔹 Clean up before returning
    for job in jobs:
        job.pop("_relevance", None)

    return jobs