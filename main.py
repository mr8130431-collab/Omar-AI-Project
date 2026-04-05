import streamlit as st

# إعدادات الصفحة
st.set_page_config(page_title="Mg. Omar Saleh AI", page_icon="🎓", layout="wide")

# تنسيق واجهة المستخدم (CSS) لإخفاء الأكواد وتحسين الشكل
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        height: 3em;
        background-color: #4B4B4B;
        color: white;
        border: 1px solid #FFD700;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #FFD700;
        color: black;
    }
    h1 {
        color: #FFD700;
        text-align: center;
        font-family: 'Arial';
    }
    .status-box {
        padding: 10px;
        border-radius: 10px;
        border: 1px solid #4B4B4B;
        margin-bottom: 10px;
    }
    </style>
    """, unsafe_allow_ Harris_true)

# العنوان الرئيسي
st.markdown("<h1>✨ Mg. Omar Saleh AI ✨</h1>", unsafe_allow_html=True)

# تقسيم الصفحة لمدخلات منظمة
col1, col2 = st.columns(2)
with col1:
    subject = st.text_input("📚 اسم المادة أو الكتاب")
with col2:
    topic = st.text_input("📝 اسم الموضوع")

# منطقة النص الخام
raw_text = st.text_area("✒️ ضع النص هنا لتبدأ المعالجة...", height=200)

st.markdown("---")
st.subheader("🛠️ اختر نوع المهمة")

# توزيع الأزرار بشكل احترافي
btn_col1, btn_col2, btn_col3 = st.columns(3)
with btn_col1:
    if st.button("🪄 1. التنسيق (AI)"):
        st.info("جاري تنسيق النص...")
with btn_col2:
    if st.button("📋 2. التلخيص (ترتيب)"):
        st.warning("جاري التلخيص...")
with btn_col3:
    if st.button("📝 3-أ. اختبار ST"):
        st.success("جاري إنشاء الاختبار...")

btn_col4, btn_col5, btn_col6 = st.columns(3)
with btn_col4:
    if st.button("🧐 3-ب. اختبار H"):
        st.info("جاري إعداد الأسئلة...")
with btn_col5:
    if st.button("🖨️ 5. طباعة المحتوى"):
        st.write("تم تجهيز النسخة للطباعة")
with btn_col6:
    if st.button("📊 4. الرسوم البيانية"):
        st.error("هذه الميزة قيد التطوير")

st.markdown("---")
st.caption("حقوق الملكية © 2026 | Mg. Omar Saleh")
