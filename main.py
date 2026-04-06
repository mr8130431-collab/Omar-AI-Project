import streamlit as st
import google.generativeai as genai

# --- إعداد الصفحة ---
st.set_page_config(page_title="مساعدك الذكي", layout="centered")

# --- جلب المفتاح من Secrets ---
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
except Exception as e:
    st.error("خطأ: لم يتم العثور على مفتاح الـ API في الإعدادات.")
    st.stop()

# تعريف النموذج (تحديث لتجنب خطأ 404)
model = genai.GenerativeModel('gemini-2.0-flash-exp')

# --- تنسيق الأزرار (كل سطر 3 أزرار) ---
# السطر الأول
col1, col2, col3 = st.columns(3)
with col1:
    btn1 = st.button("علم الأدب")
with col2:
    btn2 = st.button("علم اللغة")
with col3:
    btn3 = st.button("الأحكام الشرعية")

# السطر الثاني
col4, col5, col6 = st.columns(3)
with col4:
    btn4 = st.button("القانون الدولي")
with col5:
    btn5 = st.button("أصول الفقه")
with col6:
    btn6 = st.button("تلخيص مواد")

# إضافة مسافة سطرين كما طلبت
st.write("\n\n")
st.write("\n\n")

# زر بدء العمل في المنتصف
col_left, col_mid, col_right = st.columns([1, 2, 1])
with col_mid:
    start_btn = st.button("🚀 بدء العمل الآن", use_container_width=True)

# --- منطق التشغيل ---
user_input = st.text_input("اسأل أي شيء:", placeholder="اكتب سؤالك هنا...")

# تحديد النص بناءً على الزر المضغوط أو الكتابة
final_query = ""
if btn1: final_query = "اشرح لي في علم الأدب: " + user_input
if btn2: final_query = "اشرح لي في علم اللغة: " + user_input
if btn3: final_query = "اشرح لي في الأحكام الشرعية: " + user_input
# ... وهكذا لبقية الأزرار

if start_btn or st.button("إرسال"):
    if user_input or final_query:
        with st.spinner('جاري التفكير...'):
            try:
                response = model.generate_content(final_query if final_query else user_input)
                st.success("الرد:")
                st.write(response.text)
            except Exception as e:
                st.error(f"حدث خطأ: {e}")
    else:
        st.warning("يرجى كتابة سؤال أولاً!")
