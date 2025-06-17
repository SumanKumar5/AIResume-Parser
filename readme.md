
# AIResume Parser — Resume Intelligence API

[![FastAPI](https://img.shields.io/badge/FastAPI-0.100.0-009688?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)](https://www.python.org/)
[![OpenAI](https://img.shields.io/badge/AI%20Powered-OpenAI/Gemini-green?logo=openai)](https://openai.com/)

> An intelligent FastAPI backend that empowers resumes with AI. SmartResume parses resume files, evaluates job match scores, and rewrites bullet points to maximize impact — perfect for job seekers, platforms, and ATS enhancements.

---

## 📌 Features

- 📄 **Resume Parsing** — Converts resume PDFs into structured JSON.
- 🧠 **Job Matching** — Analyzes compatibility between resume & job description.
- ✍️ **Bullet Rewriting** — AI-powered enhancement of resume bullet points.
- 🚀 **FastAPI** — Modern async backend with blazing-fast performance.
- ✅ **Ready for Integration** — Easily pluggable into frontend/job platforms.

---

## 🛠️ Tech Stack

| Layer        | Stack                          |
|--------------|--------------------------------|
| Backend      | FastAPI, Python 3.10+          |
| AI Services  | OpenAI / Gemini (via API)      |
| Data Models  | Pydantic                       |
| Config Mgmt  | dotenv (`.env`)                |
| Dev Tools    | Uvicorn, Postman               |

---

## 🚀 Getting Started

### 1. Clone the Repo
```bash
git clone https://github.com/SumanKumar5/AIResume-Parser.git
cd AIResume-Parser
````

### 2. Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Configure Environment

Create a `.env` file:

```env
OPENAI_API_KEY=your_key_here
```

### 4. Run the Server

```bash
uvicorn app.main:app --reload
```

---

## 🧪 API Endpoints

| Method | Endpoint           | Description                      |
| ------ | ------------------ | -------------------------------- |
| `GET`  | `/health`          | Health check                     |
| `POST` | `/parse-resume`    | Upload resume file (PDF/doc/txt) |
| `POST` | `/analyze-match`   | Match resume vs job description  |
| `POST` | `/rewrite-bullets` | Rewrite bullets with AI          |


---

## 📂 Project Structure

```
app/
├── main.py                # FastAPI app entry point
├── config.py              # Loads .env config
├── models/schemas.py      # Pydantic request/response models
├── routes/                # API route handlers
├── services/              # Core logic: parsing, AI, matching
```

---

## 📌 Example Requests

### 🔍 `/analyze-match`

```json
POST /analyze-match
{
  "resume_text": "Backend engineer with FastAPI...",
  "job_description": "Seeking backend Python developer..."
}
```

### ✍️ `/rewrite-bullets`

```json
POST /rewrite-bullets
{
  "bullets": ["Led a team of 5 engineers"],
  "job_description": "Looking for leadership and backend experience"
}
```

---

## 🧠 AI Integration

The `rewrite_bullets` and `analyze_match` routes use LLM APIs (e.g., OpenAI, Gemini) for:

* Semantic bullet rewriting
* Skill alignment scoring
* Natural language similarity

---

## 🙌 Contributing

Pull requests are welcome. For major changes, open an issue first to discuss what you’d like to change.

---

## 🌐 Author

Built with ❤️ by [Suman Kumar](https://github.com/SumanKumar5)


