import streamlit as st

# 1. إعدادات الصفحة الأساسية
st.set_page_config(page_title="Mg. Omar Saleh", layout="wide")

# 2. استدعاء المكتبات الخارجية والتنسيقات (CSS & HTML)
st.markdown("""
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    
    html, body, [data-testid="stSidebar"], .stApp {
        font-family: 'Cairo', sans-serif;
        background-color: #0E1117;
        color: #FFFFFF;
        direction: rtl;
    }

    /* تصميم المربع والمكعب ذو الأطراف الدائرية للنقاط الأساسية */
    .point-container {
        display: flex;
        align-items: center;
        margin-bottom: 10px;
    }
    .point-number {
        background-color: #FF4B4B;
        color: white;
        padding: 5px 15px;
        border-radius: 10px;
        margin-left: 10px;
        font-weight: bold;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
    }
    .point-text {
        background-color: #2E7D32;
        color: white;
        padding: 5px 20px;
        border-radius: 10px;
        flex-grow: 1;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
    }

    /* تصميم الأزرار الستة */
    .stButton > button {
        width: 100%;
        border-radius: 12px;
        height: 3em;
        background-color: #262730;
        border: 1px solid #4B4B4B;
        transition: 0.3s;
    }
    .stButton > button:hover {
        border-color: #FFD700;
        box-shadow: 0px 0px 10px #FFD700;
    }
    </style>
""", unsafe_allow_html=True)

# 3. العنوان الرئيسي
st.markdown('<h1 style="text-align:center; color:#FFD700;">✨ Mg. Omar Saleh AI ✨</h1>', unsafe_allow_html=True)

# 4. شريط التحكم الجانبي (المواصفات المطلوبة في مكان لوحده)
with st.sidebar:
    st.header("⚙️ إعدادات العرض")
    brightness = st.slider("🔅 درجة السطوع", 0.1, 1.0, 0.9)
    frame_width = st.slider("📏 حجم عرض الإطار", 1, 10, 2)
    page_count = st.number_input("📑 عدد الصفحات المستهدف", 1, 100, 1)
    
    st.write("---")
    if st.button("🖼️ اختيار إطار زخرفي"):
        st.info("الأطر المتاحة: (إطار كلاسيكي، إطار قانوني مذهب، إطار تعليمي حديث)")

# 5. بيانات العمل المطلوب (المدخلات)
st.markdown('### <i class="fas fa-edit"></i> بيانات العمل الإداري', unsafe_allow_html=True)
col_a, col_b = st.columns(2)
with col_a:
    subject_name = st.text_input("📚 اسم المادة أو الكتاب")
with col_b:
    topic_name = st.text_input("🖋️ اسم الموضوع")

raw_text = st.text_area("📄 النص الخام أو العشوائي", height=200, placeholder="ضع النص هنا...")

# 6. توزيع الأزرار (المهام)
st.write("---")
st.markdown('### <i class="fas fa-tasks"></i> اختر نوع المهمة')

c1, c2, c3, c4 = st.columns(4)
with c1:
    task_format = st.button("🪄 1. التنسيق (AI)")
with c2:
    task_summary = st.button("📝 2. التلخيص (ترتيب)")
with c3:
    task_st = st.button("🤖 3-أ. اختبار ST")
with c4:
    task_h = st.button("✍️ 3-ب. اختبار H")

c5, c6 = st.columns(2)
with c5:
    task_graph = st.button("📊 4. الرسوم البيانية")
with c6:
    print_page = st.button("🖨️ 5. طباعة المحتوى")

# 7. منطق التنفيذ (Logic)
if task_summary:
    st.markdown(f"## {topic_name}")
    lines = raw_text.split('.') # تقسيم بسيط للنص
    for i, line in enumerate(lines):
        if line.strip():
            st.markdown(f"""
                <div class="point-container">
                    <div class="point-number">{i+1}</div>
                    <div class="point-text">{line.strip()}</div>
                </div>
            """, unsafe_allow_html=True)

if task_h:
    st.markdown("### ✍️ اختبار يدوي (H) بناءً على النص")
    st.write("1. (صح/خطأ): هل النص يتناول موضوع السيادة؟")
    st.write("2. (اختياري): ما هو الركن الأساسي المذكور؟")
    st.write("3. (مقال): اشرح بالتفصيل وجهة نظر الكاتب في النص.")

if print_page:
    st.warning("اضغط Ctrl + P من لوحة المفاتيح لبدء الطباعة الفورية.")

# تذييل الصفحة
st.markdown("<br><hr><p style='text-align:center;'>حقوق الملكية © Mg. Omar Saleh | 2026</p>", unsafe_allow_html=True)
