# -*- coding: utf-8 -*-
"""
منصة تفاعلية متقدمة عن التقنية والذكاء الاصطناعي للمرحلة الثانوية
أكاديمية نمو العالي للتدريب - Numo Academy
تشغيل: streamlit run app.py
"""

import streamlit as st
import time
from datetime import datetime
import base64
import requests
import qrcode
from io import BytesIO

# ---------------------------------------------------------
# إعدادات الصفحة العامة
# ---------------------------------------------------------
st.set_page_config(
    page_title="مستقبل التقنية والذكاء الاصطناعي 🚀",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# رابط Google Apps Script Web App المعتمد
GOOGLE_SHEET_WEB_APP_URL = "https://script.google.com/macros/s/AKfycbzmib9hadMZDIK70vxzb9HlNFTnL6jS4KZgp_b0CuPWJ4-kIQ-KKxJc-Sg-buL1MA_z/exec"

def get_image_base64(path):
    try:
        with open(path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode("utf-8")
    except Exception:
        return ""

logo_base64 = get_image_base64("logo.jpg")

# ---------------------------------------------------------
# دعم الـ URL المباشر (Query Parameters) لفتح صفحة المسابقة فوراً
# ---------------------------------------------------------
query_params = st.query_params
is_quiz_url = query_params.get("page", "") == "quiz"

if "current_page" not in st.session_state:
    if is_quiz_url:
        st.session_state.current_page = "🎯 التحدي التقني والمسابقة"
    else:
        st.session_state.current_page = "🏠 الرئيسية"

# ---------------------------------------------------------
# تنسيقات CSS: ضبط العرض والشاشات وتجنب أي تداخل
# ---------------------------------------------------------
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;900&display=swap');

    html, body, [class*="css"], .stMarkdown, p, span, label, div, h1, h2, h3, h4, h5, h6 {{
        font-family: 'Tajawal', sans-serif !important;
        direction: rtl !important;
        text-align: right !important;
    }}

    .stApp {{
        background: radial-gradient(circle at 15% 0%, #1b1035 0%, transparent 45%),
                    radial-gradient(circle at 85% 15%, #072a3d 0%, transparent 50%),
                    linear-gradient(160deg, #05060f 0%, #0b0f2e 45%, #150a30 100%);
        background-attachment: fixed;
        color: #eef2ff !important;
    }}

    html, body {{
        overflow-x: hidden !important;
    }}

    .block-container {{
        padding-top: 3.5rem !important;
        padding-left: clamp(0.5rem, 2vw, 1.5rem) !important;
        padding-right: clamp(0.5rem, 2vw, 1.5rem) !important;
        max-width: 100% !important;
    }}

    .sphere-logo-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 8px 0;
        direction: ltr !important;
    }}

    .sphere-logo {{
        width: 85px;
        height: 85px;
        border-radius: 50%;
        object-fit: cover;
        border: 3px solid transparent;
        background:
            linear-gradient(#0b0f2e, #0b0f2e) padding-box,
            linear-gradient(135deg, #22d3ee, #a855f7, #f472b6) border-box;
        box-shadow: 0 0 18px rgba(168, 85, 247, 0.4);
        animation: horizontalSpin 6s linear infinite;
        transform-style: preserve-3d;
    }}

    @keyframes horizontalSpin {{
        0% {{ transform: rotateY(0deg); }}
        100% {{ transform: rotateY(360deg); }}
    }}

    .main-card {{
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
        border: 1px solid rgba(255, 255, 255, 0.10);
        border-radius: 16px;
        padding: 16px;
        margin-top: 8px;
        margin-bottom: 15px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
        color: #eef2ff !important;
    }}

    .fun-card {{
        background: rgba(255, 255, 255, 0.045);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 12px;
        padding: 14px;
        margin: 10px 0;
        box-shadow: 0 4px 16px rgba(0,0,0,0.25);
        border-right: 4px solid #22d3ee;
        border-top: 1px solid rgba(255,255,255,0.06);
        border-bottom: 1px solid rgba(255,255,255,0.06);
        border-left: 1px solid rgba(255,255,255,0.06);
        color: #eef2ff !important;
    }}

    .fun-card h3, .fun-card h4 {{
        background: linear-gradient(90deg, #22d3ee, #a855f7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: block;
        margin-bottom: 6px;
    }}

    .title-glow {{
        font-size: clamp(18px, 4.2vw, 32px);
        font-weight: 900;
        background: linear-gradient(90deg, #22d3ee, #a855f7, #f472b6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: right;
        line-height: 1.35;
    }}

    .subtitle {{
        text-align: right;
        color: #94a3b8;
        font-size: clamp(11px, 2.2vw, 13px);
    }}

    input[type="text"] {{
        background-color: #0b0f2e !important;
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        font-size: 16px !important;
        font-weight: 700 !important;
        border: 2px solid #22d3ee !important;
        border-radius: 10px !important;
        text-align: right !important;
        padding: 10px 14px !important;
    }}
    
    .stTextInput label {{
        color: #e2e8f0 !important;
        font-weight: 700 !important;
        font-size: 14px !important;
    }}

    .stButton>button, .stFormSubmitButton>button {{
        background: linear-gradient(90deg, #0ea5e9, #a855f7);
        color: white;
        font-weight: 700;
        font-size: 15px;
        border-radius: 10px;
        padding: 10px 18px;
        border: none;
        box-shadow: 0 4px 14px rgba(168, 85, 247, 0.35);
        width: 100%;
        min-height: 44px;
    }}
    .stButton>button:hover {{
        color: white !important;
    }}

    section[data-testid="stSidebar"] {{
        background: linear-gradient(180deg, #05060f, #150a30);
        border-left: 1px solid rgba(255,255,255,0.08);
    }}
    section[data-testid="stSidebar"] * {{
        color: #eef2ff !important;
    }}

    @media (max-width: 768px) {{
        div[data-testid="column"] {{
            width: 100% !important;
            flex: 1 1 100% !important;
            margin-bottom: 10px;
        }}
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# الشريط الجانبي للتنقل
# ---------------------------------------------------------
pages_list = [
    "🏠 الرئيسية",
    "💡 أساسيات التحول الرقمي",
    "🤖 تقنيات الذكاء الاصطناعي المتقدمة",
    "🔒 الأمن السيبراني والأخلاقيات",
    "🧪 مختبر الذكاء الاصطناعي",
    "🎯 التحدي التقني والمسابقة",
]

if st.session_state.current_page not in pages_list:
    st.session_state.current_page = "🏠 الرئيسية"

with st.sidebar:
    if logo_base64:
        st.markdown(
            f"""
            <div class="sphere-logo-container">
                <img src="data:image/jpeg;base64,{logo_base64}" class="sphere-logo">
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.markdown("<h3 style='text-align:center; color:#22d3ee; margin-top:5px;'>أكاديمية نمو العالي</h3>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown("### 🧭 أقسام المنصة")

    selected_page = st.radio(
        "اختر القسم التعليمي:",
        pages_list,
        index=pages_list.index(st.session_state.current_page),
        key="sidebar_navigation",
    )
    
    if selected_page != st.session_state.current_page:
        st.session_state.current_page = selected_page
        if selected_page == "🎯 التحدي التقني والمسابقة":
            st.query_params["page"] = "quiz"
        else:
            if "page" in st.query_params:
                del st.query_params["page"]
        st.rerun()

    st.markdown("---")
    st.markdown("<p style='text-align:center; font-size:12px; color:#94a3b8;'>مخصص لطلبة المرحلة الثانوية 🎓</p>", unsafe_allow_html=True)

# ---------------------------------------------------------
# رأس الصفحة المشترك
# ---------------------------------------------------------
col1, col2 = st.columns([4, 1])
with col2:
    if logo_base64:
        st.markdown(
            f"""
            <div class="sphere-logo-container" style="margin:0;">
                <img src="data:image/jpeg;base64,{logo_base64}" class="sphere-logo" style="width:50px; height:50px;">
            </div>
            """,
            unsafe_allow_html=True,
        )
with col1:
    st.markdown('<div class="title-glow">منصة الابتكار الرقمي والذكاء الاصطناعي</div>', unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>أكاديمية نمو العالي للتدريب — المرحلة الثانوية</p>", unsafe_allow_html=True)

st.markdown("---")

if "lab_history" not in st.session_state:
    st.session_state.lab_history = []

page = st.session_state.current_page

# ===========================================================
# الرئيسية
# ===========================================================
if page == "🏠 الرئيسية":
    st.markdown(
        """
        <div class="main-card" style="text-align:center;">
        <h2>مرحبًا بك في بوابة قادة المستقبل الرقمي! 🚀</h2>
        <p style="font-size:15px; color:#cbd5e1; line-height:1.7;">
        نعيش اليوم ثورة تكنولوجية غير مسبوقة يقودها الذكاء الاصطناعي، الحوسبة السحابية، وتحليل البيانات الضخمة.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="fun-card" style="text-align: center; border-right: 4px solid #a855f7;">
        <h3>🏆 المسابقة والتحدي التقني المباشر</h3>
        <p style="font-size: 14px;">شارك في التحدي واختبر معلوماتك الآن عبر الزر أو مسح الرمز أدناه!</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    if st.button("🚀 الانتقال المباشر لصفحة المسابقة"):
        st.session_state.current_page = "🎯 التحدي التقني والمسابقة"
        st.query_params["page"] = "quiz"
        st.rerun()

    # توليد ورسم QR Code مباشر لصفحة المسابقة
    try:
        current_base_url = st.context.headers.get("Host", "localhost:8501")
        quiz_url = f"https://{current_base_url}/?page=quiz"
        
        qr = qrcode.QRCode(box_size=4, border=2)
        qr.add_data(quiz_url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        qr_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
        
        st.markdown(
            f"""
            <div style="text-align: center; margin-top: 15px;">
            <p style="font-size: 13px; color: #94a3b8;">امسح رمز الاستجابة السريعة (QR) بكاميرا الجوال لفتح صفحة المسابقة مباشرة:</p>
            <img src="data:image/png;base64,{qr_base64}" style="width: 130px; border-radius: 8px; border: 2px solid #22d3ee; padding: 4px; background: white;">
            </div>
            """,
            unsafe_allow_html=True,
        )
    except Exception:
        pass

# ===========================================================
# أساسيات التحول الرقمي
# ===========================================================
elif page == "💡 أساسيات التحول الرقمي":
    st.markdown('<div class="main-card"><h2>💡 أساسيات التحول الرقمي</h2><p>استكشاف الحوسبة السحابية وإنترنت الأشياء.</p></div>', unsafe_allow_html=True)

# ===========================================================
# تقنيات الذكاء الاصطناعي المتقدمة
# ===========================================================
elif page == "🤖 تقنيات الذكاء الاصطناعي المتقدمة":
    st.markdown('<div class="main-card"><h2>🤖 تقنيات الذكاء الاصطناعي</h2><p>التعلم العميق والشبكات العصبية.</p></div>', unsafe_allow_html=True)

# ===========================================================
# الأمن السيبراني والأخلاقيات
# ===========================================================
elif page == "🔒 الأمن السيبراني والأخلاقيات":
    st.markdown('<div class="main-card"><h2>🔒 الأمن السيبراني</h2><p>حماية البيانات وأخلاقيات التقنية.</p></div>', unsafe_allow_html=True)

# ===========================================================
# مختبر الذكاء الاصطناعي
# ===========================================================
elif page == "🧪 مختبر الذكاء الاصطناعي":
    st.markdown('<div class="main-card"><h2>🧪 مختبر التصنيف الذكي</h2></div>', unsafe_allow_html=True)
    user_query = st.text_input("📝 اكتب استفسارك التقني:", key="lab_query_input")
    if user_query:
        st.markdown(f'<div class="fun-card"><h3>النتيجة:</h3><p>مصطلح تقني تم تحليله بنجاح.</p></div>', unsafe_allow_html=True)

# ===========================================================
# التحدي التقني والمسابقة (صفحة مستقلة برابط مباشر)
# ===========================================================
elif page == "🎯 التحدي التقني والمسابقة":
    if st.button("⬅️ العودة للرئيسية"):
        st.session_state.current_page = "🏠 الرئيسية"
        if "page" in st.query_params:
            del st.query_params["page"]
        st.rerun()

    st.markdown('<div class="main-card"><h2>🎯 التحدي التقني النهائي وسحب الأكاديمية</h2></div>', unsafe_allow_html=True)

    with st.form("competition_form"):
        st.markdown("### بيانات المتسابق:")
        participant_name = st.text_input("👤 الاسم الكامل:", key="comp_name")
        participant_phone = st.text_input("📱 رقم الجوال (مثال: 05XXXXXXXX):", key="comp_phone")

        st.markdown("---")
        st.markdown("### أسئلة التحدي:")

        questions = [
            {
                "q": "1. مؤسسة تريد تحليل سلوك آلاف العملاء دون تصنيفات مسبقة لبياناتهم، فما نوع التعلم الآلي الأنسب؟",
                "options": ["تعلم موجَّه", "تعلم غير موجَّه", "تعلم تعزيزي"],
                "answer": "تعلم غير موجَّه",
                "explain": "التعلم غير الموجَّه يكتشف الأنماط والتجمعات في البيانات تلقائياً.",
            },
            {
                "q": "2. خدمة سحابية توفر بيئة جاهزة لتطوير وتشغيل التطبيقات دون إدارة خوادم:",
                "options": ["IaaS", "PaaS", "SaaS"],
                "answer": "PaaS",
                "explain": "منصة كخدمة (PaaS) مخصصة لتشغيل وتطوير التطبيقات بسهولة.",
            },
            {
                "q": "3. رسالة تطلب تحديث بياناتك البنكي عبر رابط غريب تمثل هجوم:",
                "options": ["برمجية فدية", "تصيّد احتيالي (Phishing)", "حجب خدمة"],
                "answer": "تصيّد احتيالي (Phishing)",
                "explain": "التصيد الاحتيالي يخدع المستخدم لسرقة بياناته.",
            },
        ]

        answers = []
        for i, item in enumerate(questions):
            st.markdown(f'<div class="fun-card"><h4>{item["q"]}</h4></div>', unsafe_allow_html=True)
            ans = st.radio("اختر الإجابة:", item["options"], index=None, key=f"q{i}_radio")
            answers.append(ans)

        submitted = st.form_submit_button("🚀 إرسال الإجابات وتسجيل المشاركة")

        if submitted:
            if not participant_name.strip() or not participant_phone.strip():
                st.error("⚠️ الرجاء إدخال الاسم ورقم الجوال بشكل صحيح.")
            elif any(a is None for a in answers):
                st.error("⚠️ الرجاء الإجابة على جميع الأسئلة.")
            else:
                score = sum(1 for a, item in zip(questions, answers) if a == item["answer"])

                st.success(f"🎉 شكرًا لك يا {participant_name}! تم استلام إجاباتك بنجاح.")
                st.markdown(
                    f"""
                    <div class="fun-card" style="text-align:center;">
                    <h3>📊 نتيجتك النهائية:</h3>
                    <h1 style="color:#22d3ee;">{score} / {len(questions)}</h1>
                    <p>تم حفظ بياناتك وجوالك ({participant_phone}) في سحابة الأكاديمية.</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                if score == len(questions):
                    st.balloons()
                    st.markdown("<h3 style='text-align:center; color:#4ade80;'>🏆 أداء ممتاز! اجتزت التحدي بجدارة.</h3>", unsafe_allow_html=True)

                try:
                    payload = {
                        "name": participant_name,
                        "phone": participant_phone,
                        "score": score,
                        "total": len(questions),
                        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    }
                    if GOOGLE_SHEET_WEB_APP_URL != "ضع_رابط_ويب_جوجل_هنا":
                        requests.post(GOOGLE_SHEET_WEB_APP_URL, json=payload, timeout=5)
                except Exception as e:
                    print(f"خطأ: {e}")

# ---------------------------------------------------------
# تذييل الصفحة
# ---------------------------------------------------------
st.markdown("---")
st.markdown(
    """
    <div style="text-align:center; color:#94a3b8; font-size:12px;">
    🎓 أكاديمية نمو العالي للتدريب © 2026 — بناء القدرات الرقمية لشباب المستقبل 🌟
    </div>
    """,
    unsafe_allow_html=True,
)# -*- coding: utf-8 -*-
"""
منصة تفاعلية متقدمة عن التقنية والذكاء الاصطناعي للمرحلة الثانوية
أكاديمية نمو العالي للتدريب - Numo Academy
تشغيل: streamlit run app.py
"""

import streamlit as st
import time
from datetime import datetime
import base64
import requests
import qrcode
from io import BytesIO

# ---------------------------------------------------------
# إعدادات الصفحة العامة
# ---------------------------------------------------------
st.set_page_config(
    page_title="مستقبل التقنية والذكاء الاصطناعي 🚀",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

# رابط Google Apps Script Web App المعتمد
GOOGLE_SHEET_WEB_APP_URL = "https://script.google.com/macros/s/AKfycbzmib9hadMZDIK70vxzb9HlNFTnL6jS4KZgp_b0CuPWJ4-kIQ-KKxJc-Sg-buL1MA_z/exec"

def get_image_base64(path):
    try:
        with open(path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode("utf-8")
    except Exception:
        return ""

logo_base64 = get_image_base64("logo.jpg")

# ---------------------------------------------------------
# التحقق من الرابط المباشر (Query Parameters)
# ---------------------------------------------------------
query_params = st.query_params
is_quiz_url = query_params.get("page", "") == "quiz"

# ---------------------------------------------------------
# تنسيقات CSS: ضمان وضوح النصوص وعدم وجود فراغات
# ---------------------------------------------------------
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;500;700;900&display=swap');

    html, body, [class*="css"], .stMarkdown, p, span, label, div, h1, h2, h3, h4, h5, h6 {{
        font-family: 'Tajawal', sans-serif !important;
        direction: rtl !important;
        text-align: right !important;
    }}

    .stApp {{
        background: radial-gradient(circle at 15% 0%, #1b1035 0%, transparent 45%),
                    radial-gradient(circle at 85% 15%, #072a3d 0%, transparent 50%),
                    linear-gradient(160deg, #05060f 0%, #0b0f2e 45%, #150a30 100%);
        background-attachment: fixed;
        color: #eef2ff !important;
    }}

    html, body {{
        overflow-x: hidden !important;
    }}

    .block-container {{
        padding-top: 4rem !important;
        padding-left: clamp(0.6rem, 3vw, 2rem) !important;
        padding-right: clamp(0.6rem, 3vw, 2rem) !important;
        max-width: 100% !important;
    }}

    .sphere-logo-container {{
        perspective: 1000px;
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 10px 0;
        direction: ltr !important;
    }}

    .sphere-logo {{
        width: 90px;
        height: 90px;
        border-radius: 50%;
        object-fit: cover;
        border: 3px solid transparent;
        background:
            linear-gradient(#0b0f2e, #0b0f2e) padding-box,
            linear-gradient(135deg, #22d3ee, #a855f7, #f472b6) border-box;
        box-shadow: 0 0 20px rgba(168, 85, 247, 0.4);
        animation: horizontalSpin 6s linear infinite;
        transform-style: preserve-3d;
    }}

    @keyframes horizontalSpin {{
        0% {{ transform: rotateY(0deg); }}
        100% {{ transform: rotateY(360deg); }}
    }}

    .main-card {{
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
        border: 1px solid rgba(255, 255, 255, 0.10);
        border-radius: 16px;
        padding: 16px;
        margin-top: 10px;
        margin-bottom: 15px;
        box-shadow: 0 8px 24px rgba(0,0,0,0.3);
        color: #eef2ff !important;
    }}

    .fun-card {{
        background: rgba(255, 255, 255, 0.045);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 14px;
        padding: 14px;
        margin: 10px 0;
        box-shadow: 0 4px 16px rgba(0,0,0,0.25);
        border-right: 4px solid #22d3ee;
        border-top: 1px solid rgba(255,255,255,0.06);
        border-bottom: 1px solid rgba(255,255,255,0.06);
        border-left: 1px solid rgba(255,255,255,0.06);
        color: #eef2ff !important;
    }}

    .fun-card h3, .fun-card h4 {{
        background: linear-gradient(90deg, #22d3ee, #a855f7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: block;
        margin-bottom: 6px;
    }}

    .title-glow {{
        font-size: clamp(18px, 4.2vw, 32px);
        font-weight: 900;
        background: linear-gradient(90deg, #22d3ee, #a855f7, #f472b6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: right;
        line-height: 1.4;
    }}

    .subtitle {{
        text-align: right;
        color: #94a3b8;
        font-size: clamp(11px, 2.2vw, 13px);
    }}

    input[type="text"] {{
        background-color: #0b0f2e !important;
        color: #ffffff !important;
        -webkit-text-fill-color: #ffffff !important;
        font-size: 16px !important;
        font-weight: 700 !important;
        border: 2px solid #22d3ee !important;
        border-radius: 12px !important;
        text-align: right !important;
        padding: 10px 14px !important;
    }}
    
    .stTextInput label {{
        color: #e2e8f0 !important;
        font-weight: 700 !important;
        font-size: 14px !important;
    }}

    .stButton>button, .stFormSubmitButton>button {{
        background: linear-gradient(90deg, #0ea5e9, #a855f7);
        color: white;
        font-weight: 700;
        font-size: 15px;
        border-radius: 12px;
        padding: 10px 20px;
        border: none;
        box-shadow: 0 4px 16px rgba(168, 85, 247, 0.35);
        width: 100%;
        min-height: 44px;
    }}
    .stButton>button:hover {{
        color: white !important;
    }}

    section[data-testid="stSidebar"] {{
        background: linear-gradient(180deg, #05060f, #150a30);
        border-left: 1px solid rgba(255,255,255,0.08);
    }}
    section[data-testid="stSidebar"] * {{
        color: #eef2ff !important;
    }}

    @media (max-width: 768px) {{
        div[data-testid="column"] {{
            width: 100% !important;
            flex: 1 1 100% !important;
            margin-bottom: 10px;
        }}
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# إدارة التنقل (عبر الـ URL أو الشريط الجانبي)
# ---------------------------------------------------------
if is_quiz_url:
    page = "🎯 التحدي التقني والمسابقة"
else:
    with st.sidebar:
        if logo_base64:
            st.markdown(
                f"""
                <div class="sphere-logo-container">
                    <img src="data:image/jpeg;base64,{logo_base64}" class="sphere-logo">
                </div>
                """,
                unsafe_allow_html=True,
            )
        else:
            st.image("logo.jpg", use_container_width=True)

        st.markdown(
            "<h3 style='text-align:center; background:linear-gradient(90deg,#22d3ee,#a855f7);"
            "-webkit-background-clip:text; -webkit-text-fill-color:transparent; margin-top:5px;'>"
            "أكاديمية نمو العالي</h3>",
            unsafe_allow_html=True,
        )
        st.markdown("---")
        st.markdown("### 🧭 أقسام المنصة")

        page = st.radio(
            "اختر القسم التعليمي:",
            [
                "🏠 الرئيسية",
                "💡 أساسيات التحول الرقمي",
                "🤖 تقنيات الذكاء الاصطناعي المتقدمة",
                "🔒 الأمن السيبراني والأخلاقيات",
                "🧪 مختبر الذكاء الاصطناعي",
                "🎯 التحدي التقني والمسابقة",
            ],
            key="main_navigation_safe",
        )

        st.markdown("---")
        st.markdown("<p style='text-align:center; font-size:12px; color:#94a3b8;'>مخصص لطلبة المرحلة الثانوية 🎓</p>", unsafe_allow_html=True)

# ---------------------------------------------------------
# رأس الصفحة المشترك
# ---------------------------------------------------------
col1, col2 = st.columns([4, 1])
with col2:
    if logo_base64:
        st.markdown(
            f"""
            <div class="sphere-logo-container" style="margin:0;">
                <img src="data:image/jpeg;base64,{logo_base64}" class="sphere-logo" style="width:50px; height:50px;">
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.image("logo.jpg", width=50)
with col1:
    st.markdown('<div class="title-glow">منصة الابتكار الرقمي والذكاء الاصطناعي</div>', unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>برنامج إثراء مهارات المستقبل للمرحلة الثانوية — أكاديمية نمو العالي</p>", unsafe_allow_html=True)

st.markdown("---")

if "lab_history" not in st.session_state:
    st.session_state.lab_history = []

# ===========================================================
# الرئيسية
# ===========================================================
if page == "🏠 الرئيسية":
    st.markdown(
        """
        <div class="main-card" style="text-align:center;">
        <span class="badge">بوابة التعلّم الرقمي</span>
        <h2>مرحبًا بك في بوابة مهندسي وقادة المستقبل الرقمي! 🚀</h2>
        <p style="font-size:15px; color:#cbd5e1; line-height:1.7;">
        نعيش اليوم ثورة تكنولوجية غير مسبوقة يقودها الذكاء الاصطناعي، الحوسبة السحابية، وتحليل البيانات الضخمة.
        هذه المنصة صُممت خصيصًا لتزويدك بالمفاهيم الأساسية والمتقدمة لمواكبة متطلبات سوق العمل الرقمي الحديث.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="fun-card" style="text-align: center; border-right: 4px solid #a855f7;">
        <h3>🏆 المسابقة والتحدي التقني</h3>
        <p style="font-size: 14px; margin-bottom: 10px;">اختبر معلوماتك وسجل مشاركتك في سحب الأكاديمية الآن!</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    if st.button("🚀 الانتقال المباشر إلى التحدي التقني والمسابقة"):
        st.query_params["page"] = "quiz"
        st.rerun()

    # توليد رمز QR مباشر لرابط المسابقة لكي يمسحه الطلاب بالجوال
    try:
        current_host = st.context.headers.get("Host", "localhost:8501")
        quiz_url = f"https://{current_host}/?page=quiz"
        
        qr = qrcode.QRCode(box_size=4, border=2)
        qr.add_data(quiz_url)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        
        buffered = BytesIO()
        img.save(buffered, format="PNG")
        qr_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
        
        st.markdown(
            f"""
            <div style="text-align: center; margin-top: 15px;">
            <p style="font-size: 13px; color: #94a3b8;">📱 أو امسح رمز الاستجابة السريعة (QR) بكاميرا الجوال لفتح المسابقة فوراً:</p>
            <img src="data:image/png;base64,{qr_base64}" style="width: 130px; border-radius: 8px; border: 2px solid #22d3ee; padding: 4px; background: white;">
            </div>
            """,
            unsafe_allow_html=True,
        )
    except Exception:
        pass

    st.markdown("<br>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="fun-card"><h3>🌐 التحول الرقمي</h3><p style="font-size: 14px;">البنى التحتية، إنترنت الأشياء، والحوسبة السحابية.</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="fun-card"><h3>🧠 نماذج الذكاء</h3><p style="font-size: 14px;">التعلم الآلي، الشبكات العصبية، ومعالجة اللغات.</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="fun-card"><h3>🛡️ أمن المعلومات</h3><p style="font-size: 14px;">التهديدات السيبرانية الشائعة وأخلاقيات التقنية.</p></div>', unsafe_allow_html=True)

# ===========================================================
# أساسيات التحول الرقمي
# ===========================================================
elif page == "💡 أساسيات التحول الرقمي":
    st.markdown('<div class="main-card"><h2>💡 أساسيات التحول الرقمي والتقنيات الناشئة</h2></div>', unsafe_allow_html=True)
    st.markdown('<div class="fun-card"><h3>ما هو التحول الرقمي؟</h3><p style="font-size:15px; line-height:1.7;">إعادة هندسة شاملة للعمليات والخدمات باستخدام التقنية لرفع الكفاءة.</p></div>', unsafe_allow_html=True)

# ===========================================================
# تقنيات الذكاء الاصطناعي المتقدمة
# ===========================================================
elif page == "🤖 تقنيات الذكاء الاصطناعي المتقدمة":
    st.markdown('<div class="main-card"><h2>🤖 عمق خوارزميات الذكاء الاصطناعي</h2></div>', unsafe_allow_html=True)
    st.markdown('<div class="fun-card"><h3>التعلم الآلي والعميق</h3><p style="font-size:15px; line-height:1.7;">اكتشاف الأنماط عبر الشبكات العصبية المتقدمة.</p></div>', unsafe_allow_html=True)

# ===========================================================
# الأمن السيبراني والأخلاقيات
# ===========================================================
elif page == "🔒 الأمن السيبراني والأخلاقيات":
    st.markdown('<div class="main-card"><h2>🔒 الأمن السيبراني وأخلاقيات التقنية</h2></div>', unsafe_allow_html=True)
    st.markdown('<div class="fun-card"><h3>سبل الحماية</h3><p style="font-size:15px; line-height:1.7;">التصدي للتهديدات الرقمية وتفعيل المصادقة الثنائية.</p></div>', unsafe_allow_html=True)

# ===========================================================
# مختبر الذكاء الاصطناعي
# ===========================================================
elif page == "🧪 مختبر الذكاء الاصطناعي":
    st.markdown('<div class="main-card"><h2>🧪 محاكي تصنيف النصوص بالكلمات المفتاحية</h2></div>', unsafe_allow_html=True)
    user_query = st.text_input("📝 اكتب جملة أو استفسارًا تقنيًا:", placeholder="مثال: كيف يحمي جدار الحماية الشبكة؟", key="lab_query_input")
    if user_query:
        st.markdown(f'<div class="fun-card"><h3>النتيجة</h3><p>تم تحليل النص بنجاح وإسناده للمجال التقني المناسب.</p></div>', unsafe_allow_html=True)

# ===========================================================
# التحدي التقني والمسابقة
# ===========================================================
elif page == "🎯 التحدي التقني والمسابقة":
    if is_quiz_url:
        if st.button("⬅️ العودة للرئيسية"):
            if "page" in st.query_params:
                del st.query_params["page"]
            st.rerun()

    st.markdown('<div class="main-card"><h2>🎯 التحدي التقني النهائي (اختبر معلوماتك وسجل بالمسابقة)</h2></div>', unsafe_allow_html=True)

    with st.form("competition_form"):
        st.markdown("### بيانات المتسابق:")
        participant_name = st.text_input("👤 الاسم الكامل:", key="comp_name")
        participant_phone = st.text_input("📱 رقم الجوال (مثال: 05XXXXXXXX):", key="comp_phone")

        st.markdown("---")
        st.markdown("### أسئلة التحدي:")

        questions = [
            {
                "q": "1. مؤسسة تريد تحليل سلوك آلاف العملاء دون تصنيفات مسبقة لبياناتهم، فما نوع التعلم الآلي الأنسب؟",
                "options": ["تعلم موجَّه (Supervised)", "تعلم غير موجَّه (Unsupervised)", "تعلم تعزيزي (Reinforcement)"],
                "answer": "تعلم غير موجَّه (Unsupervised)",
                "explain": "التعلم غير الموجَّه يكتشف الأنماط والتجمعات في البيانات دون تصنيفات مسبقة.",
            },
            {
                "q": "2. شركة ناشئة تريد إطلاق تطبيق بسرعة دون إدارة خوادمها، ما نوع الخدمة السحابية الأنسب؟",
                "options": ["IaaS", "PaaS", "SaaS"],
                "answer": "PaaS",
                "explain": "منصة كخدمة (PaaS) توفر بيئة جاهزة لتطوير ونشر التطبيقات مباشرة.",
            },
            {
                "q": "3. رسالة تطلب تحديث بياناتك البنكية عبر رابط غريب تمثل هجوم:",
                "options": ["برمجية فدية", "تصيّد احتيالي (Phishing)", "هجوم حجب خدمة"],
                "answer": "تصيّد احتيالي (Phishing)",
                "explain": "التصيد الاحتيالي يعتمد على خداع المستخدم لسرقة بياناته الشخصية أو البنكية.",
            },
        ]

        answers = []
        for i, item in enumerate(questions):
            st.markdown(f'<div class="fun-card"><h4>{item["q"]}</h4></div>', unsafe_allow_html=True)
            ans = st.radio("اختر الإجابة:", item["options"], index=None, key=f"q{i}_radio")
            answers.append(ans)

        submitted = st.form_submit_button("🚀 إرسال الإجابات وتسجيل المشاركة")

        if submitted:
            if not participant_name.strip() or not participant_phone.strip():
                st.error("⚠️ الرجاء إدخال الاسم ورقم الجوال بشكل صحيح قبل الإرسال.")
            elif any(a is None for a in answers):
                st.error("⚠️ الرجاء الإجابة على جميع الأسئلة قبل الإرسال.")
            else:
                score = sum(1 for a, item in zip(answers, questions) if a == item["answer"])

                st.success(f"🎉 شكرًا لك يا {participant_name}! تم استلام إجاباتك بنجاح.")
                st.markdown(
                    f"""
                    <div class="fun-card" style="text-align:center;">
                    <h3>📊 نتيجتك النهائية في التحدي:</h3>
                    <h1 style="color:#22d3ee;">{score} / {len(questions)}</h1>
                    <p>تم تسجيل بياناتك ({participant_phone}) في سجل الأكاديمية.</p>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )

                if score == len(questions):
                    st.balloons()
                    st.markdown("<h3 style='text-align:center; color:#4ade80;'>🏆 أداء ممتاز! لقد اجتزت التحدي بجدارة.</h3>", unsafe_allow_html=True)

                try:
                    payload = {
                        "name": participant_name,
                        "phone": participant_phone,
                        "score": score,
                        "total": len(questions),
                        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    }
                    if GOOGLE_SHEET_WEB_APP_URL != "ضع_رابط_ويب_جوجل_هنا":
                        requests.post(GOOGLE_SHEET_WEB_APP_URL, json=payload, timeout=5)
                except Exception as e:
                    print(f"خطأ في الاتصال بالسحابة: {e}")

# ---------------------------------------------------------
# تذييل الصفحة
# ---------------------------------------------------------
st.markdown("---")
st.markdown(
    """
    <div style="text-align:center; color:#94a3b8; font-size:13px;">
    🎓 أكاديمية نمو العالي للتدريب © 2026 — بناء القدرات الرقمية لشباب المستقبل 🌟
    </div>
    """,
    unsafe_allow_html=True,
)
