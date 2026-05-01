# AI-Powered Portfolio Assistant

An intelligent virtual assistant that answers questions about my career, education, and projects — deployed as an async FastAPI backend with Google Gemini integration.

---

## Overview

This repository hosts the asynchronous backend for my personal portfolio. The assistant functions as a *recruiter agent* that leverages state-of-the-art LLM models to provide contextual, personalized information to visitors.

- **Frontend:** [View on Vercel](https://your-vercel-link.vercel.app)
- **Backend API:** [View on Railway](https://your-railway-link.up.railway.app)

---

## Technical Features

- **AI Engine** — Google Gemini 2.5 Flash (or 2.0 Live Preview) for fast, precise responses
- **Context Injection** — JSON-based Knowledge Base to personalize model answers
- **Performance** — Built with FastAPI and full `async/await` support for low latency
- **Security** — API keys and resource paths managed via `.env` environment variables
- **Containerization** — Docker configuration for consistent, reproducible deployments

---

## Tech Stack

```
Language     →  Python 3.12+
Framework    →  FastAPI
AI SDK       →  Google GenAI
Deployment   →  Railway (Backend) · Vercel (Frontend)
DevOps       →  Docker
```

---

## Project Structure

```text
backend/
├── info-en/            # Contextual data (English)
├── info-ro/            # Contextual data (Romanian)
├── main.py             # FastAPI server and AI logic
├── Dockerfile          # Containerization instructions
├── requirements.txt    # Project dependencies
└── .env.example        # Template for environment variables
```

---

## Local Setup

### 1. Environment Configuration

Create a `.env` file inside the `backend/` folder and add your credentials.

> No spaces around the `=` sign.

```env
GOOGLE_API_KEY=your_actual_key_here
get_denis_en=./info-en/info_denis_en.json
get_denis_ro=./info-ro/info_denis_ro.json
```

### 2. Run with Docker (Recommended)

```bash
# Build the image
docker build -t portfolio-assistant .

# Run the container
docker run -p 8001:8080 --env-file .env portfolio-assistant
```

### 3. Manual Execution

```bash
pip install -r requirements.txt
uvicorn main:app --reload --port 8001
```

---

## Privacy & Security

The JSON files used for context contain only public professional information. Sensitive data and access keys are protected via environment variables and are never stored in the repository.
