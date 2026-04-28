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

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key="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"
)

class Message(BaseModel):
    message: str


