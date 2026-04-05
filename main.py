import streamlit as st
import time
import google.generativeai as genai

# 1. إعدادات الصفحة
st.set_page_config(page_title="Mg. Omar Saleh AI", page_icon="🎓", layout="wide")

# 2. ربط الذكاء الاصطناعي (حط مفتاحك هنا)
# امسح الكلمة اللي بين القوسين وحط مفتاحك اللي بيبدأ بـ AIza
genai.configure(api_key="AIzaSyC0E0SxmAws2daFLPAgVoZMJW0ClcpWEnU") 
model = genai.GenerativeModel('gemini-pro')

# 3. إدارة الألوان والمهام
if 'task' not in st.session_state: st.session_state.task = None
if 'f_color' not in st.session_state: st.session_state.f_color = "#FFD700"

# تصميم احترافي
st.markdown(f"""
    <style>
    .main {{ background-color: #0e1117; }}
    h1 {{ color: {st.session_state.f_color}; text-align: center; border: 2px solid {st.session_state.f_color}; padding: 10px; border-radius: 15px; }}
    .stButton>button {{ width: 100%; border-radius: 10px; font-weight: bold; transition: 0.3s; height: 3em; }}
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1>✨ Mg. Omar Saleh AI ✨</h1>", unsafe_allow_html=True)

# 4. المدخلات
c_a, c_b = st.columns(2)
with c_a: sub = st.text_input("📚 المادة")
with c_b: top = st.text_input("📝 الموضوع")
txt = st.text_area("✒️ النص القانوني:", height=150)

st.markdown("---")

# 5. أزرار المهام (5 أزرار)
st.subheader("🛠️ المهام")
t1, t2, t3, t4, t5 = st.columns(5)
with t1: 
    if st.button("🪄 تنسيق"): st.session_state.task = "format"
with t2: 
    if st.button("📋 تلخيص"): st.session_state.task = "summary"
with t3: 
    if st.button("📝 اختبار ST"): st.session_state.task = "test1"
with t4: 
    if st.button("🧐 اختبار H"): st.session_state.task = "test2"
with t5: 
    if st.button("🖨️ طباعة"): st.session_state.task = "print"

# 6. أزرار الألوان (5 أزرار)
st.subheader("🎨 الألوان")
l1, l2, l3, l4, l5 = st.columns(5)
with l1: 
    if st.button("🟡 ذهبي"): st.session_state.f_color = "#FFD700"
with l2: 
    if st.button("🔵 أزرق"): st.session_state.f_color = "#3498db"
with l3: 
    if st.button("🟢 أخضر"): st.session_state.f_color = "#2ecc71"
with l4: 
    if st.button("🔴 أحمر"): st.session_state.f_color = "#e74c3c"
with l5: 
    if st.button("⚪ افتراضي"): st.session_state.f_color = "#FFFFFF"

st.markdown("---")

# 7. زر بدء العمل
if st.button("🚀 بدء العمل الآن"):
    if not st.session_state.task:
        st.error("اختار مهمة الأول!")
    elif not txt:
        st.warning("دخل نص الأول!")
    else:
        start = time.time()
        with st.spinner("جاري التنفيذ..."):
            if st.session_state.task == "format":
                res = model.generate_content(f"نسق النص ده: {txt}")
                st.info(res.text)
            elif st.session_state.task == "summary":
                res = model.generate_content(f"لخص النص ده: {txt}")
                st.warning(res.text)
            elif st.session_state.task == "print":
                st.code(txt)
            # باقي المهام تعمل بنفس الطريقة
        st.caption(f"تم في {round(time.time()-start, 2)} ثانية")
