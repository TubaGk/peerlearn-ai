from fastapi import APIRouter, HTTPException
from Backend.models.teacher_report import TeacherReport, TeacherReportCreate
from Backend.services.firebase_service import db
from uuid import uuid4
from datetime import datetime

router = APIRouter()

@router.post("/teacher_reports/", response_model=TeacherReport)
async def create_teacher_report(data: TeacherReportCreate):
    try:
        report_id = str(uuid4())
        created_at = datetime.utcnow().isoformat()
        report_dict = {
            "id": report_id,
            "teacher_id": str(data.teacher_id),
            "content": data.content,
            "created_at": created_at
        }
        db.collection("teacher_reports").document(report_id).set(report_dict)
        return report_dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/teacher_reports/{report_id}", response_model=TeacherReport)
async def get_teacher_report(report_id: str):
    try:
        doc = db.collection("teacher_reports").document(report_id).get()
        if doc.exists:
            return doc.to_dict()
        else:
            raise HTTPException(status_code=404, detail="Teacher report not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
