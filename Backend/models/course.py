from pydantic import BaseModel
from uuid import UUID
from datetime import datetime
from typing import Optional

# Frontend'ten gelen istek için model
class CourseCreate(BaseModel):
    name: str
    description: Optional[str] = None
    teacher_id: UUID

# Veritabanında saklanan tam model
class Course(CourseCreate):
    id: UUID
    created_at: datetime

    class Config:
        from_attributes = True  # Pydantic v2 için (önceki orm_mode)
