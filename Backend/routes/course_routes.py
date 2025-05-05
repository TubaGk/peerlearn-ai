from fastapi import APIRouter, HTTPException
from Backend.models.explanation import Explanation, ExplanationCreate
from Backend.services.firebase_service import db
from uuid import uuid4

router = APIRouter()

@router.post("/explanations/", response_model=Explanation)
async def create_explanation(data: ExplanationCreate):
    try:
        explanation_id = str(uuid4())
        explanation_dict = {
            "id": explanation_id,
            "content": data.content,
            "course_id": str(data.course_id),
            "student_id": str(data.student_id)
        }
        db.collection("explanations").document(explanation_id).set(explanation_dict)
        return explanation_dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/explanations/{explanation_id}", response_model=Explanation)
async def get_explanation(explanation_id: str):
    try:
        doc = db.collection("explanations").document(explanation_id).get()
        if doc.exists:
            return doc.to_dict()
        else:
            raise HTTPException(status_code=404, detail="Explanation not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
