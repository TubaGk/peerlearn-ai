import streamlit as st
from api_utils import evaluate_explanation_mock

def show():
    st.title("🧠 Anlatım Değerlendirme")

    student_id = st.number_input("Öğrenci ID", value=1)
    topic = st.selectbox("Konu", ["Türev", "İyon", "Organik Kimya"])
    explanation = st.text_area("Anlatımın", placeholder="Bu konuyu kendi cümlelerinle açıkla...")

    if st.button("AI ile Değerlendir"):
        if explanation.strip():
            result = evaluate_explanation_mock(topic, explanation)
            st.success(f"Puan: {result['rating']} / 5")
            st.markdown(f"💬 Yorum: {result['comment']}")
            st.markdown(f"💡 Öneri: {result['suggestion']}")
        else:
            st.warning("Lütfen önce bir anlatım yaz.")
