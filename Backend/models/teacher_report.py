from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class TeacherReportCreate(BaseModel):
    teacher_id: UUID
    content: str

class TeacherReport(TeacherReportCreate):
    id: UUID
    created_at: datetime

    class Config:
        from_attributes = True
