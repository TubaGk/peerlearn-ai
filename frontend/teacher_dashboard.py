import streamlit as st
import pandas as pd

def show():
    st.title("📊 Öğretmen Paneli")

    st.markdown("Öğrencilerin performansını ve sistem kullanımını buradan takip edebilirsiniz.")

    # 🔹 Sınıf seçimi
    selected_class = st.selectbox("Sınıf Seçiniz", ["10. Sınıf", "11. Sınıf", "Tüm Sınıflar"])

    # 🔹 Mock öğrenci verisi
    data = [
        {"Ad": "Aylin Demir", "Sınıf": 10, "Puan": 4.5, "Anlatım Sayısı": 3, "Eşleşme Sayısı": 2},
        {"Ad": "Emir Yılmaz", "Sınıf": 10, "Puan": 4.8, "Anlatım Sayısı": 5, "Eşleşme Sayısı": 4},
        {"Ad": "Zeynep Kaya", "Sınıf": 11, "Puan": 4.9, "Anlatım Sayısı": 2, "Eşleşme Sayısı": 1},
        {"Ad": "Furkan Şahin", "Sınıf": 11, "Puan": 4.7, "Anlatım Sayısı": 4, "Eşleşme Sayısı": 3},
    ]
    df = pd.DataFrame(data)

    # 🔹 Sınıfa göre filtreleme
    if selected_class == "10. Sınıf":
        df = df[df["Sınıf"] == 10]
    elif selected_class == "11. Sınıf":
        df = df[df["Sınıf"] == 11]

    st.subheader("📋 Öğrenci Listesi")
    st.dataframe(df, use_container_width=True)

    st.subheader("📈 Ortalama Puan Dağılımı")
    st.bar_chart(df.set_index("Ad")["Puan"])

    st.subheader("📚 Anlatım Aktivitesi")
    st.line_chart(df.set_index("Ad")["Anlatım Sayısı"])
