from fastapi import APIRouter, HTTPException
from Backend.models.question import Question, QuestionCreate
from Backend.services.firebase_service import db
from uuid import uuid4
from datetime import datetime

router = APIRouter()

@router.post("/questions/", response_model=Question)
async def create_question(data: QuestionCreate):
    try:
        question_id = str(uuid4())
        created_at = datetime.utcnow().isoformat()
        question_dict = {
            "id": question_id,
            "content": data.content,
            "course_id": str(data.course_id),
            "created_at": created_at
        }
        db.collection("questions").document(question_id).set(question_dict)
        return question_dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/questions/{question_id}", response_model=Question)
async def get_question(question_id: str):
    try:
        doc = db.collection("questions").document(question_id).get()
        if doc.exists:
            return doc.to_dict()
        else:
            raise HTTPException(status_code=404, detail="Question not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
