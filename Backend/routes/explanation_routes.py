from fastapi import APIRouter, HTTPException
from Backend.models.explanation import Explanation
from Backend.services.firebase_service import db
import uuid

router = APIRouter()

# Yeni açıklama oluşturma
@router.post("/explanations/", response_model=Explanation)
async def create_explanation(explanation: Explanation):
    try:
        explanation_id = str(uuid.uuid4())
        explanation_data = explanation.dict()
        db.child("explanations").document(explanation_id).set(explanation_data)
        return explanation.copy(update={"id": explanation_id})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Açıklama bilgilerini listeleme
@router.get("/explanations/{explanation_id}", response_model=Explanation)
async def get_explanation(explanation_id: str):
    try:
        doc_ref = db.child("explanations").document(explanation_id)
        doc = doc_ref.get()
        if doc.exists:
            return doc.to_dict()
        else:
            raise HTTPException(status_code=404, detail="Explanation not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
