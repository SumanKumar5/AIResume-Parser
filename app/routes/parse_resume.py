from fastapi import APIRouter, File, UploadFile
from app.services.parser import (
    extract_text_from_pdf,
    extract_email,
    extract_phone,
    extract_name,
    extract_skills,
    extract_education,
    extract_experience
)
from app.models.schemas import ParsedResume
from io import BytesIO

router = APIRouter()

@router.post("/parse-resume", response_model=ParsedResume, tags=["Resume"])
async def parse_resume(file: UploadFile = File(...)):
    content = await file.read()
    text = extract_text_from_pdf(BytesIO(content))

    parsed = ParsedResume(
        name=extract_name(text),
        email=extract_email(text),
        phone=extract_phone(text),
        skills=extract_skills(text),
        education=extract_education(text),
        experience=extract_experience(text)
    )

    return parsed
