import streamlit as st

st.title("🧠 Anlatım Oluşturma ve Değerlendirme")

st.markdown("Hasan, eşleştirildin. Aşağıya konuyla ilgili kendi anlatımını yaz.")

topic = "TÜREV NEDİR?"
st.markdown(f"### Konu: {topic}")

user_input = st.text_area("Kendi cümlelerinle açıkla:", height=150)

if st.button("AI ile Değerlendir"):
    if user_input.strip():
        # Örnek değerlendirme cevabı (mock)
        st.info("AI: Tanım doğru, örnek eksik. 5 üzerinden 4.")
        st.markdown("💡 Öneri: Gerçek hayattan bir örnekle destekleyebilirsin.")
    else:
        st.warning("Lütfen önce bir metin girin.")
