from fastapi import FastAPI
from app.config import settings
from app.routes import health, parse_resume
from app.routes import analyze_match
from app.routes import rewrite_bullets

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.API_VERSION
)

# Include route modules
app.include_router(health.router)
app.include_router(parse_resume.router)
app.include_router(analyze_match.router)
app.include_router(rewrite_bullets.router)