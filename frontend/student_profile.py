import streamlit as st
import pandas as pd

def show():
    st.title("👤 Öğrenci Profili")

    st.markdown("Aşağıda öğrencinin geçmiş eşleşmeleri ve yaptığı anlatımlar yer almaktadır.")

    # Öğrenci Seçimi (şimdilik ID)
    student_id = st.selectbox("Öğrenci ID Seçiniz", [1, 2, 3])

    # Mock anlatım geçmişi
    explanations = {
        1: [{"Konu": "Türev", "Puan": 4, "Yorum": "Tanım doğru, örnek eksik."},
            {"Konu": "İyon", "Puan": 5, "Yorum": "Harika anlatım!"}],
        2: [{"Konu": "Asit-Baz", "Puan": 3, "Yorum": "Tanımda hata var."}],
        3: []
    }

    # Mock eşleşme geçmişi
    matches = {
        1: [{"Konu": "Fonksiyon Grafikleri", "Eşleştiği Kişi": "Emir Yılmaz", "Puan": 4.8}],
        2: [{"Konu": "Asit-Baz", "Eşleştiği Kişi": "Aylin Demir", "Puan": 4.5}],
        3: []
    }

    st.subheader("🧠 Anlatım Geçmişi")
    if explanations[student_id]:
        df_exp = pd.DataFrame(explanations[student_id])
        st.table(df_exp)
    else:
        st.info("Bu öğrenci henüz anlatım yapmamış.")

    st.subheader("🤝 Eşleşme Geçmişi")
    if matches[student_id]:
        df_match = pd.DataFrame(matches[student_id])
        st.table(df_match)
    else:
        st.info("Bu öğrenci henüz kimseyle eşleşmemiş.")
