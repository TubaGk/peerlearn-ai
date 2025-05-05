from pydantic import BaseModel, EmailStr
from typing import Optional

# Bu modeli frontend POST ederken kullanacağız (id yok)
class StudentCreate(BaseModel):
    first_name: str
    last_name: str
    grade_level: int
    email: EmailStr

# Bu model veritabanında tam veri olarak tutulur (id zorunludur)
class Student(StudentCreate):
    id: str
    joined_at: str
    profile_score: int
