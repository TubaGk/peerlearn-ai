from fastapi import FastAPI
from dotenv import load_dotenv
import os
from importlib import reload
import google.generativeai as genai

from Backend.routes import student_routes, teacher_routes, course_routes, topic_routes, explanation_routes, \
    peer_match_routes, teacher_report_routes, question_routes

load_dotenv()

app = FastAPI()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

reload(student_routes)
reload(teacher_routes)
reload(course_routes)
reload(topic_routes)
reload(explanation_routes)
reload(peer_match_routes)
reload(teacher_report_routes)
reload(question_routes)
app.include_router(student_routes.router)
app.include_router(teacher_routes.router)
app.include_router(course_routes.router)
app.include_router(topic_routes.router)
app.include_router(explanation_routes.router)
app.include_router(peer_match_routes.router)
app.include_router(teacher_report_routes.router)
app.include_router(question_routes.router)


@app.get("/")
def root():
    return {"message": "PeerLearn-AI Backend is runningg!"}

@app.get("/generate")
def generate_response(prompt: str):
    response = model.generate_content(prompt)
    return {"response": response.text}
