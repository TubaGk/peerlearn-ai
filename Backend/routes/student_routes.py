from fastapi import APIRouter, HTTPException
from Backend.models.student import Student, StudentCreate
from Backend.services.firebase_service import db
import uuid
from datetime import datetime

router = APIRouter()

@router.post("/students/", response_model=Student)
async def create_student(student_data: StudentCreate):
    try:
        student_id = str(uuid.uuid4())  # UUID oluştur
        joined_at = datetime.utcnow().isoformat()
        profile_score = 0  # İlk başlangıçta 0 olabilir

        student_dict = {
            "id": student_id,
            "first_name": student_data.first_name,
            "last_name": student_data.last_name,
            "grade_level": student_data.grade_level,
            "email": student_data.email,
            "joined_at": joined_at,
            "profile_score": profile_score
        }

        db.child("students").child(student_id).set(student_dict)
        return student_dict

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
