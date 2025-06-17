import re
from io import BytesIO
from pdfminer.high_level import extract_text
import spacy

nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(file: BytesIO) -> str:
    return extract_text(file)

def extract_email(text: str) -> str:
    match = re.search(r'[\w\.-]+@[\w\.-]+', text)
    return match.group(0) if match else None

def extract_phone(text: str) -> str:
    match = re.search(r'(\+?\d{1,3}[\s-]?)?\(?\d{3,5}\)?[\s.-]?\d{3,5}[\s.-]?\d{3,5}', text)
    return match.group(0) if match else None

def extract_name(text: str) -> str:
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None

def extract_skills(text: str) -> list:
    skill_keywords = ["python", "java", "sql", "mongodb", "react", "docker", "node", "nlp", "aws"]
    found = []
    for word in skill_keywords:
        if re.search(rf"\b{word}\b", text, re.IGNORECASE):
            found.append(word.lower())
    return list(set(found))

def extract_education(text: str) -> str:
    education_keywords = ["bachelor", "master", "b.tech", "bsc", "msc", "m.tech", "phd"]
    lines = text.lower().split('\n')
    return "\n".join(line for line in lines if any(k in line for k in education_keywords))

def extract_experience(text: str) -> str:
    lines = text.lower().split('\n')
    experience_lines = [line for line in lines if "experience" in line or "internship" in line]
    return "\n".join(experience_lines)
