import streamlit as st
import google.generativeai as genai

# --- إعداد الصفحة ---
st.set_page_config(page_title="مساعد الذكاء الاصطناعي", page_icon="🚀")

# --- جلب المفتاح من Secrets ---
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
except Exception as e:
    st.error("خطأ: لم يتم العثور على مفتاح الـ API في الإعدادات (Secrets).")
    st.stop()

# --- تعريف النموذج (الاسم المحدث لتجنب خطأ 404) ---
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🚀 بدء العمل الآن")

# خانة إدخال النص
user_input = st.text_input("اسأل أي شيء:", placeholder="اكتب سؤالك هنا...")

if st.button("إرسال"):
    if user_input:
        with st.spinner('جاري التفكير...'):
            try:
                # طلب الرد من Gemini
                response = model.generate_content(user_input)
                
                # عرض الرد
                st.markdown("### الرد:")
                st.write(response.text)
                
            except Exception as e:
                # إذا ظهر خطأ 404 هنا، تأكد من تحديث المكتبة في requirements.txt
                st.error(f"حدث خطأ أثناء الاتصال بالذكاء الاصطناعي: {e}")
    else:
        st.warning("من فضلك اكتب سؤالاً أولاً.")
