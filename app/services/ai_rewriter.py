import google.generativeai as genai
from typing import List

import os
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.0-flash")

def rewrite_bullets_with_ai(bullets: List[str], job_description: str = None) -> List[dict]:
    rewritten = []

    for bullet in bullets:
        prompt = f"""You are a professional resume editor.
Improve the following resume bullet point to be more impactful, action-driven, and align with this job description if provided.

Bullet Point: "{bullet}"
Job Description: "{job_description or 'N/A'}"

Respond only with the improved version. No explanations."""

        try:
            response = model.generate_content(prompt)
            improved = response.text.strip()
        except Exception as e:
            improved = f"[Error generating improvement: {e}]"

        rewritten.append({
            "original": bullet,
            "improved": improved
        })

    return rewritten
