from pydantic import BaseModel
from uuid import UUID
from datetime import datetime

class QuestionCreate(BaseModel):
    content: str
    course_id: UUID

class Question(QuestionCreate):
    id: UUID
    created_at: datetime

    class Config:
        from_attributes = True
