from pydantic import BaseModel
from uuid import UUID
from typing import Optional

class PeerMatchCreate(BaseModel):
    student_1_id: UUID
    student_2_id: UUID
    match_score: Optional[float] = 0.0

class PeerMatch(PeerMatchCreate):
    id: UUID

    class Config:
        from_attributes = True
