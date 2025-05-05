from pydantic import BaseModel
from uuid import UUID

class ExplanationCreate(BaseModel):
    content: str
    course_id: UUID
    student_id: UUID

class Explanation(ExplanationCreate):
    id: UUID

    class Config:
        from_attributes = True
