import streamlit as st

st.title("🤝 Eşleştirme Sayfası")

# Örnek: Kullanıcı bilgisi (genelde session'dan alınır)
user_name = "Aylin"
user_class = "10. Sınıf"
user_needs = ["Asit-Baz", "İyonlar"]

st.markdown(f"**{user_name} ({user_class})** olarak giriş yaptınız.")
st.markdown("### Eksik Olduğun Konular:")
st.write(", ".join(user_needs))

if st.button("Eşleşme Talep Et"):
    # Basit eşleştirme çıktısı (mock)
    matched_name = "Emir"
    matched_topic = "Asit-Baz"
    st.success(f"🎉 {matched_name} ile '{matched_topic}' konusunda eşleştirildiniz!")
    st.button("Görüşmeyi Bitir")
