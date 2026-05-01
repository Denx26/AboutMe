import json
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google import genai
from google.genai import types

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

path1 = os.getenv("get_denis_ro")
path2 = os.getenv("get_denis_en")

try:
    with open(path1, "r", encoding="utf-8") as f:
        denis_info = json.load(f)
    with open(path2, "r", encoding="utf-8") as f1:
        denis_info1 = json.load(f1)
except Exception as e:
    print(f"Error loading JSON: {e}")
    denis_info, denis_info1 = {}, {}

class Message(BaseModel):
    message: str

@app.post("/chat")
async def chat(msg: Message):
    try:
        context = denis_info if any(c in msg.message.lower() for c in "ăâîșț") else denis_info1
        context_string = json.dumps(context, ensure_ascii=False)
        
        response = await client.aio.models.generate_content(
            model="gemini-2.5-flash",
            contents=msg.message,
            config=types.GenerateContentConfig(
                 system_instruction=(
                f"Esti asistenul virtual inteligent al lui Denis."
                f"Foloseste aceste date reale ca baza: {context_string}"
                "Reguli de comportament: "
                "1. Fii profesional, dar entuziast. "
                "2. Daca esti intrebat despre viitorul lui Denis, fa predictii creative si optimiste. "
                "bazate pe pasiunile lui pentru AI/ML si Full Stack. Imagineaza-l lucrand la proiecte inovatoare. "
                "3. Nu inventa facultati (ex: Cai Ferate) daca nu apar in JSON; spune doar Universitatea Politehnica Timisoara adica Facultatea de Automatica si Calculatoare. "
                "4. Daca cineva te intreaba ceva ce nu e in JSON, raspunde bazandu-te pe 'viziunea' ta de asistent AI despre potentialul lui."
                "5. Daca cineva te intreaba la fel, acelasi lucru sau contexte asemanatoare in English, sa ii raspunzi la fel in English. Fie ca incepe conversatia in English la fel sa continui in English sau daca intreaba ulterior. "                
            ),
                max_output_tokens=500,
                temperature=0.8
            )
        )
        return {"response": response.text if response.text else "Salut! Se pare ca am nevoie o secunda sa ma gandesc. Intreaba-ma iar!"}
    except Exception as e:
        print(f"Eroare API: {e}")
        return {"response": "Momentan am primit prea multe întrebări și mă odihnesc puțin. Reîncearcă în câteva secunde sau contactează-l pe Denis pe email!"}
    
