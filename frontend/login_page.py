import streamlit as st

def show():
    st.title("🔐 Giriş Yap")

    st.markdown("Lütfen sisteme giriş yapın. Bu sayfa şimdilik oturumu sadece simüle eder.")

    email = st.text_input("E-posta")
    password = st.text_input("Şifre", type="password")
    user_type = st.selectbox("Kullanıcı Tipi", ["Öğrenci", "Öğretmen"])

    if st.button("Giriş Yap"):
        if email and password:
            st.session_state["logged_in"] = True
            st.session_state["email"] = email
            st.session_state["user_type"] = user_type
            st.success(f"Hoş geldin, {user_type}! 🎉")
        else:
            st.warning("Lütfen tüm alanları doldurun.")

    # Oturum açık ise mesaj göster
    if st.session_state.get("logged_in"):
        st.info(f"Giriş yapıldı: {st.session_state['email']} ({st.session_state['user_type']})")
