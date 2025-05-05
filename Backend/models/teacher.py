from pydantic import BaseModel, EmailStr
from typing import Optional
from uuid import UUID
from datetime import datetime

# Bu modeli frontend POST ederken kullanacağız (id yok)
class TeacherCreate(BaseModel):
    name: str
    surname: str
    subject: str
    email: EmailStr

# Bu model veritabanında tam veri olarak tutulur (id zorunludur)
class Teacher(TeacherCreate):
    id: str
    joined_at: str
    profile_score: int
