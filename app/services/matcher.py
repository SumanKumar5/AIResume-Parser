import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_skills_from_text(text: str, skill_keywords=None) -> list:
    if not skill_keywords:
        skill_keywords = [
            "python", "java", "react", "node", "mongodb", "sql", "aws",
            "docker", "fastapi", "typescript", "postman", "microservices"
        ]
    found = []
    for skill in skill_keywords:
        if re.search(rf"\b{skill}\b", text, re.IGNORECASE):
            found.append(skill.lower())
    return list(set(found))

def compute_match_score(resume_text: str, jd_text: str) -> float:
    tfidf = TfidfVectorizer().fit_transform([resume_text, jd_text])
    score = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
    return round(score * 100, 2)  # Return % match
