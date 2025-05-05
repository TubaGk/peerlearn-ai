from pydantic import BaseModel
from uuid import UUID
from typing import Optional

class TopicCreate(BaseModel):
    name: str
    description: Optional[str] = None
    course_id: UUID

class Topic(TopicCreate):
    id: UUID

    class Config:
        from_attributes = True
