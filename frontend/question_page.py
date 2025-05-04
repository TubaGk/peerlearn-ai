import streamlit as st

def mock_ai_answer(question):
    """Soruya göre basit bir yapay zeka cevabı taklidi döndürür."""
    if "asit" in question.lower():
        return "Asitler, suda çözündüğünde H+ iyonu veren maddelerdir. Örneğin, hidroklorik asit (HCl)."
    elif "iyon" in question.lower():
        return "İyon, elektron almış ya da vermiş atom ya da moleküldür. Pozitif yüklü iyonlara katyon, negatiflere anyon denir."
    elif "türev" in question.lower():
        return "Türev, bir fonksiyonun değişim hızını gösterir. Eğri üzerindeki eğimin ölçüsüdür."
    else:
        return "Bu konuda sana yardımcı olabilirim, ancak lütfen biraz daha detaylı bir soru sor."

def show():
    st.title("❓ AI'ye Soru Sor")

    st.markdown("Zorlandığın konularla ilgili AI'ye istediğin soruyu yazabilirsin.")

    question = st.text_area("Sorunu buraya yaz:", height=150, placeholder="Örnek: Asit nedir?")

    if st.button("AI'ye Sor"):
        if question.strip():
            with st.spinner("AI cevabı hazırlanıyor..."):
                answer = mock_ai_answer(question)
                st.markdown("### 💬 AI Cevabı:")
                st.success(answer)
        else:
            st.warning("Lütfen önce bir soru yazınız.")
