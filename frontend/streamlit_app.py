import streamlit as st
from login_page import show as show_login
from matching_page import show as show_matching
from explanation_page import show as show_explanation
from question_page import show as show_question
from teacher_dashboard import show as show_teacher
from student_profile import show as show_profile

st.set_page_config(page_title="PeerLearn AI", layout="wide")

# Oturum başlatılmadıysa false yap
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False

st.sidebar.title("📚 PeerLearn AI")
page = st.sidebar.radio("Sayfa Seç", [
    "🔐 Giriş",
    "👥 Akran Eşleştirme",
    "🧠 Anlatım Değerlendirme",
    "❓ Soru Sor",
    "📊 Öğretmen Paneli",
    "👤 Öğrenci Profili"
])

# Giriş kontrolü: sadece giriş sayfası hariç sayfalarda engelle
if page != "🔐 Giriş" and not st.session_state["logged_in"]:
    st.warning("Bu sayfayı görmek için lütfen önce giriş yapın.")
    show_login()
else:
    if page == "🔐 Giriş":
        show_login()
    elif page == "👥 Akran Eşleştirme":
        show_matching()
    elif page == "🧠 Anlatım Değerlendirme":
        show_explanation()
    elif page == "❓ Soru Sor":
        show_question()
    elif page == "📊 Öğretmen Paneli":
        show_teacher()
    elif page == "👤 Öğrenci Profili":
        show_profile()
