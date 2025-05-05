from fastapi import APIRouter, HTTPException
from Backend.models.teacher import Teacher, TeacherCreate
from Backend.services.firebase_service import db
import uuid
from datetime import datetime

router = APIRouter()

@router.post("/teachers/", response_model=Teacher)
async def create_teacher(teacher_data: TeacherCreate):
    try:
        teacher_id = str(uuid.uuid4())  # UUID oluştur
        joined_at = datetime.utcnow().isoformat()  # joined_at'ı otomatik oluştur
        profile_score = 0  # İlk başta 0 olabilir

        teacher_dict = {
            "id": teacher_id,
            "name": teacher_data.name,
            "surname": teacher_data.surname,
            "subject": teacher_data.subject,
            "email": teacher_data.email,
            "joined_at": joined_at,
            "profile_score": profile_score
        }

        db.child("teachers").child(teacher_id).set(teacher_dict)
        return teacher_dict

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# Öğretmen bilgilerini alma
@router.get("/teachers/{teacher_id}", response_model=Teacher)
async def get_teacher(teacher_id: str):
    try:
        doc_ref = db.collection("teachers").document(teacher_id)
        doc = doc_ref.get()
        if doc.exists:
            teacher_data = doc.to_dict()
            return Teacher(**teacher_data)
        else:
            raise HTTPException(status_code=404, detail="Teacher not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
