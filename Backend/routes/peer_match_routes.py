from fastapi import APIRouter, HTTPException
from Backend.models.peer_match import PeerMatch, PeerMatchCreate
from Backend.services.firebase_service import db
from uuid import uuid4

router = APIRouter()

@router.post("/peer_matches/", response_model=PeerMatch)
async def create_peer_match(data: PeerMatchCreate):
    try:
        match_id = str(uuid4())
        match_dict = {
            "id": match_id,
            "student_1_id": str(data.student_1_id),
            "student_2_id": str(data.student_2_id),
            "match_score": data.match_score
        }
        db.collection("peer_matches").document(match_id).set(match_dict)
        return match_dict
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/peer_matches/{peer_match_id}", response_model=PeerMatch)
async def get_peer_match(peer_match_id: str):
    try:
        doc = db.collection("peer_matches").document(peer_match_id).get()
        if doc.exists:
            return doc.to_dict()
        else:
            raise HTTPException(status_code=404, detail="Peer match not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
