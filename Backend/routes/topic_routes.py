from fastapi import APIRouter, HTTPException
from Backend.models.topic import Topic, TopicCreate
from Backend.services.firebase_service import db
from uuid import uuid4

router = APIRouter()

@router.post("/topics/", response_model=Topic)
async def create_topic(data: TopicCreate):
    try:
        topic_id = str(uuid4())
        topic_dict = {
            "id": topic_id,
            "name": data.name,
            "description": data.description,
            "course_id": str(data.course_id)
        }
        db.collection("topics").document(topic_id).set(topic_dict)
        return topic_dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/topics/{topic_id}", response_model=Topic)
async def get_topic(topic_id: str):
    try:
        doc = db.collection("topics").document(topic_id).get()
        if doc.exists:
            return doc.to_dict()
        else:
            raise HTTPException(status_code=404, detail="Topic not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
