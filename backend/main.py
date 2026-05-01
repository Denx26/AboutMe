import json
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from google import genai
from google.genai import types

load_dotenv()
app = FastAPI()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

try:
    with open("info-ro/info_denis_ro.json", "r", encoding="utf-8") as f:
        denis_info = json.load(f)
    with open("info-en/info_denis_en.json", "r", encoding="utf-8") as f1:
        denis_info1 = json.load(f1)
except Exception as e:
    print(f"Error loading JSON: {e}")
    denis_info, denis_info1 = {}, {}

class Message(BaseModel):
    message: str

@app.post("/chat")
async def chat(msg: Message):
    context = denis_info if any(c in msg.message.lower() for c in "ăâîșț") else denis_info1
    context_string = json.dumps(context, ensure_ascii=False)
    
    response = client.models.generate_content(
        model="gemini-2.0-flash",
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
            max_output_tokens=200,
            temperature=0.5
        )
    )
    
    return {"response": response.text}
