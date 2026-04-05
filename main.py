import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="Mg. Omar Saleh AI", page_icon="🎓", layout="wide")

# تنسيق واجهة المستخدم (CSS)
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        height: 3.5em;
        background-color: #262730;
        color: white;
        border: 1px solid #FFD700;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #FFD700;
        color: black;
    }
    h1 {
        color: #FFD700;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# العنوان الرئيسي
st.markdown("<h1>✨ Mg. Omar Saleh AI ✨</h1>", unsafe_allow_html=True)

# ترتيب المدخلات
col1, col2 = st.columns(2)
with col1:
    subject = st.text_input("📚 اسم المادة أو الكتاب")
with col2:
    topic = st.text_input("📝 اسم الموضوع")

raw_text = st.text_area("✒️ ضع النص هنا لتبدأ المعالجة...", height=200)

st.markdown("---")
st.subheader("🛠️ اختر نوع المهمة")

# توزيع الأزرار بشكل منتظم
c1, c2, c3 = st.columns(3)
with c1:
    if st.button("🪄 1. التنسيق (AI)"):
        st.info("جاري التنسيق...")
with c2:
    if st.button("📋 2. التلخيص (ترتيب)"):
        st.warning("جاري التلخيص...")
with c3:
    if st.button("📝 3-أ. اختبار ST"):
        st.success("جاري إنشاء الاختبار...")

c4, c5, c6 = st.columns(3)
with c4:
    if st.button("🧐 3-ب. اختبار H"):
        st.info("جاري إعداد الأسئلة...")
with c5:
    if st.button("🖨️ 5. طباعة المحتوى"):
        st.write("تم التجهيز للطباعة")
with c6:
    if st.button("📊 4. الرسوم البيانية"):
        st.error("ميزة قيد التطوير")

st.markdown("---")
st.caption("حقوق الملكية © 2026 | Mg. Omar Saleh")
