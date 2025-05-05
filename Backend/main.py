import os
from fastapi import FastAPI, HTTPException
from dotenv import load_dotenv
import google.generativeai as genai
from importlib import reload
from Backend.matches import MatchRequest, MatchedStudent, MatchResponse, find_suitable_peers, select_best_match
from Backend.routes import student_routes, teacher_routes, course_routes, topic_routes, explanation_routes, \
    peer_match_routes, teacher_report_routes, question_routes


print("Main.py dosyası çalıştırılıyor...")

# Ortam değişkenlerini yükle
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
model = None

# Gemini modelini yapılandır
if GEMINI_API_KEY:
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel('models/gemini-2.0-flash-exp')
        print("Gemini modeli başarıyla yapılandırıldı.")
    except Exception as e:
        print(f"Uyarı: Gemini modeli yapılandırılamadı: {e}")
else:
    print("Uyarı: GEMINI_API_KEY ortam değişkeni tanımlanmamış. Gemini analizi devre dışı.")

app = FastAPI()
app = FastAPI()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-pro")

reload(student_routes)
reload(teacher_routes)
reload(course_routes)
reload(topic_routes)
reload(explanation_routes)
reload(peer_match_routes)
reload(teacher_report_routes)
reload(question_routes)
app.include_router(student_routes.router)
app.include_router(teacher_routes.router)
app.include_router(course_routes.router)
app.include_router(topic_routes.router)
app.include_router(explanation_routes.router)
app.include_router(peer_match_routes.router)
app.include_router(teacher_report_routes.router)
app.include_router(question_routes.router)
print("FastAPI uygulaması oluşturuldu.")

async def get_gemini_analysis(difficulty_topic: str) -> str:
    """Verilen konu için Gemini'den kısa bir analiz alır."""
    try:
        gemini_prompt = f"{difficulty_topic} konusunda zorlanan bir öğrenciye 2 3 cümle ile nasıl yardımcı olursun? Bu öğrencinin seviyesi orta."
        response = await model.generate_content(gemini_prompt)
        return response.text
    except Exception as e:
        return f"Gemini API hatası: {e}"

@app.post("/matches", response_model=MatchResponse)
async def match_students(request: MatchRequest):
    print(f"/matches endpoint'ine istek geldi: {request}")
    analysis = "Konu belirtilmemiş."

    if request.difficulty_topic:
        if model:
            analysis = await get_gemini_analysis(request.difficulty_topic)
        else:
            analysis = "Gemini API anahtarı bulunamadığı için analiz yapılamadı."

    suitable_peers = find_suitable_peers(request, request.student_id)
    print(f"Uygun akranlar bulundu: {suitable_peers}")
    matched_student_data = select_best_match(suitable_peers)
    print(f"En uygun akran seçildi: {matched_student_data}")

    if matched_student_data:
        matched_student = MatchedStudent(
            student_id=matched_student_data["student_id"],
            first_name=matched_student_data["first_name"],
            last_name=matched_student_data["last_name"],
            overall_rating=matched_student_data["overall_rating"],
            match_reason=analysis
        )
        response = MatchResponse(matched_students=[matched_student], success=True)
        print(f"/matches yanıtı oluşturuldu: {response}")
        return response
    else:
        error_message = "Uygun akran bulunamadı."
        print(f"Hata: {error_message}")
        raise HTTPException(status_code=404, detail=error_message)

if __name__ == "_main_":
    import uvicorn
    print("Uvicorn başlatılıyor...")
    uvicorn.run(app, host="0.0.0.0", port=8000)
    print("Uvicorn çalışmayı bitirdi.")

print("MAIN.PY SONU")
