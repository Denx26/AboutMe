import json
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import AsyncOpenAI

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

try:
    with open("info-ro/info_denis_ro.json", "r", encoding="utf-8") as f:
        denis_info = json.load(f)
except Exception as e:
    print(f"Eroare la încărcarea JSON-ului: {e}")
    denis_info = {}

try:
    with open("info-en/info_denis_en.json", "r", encoding="utf-8") as f1:
        denis_info1 = json.load(f1)
except Exception as e:
    print(f"Error at JSON load: {e}")
    denis_info1 = {}

load_dotenv()
api_key = os.getenv("NVIDIA_API_KEY")

client = AsyncOpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=api_key 
)

class Message(BaseModel):
    message: str

@app.post("/chat")
async def chat(msg: Message):
    # Folosește ambele contexte pentru a fi pregătit
    context = denis_info if any(c in msg.message.lower() for c in "ăâîșț") else denis_info1
    context_string = json.dumps(context, ensure_ascii=False)
    
    # ADAUGĂ 'await' aici - asta e cheia vitezei!
    completion = await client.chat.completions.create(
        model="meta/llama-3.1-8b-instruct",
        messages=[
            {
                "role": "system", 
                "content": f"Ești asistentul lui Denis. Răspunde scurt folosind: {context_string}"
            },
            {"role": "user", "content": msg.message}
        ],
        max_tokens=100,
        temperature=0.5
    )
    return {"response": completion.choices[0].message.content}



