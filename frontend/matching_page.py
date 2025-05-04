import streamlit as st
from api_utils import get_peer_match

def show():
    st.title("🤝 Akran Eşleştirme")

    student_id = st.number_input("Öğrenci ID", value=1)
    class_level = st.selectbox("Sınıf", [10, 11])
    topic = st.selectbox("Zorlandığın Konu", ["Asit-Baz", "Fonksiyon Grafikleri"])

    if st.button("Eşleşme Talep Et"):
        with st.spinner("Eşleştirme yapılıyor..."):
            result = get_peer_match(student_id, topic, class_level)
            if result.get("success"):
                student = result["matched_students"][0]
                st.success(f"{student['first_name']} {student['last_name']} ile eşleştirildin!")
                st.markdown(f"💬 AI Yorumu: _{student['match_reason']}_")
                st.markdown(f"⭐ Puan: {student['overall_rating']}")
            else:
                st.error("Uygun eşleşme bulunamadı.")
