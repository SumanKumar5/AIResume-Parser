from fastapi import APIRouter
from app.models.schemas import MatchRequest, MatchResult
from app.services.matcher import extract_skills_from_text, compute_match_score

router = APIRouter()

@router.post("/analyze-match", response_model=MatchResult, tags=["Matching"])
async def analyze_match(payload: MatchRequest):
    resume = payload.resume_text
    jd = payload.job_description

    resume_skills = extract_skills_from_text(resume)
    jd_skills = extract_skills_from_text(jd)

    missing = [skill for skill in jd_skills if skill not in resume_skills]
    match_score = compute_match_score(resume, jd)

    return MatchResult(
        match_score=match_score,
        missing_skills=missing,
        jd_skills=jd_skills
    )
