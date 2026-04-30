import json
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from openai import OpenAI

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

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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" 
)

class Message(BaseModel):
    message: str

@app.post("/chat")
async def chat(msg: Message):
    context_string = json.dumps(denis_info, ensure_ascii=False)
    
    completion = client.chat.completions.create(
        model="meta/llama-3.1-8b-instruct", #
        messages=[
            {
                "role": "system", 
                "content": f"Ești asistentul virtual de pe portofoliul lui Denis. Răspunde profesional și prietenos. Iată datele despre Denis pe care trebuie să le folosești: {context_string}. Dacă nu știi un răspuns, sugerează vizitatorului să-l contacteze pe Denis prin email."
            },
            {"role": "user", "content": msg.message}
        ],
        max_tokens=500
    )
    return {"response": completion.choices[0].message.content}




