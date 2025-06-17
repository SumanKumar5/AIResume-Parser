from fastapi import APIRouter
from typing import List
from app.models.schemas import RewriteRequest, RewriteResponse
from app.services.ai_rewriter import rewrite_bullets_with_ai

router = APIRouter()

@router.post("/rewrite-bullets", response_model=List[RewriteResponse], tags=["AI Rewriter"])
async def rewrite_bullets(payload: RewriteRequest):
    results = rewrite_bullets_with_ai(payload.bullets, payload.job_description)
    return results
