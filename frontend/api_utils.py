import requests

BACKEND_URL = "http://localhost:8000"

def get_peer_match(student_id: int, topic: str, class_level: int):
    url = f"{BACKEND_URL}/matches"
    payload = {
        "student_id": student_id,
        "difficulty_topic": topic,
        "class_level": class_level
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return response.json()
    else:
        return {"success": False, "matched_students": [], "error": response.text}

def evaluate_explanation_mock(topic: str, explanation: str):
    if "örnek" in explanation.lower():
        return {
            "rating": 5,
            "comment": "Tanım ve örnek harika.",
            "suggestion": "Grafik eklersen daha da güçlü olur."
        }
    else:
        return {
            "rating": 4,
            "comment": "Tanım güzel ama örnek eksik.",
            "suggestion": "Gerçek bir örnekle destekleyebilirsin."
        }
