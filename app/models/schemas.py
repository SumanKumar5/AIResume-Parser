from pydantic import BaseModel
from typing import List, Optional

class ParsedResume(BaseModel):
    name: Optional[str]
    email: Optional[str]
    phone: Optional[str]
    skills: List[str]
    education: Optional[str]
    experience: Optional[str]

class MatchRequest(BaseModel):
    resume_text: str
    job_description: str

class MatchResult(BaseModel):
    match_score: float
    missing_skills: List[str]
    jd_skills: List[str]
class RewriteRequest(BaseModel):
    bullets: List[str]
    job_description: Optional[str] = None

class RewriteResponse(BaseModel):
    original: str
    improved: str