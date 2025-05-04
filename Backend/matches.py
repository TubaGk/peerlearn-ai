from pydantic import BaseModel
from typing import List, Dict, Optional

# Veri modelleri (Pydantic)
class MatchRequest(BaseModel):
    student_id: int
    difficulty_topic: Optional[str] = None
    class_level: Optional[int] = None

class MatchedStudent(BaseModel):
    student_id: int
    first_name: str
    last_name: str
    overall_rating: float
    match_reason: str

class MatchResponse(BaseModel):
    matched_students: List[MatchedStudent]
    success: bool

# Geçici öğrenci verileri (Veritabanı yerine)
students_data: List[Dict] = [
    {"student_id": 1, "first_name": "Aylin", "last_name": "Demir", "class_level": 10, "overall_rating": 4.5, "topics": {"Asit-Baz": "beginner", "Organik Kimya": "expert"}},
    {"student_id": 2, "first_name": "Emir", "last_name": "Yılmaz", "class_level": 10, "overall_rating": 4.8, "topics": {"Asit-Baz": "expert", "Organik Kimya": "intermediate"}},
    {"student_id": 3, "first_name": "Zeynep", "last_name": "Kaya", "class_level": 11, "overall_rating": 4.9, "topics": {"İkinci Dereceden Denklemler": "expert", "Fonksiyon Grafikleri": "beginner"}},
    {"student_id": 4, "first_name": "Furkan", "last_name": "Şahin", "class_level": 11, "overall_rating": 4.7, "topics": {"İkinci Dereceden Denklemler": "intermediate", "Fonksiyon Grafikleri": "expert"}},
]

def find_suitable_peers(request: MatchRequest, current_student_id: int) -> List[Dict]:
    """Uygun akranları geçici verilerden bulur."""
    return [
        student for student in students_data
        if request.class_level is not None and student["class_level"] == request.class_level
        and request.difficulty_topic is not None and student["topics"].get(request.difficulty_topic) == "expert"
        and student["student_id"] != current_student_id
    ]

def select_best_match(peers: List[Dict]) -> Optional[Dict]:
    """Verilen akranlar listesinden en uygun olanı (puanına göre) seçer."""
    if peers:
        return max(peers, key=lambda x: x["overall_rating"])
    return None