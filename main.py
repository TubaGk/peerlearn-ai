from fastapi import FastAPI
from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

app = FastAPI()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

@app.get("/")
def root():
    return {"message": "PeerLearn-AI Backend is running!"}

@app.get("/generate")
def generate_response(prompt: str):
    response = model.generate_content(prompt)
    return {"response": response.text}
