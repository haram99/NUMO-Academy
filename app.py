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
# قراءة رابط الـ URL المباشر (Query Parameters)
# ---------------------------------------------------------
query_params = st.query_params
url_page = query_params.get("page", None)

# ---------------------------------------------------------
# تنسيقات CSS: منع أي تداخل، ضبط العرض وتنسيق الجوال
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
        width: 80px;
        height: 80px;
        border-radius: 50%;
        object-fit: cover;
        border: 3px solid transparent;
        background:
            linear-gradient(#0b0f2e, #0b0f2e) padding-box,
            linear-gradient(135deg, #22d3ee, #a855f7, #f472b6) border-box;
        box-shadow: 0 0 16px rgba(168, 85, 247, 0.4);
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
        padding: 14px;
        margin-top: 8px;
        margin-bottom: 12px;
        box-shadow: 0 6px 20px rgba(0,0,0,0.3);
        color: #eef2ff !important;
        word-break: normal;
        overflow-wrap: break-word;
    }}

    .fun-card {{
        background: rgba(255, 255, 255, 0.045);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 12px;
        padding: 12px;
        margin: 8px 0;
        box-shadow: 0 4px 14px rgba(0,0,0,0.25);
        border-right: 4px solid #22d3ee;
        border-top: 1px solid rgba(255,255,255,0.06);
        border-bottom: 1px solid rgba(255,255,255,0.06);
        border-left: 1px solid rgba(255,255,255,0.06);
        color: #eef2ff !important;
        word-break: normal;
        overflow-wrap: break-word;
    }}

    .fun-card h3, .fun-card h4 {{
        background: linear-gradient(90deg, #22d3ee, #a855f7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: block;
        margin-bottom: 4px;
    }}

    .title-glow {{
        font-size: clamp(16px, 4vw, 28px);
        font-weight: 900;
        background: linear-gradient(90deg, #22d3ee, #a855f7, #f472b6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: right;
        line-height: 1.3;
    }}

    .subtitle {{
        text-align: right;
        color: #94a3b8;
        font-size: clamp(10px, 2vw, 12px);
    }}

    .stRadio label, .stRadio div, .stRadio p {{
        color: #eef2ff !important;
        font-size: 14px !important;
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
        padding: 8px 12px !important;
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
        min-height: 42px;
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
            margin-bottom: 8px;
        }}
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

# ---------------------------------------------------------
# تحديد الصفحة الحالية (سواء عبر الـ URL أو القائمة)
# ---------------------------------------------------------
if url_page == "quiz":
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
        st.markdown("<h3 style='text-align:center; color:#22d3ee; margin-top:5px;'>أكاديمية نمو العالي</h3>", unsafe_allow_html=True)
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
            key="main_navigation",
        )

# ---------------------------------------------------------
# رأس الصفحة المشترك
# ---------------------------------------------------------
col1, col2 = st.columns([4, 1])
with col2:
    if logo_base64:
        st.markdown(
            f"""
            <div class="sphere-logo-container" style="margin:0;">
                <img src="data:image/jpeg;base64,{logo_base64}" class="sphere-logo" style="width:45px; height:45px;">
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

# ===========================================================
# الرئيسية
# ===========================================================
if page == "🏠 الرئيسية":
    st.markdown(
        """
        <div class="main-card" style="text-align:center;">
        <h2>مرحبًا بك في بوابة قادة المستقبل الرقمي! 🚀</h2>
        <p style="font-size:14px; color:#cbd5e1; line-height:1.6;">
        اختر القسم المناسب من القائمة أو انتقل مباشرة للمسابقة عبر الزر أدناه.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # زر مباشر للمسابقة مع عرض QR Code لسهولة المسح بالجوال
    st.markdown(
        """
        <div class="fun-card" style="text-align: center; border-right: 4px solid #a855f7;">
        <h3>🏆 المسابقة والتحدي التقني المباشر</h3>
        <p style="font-size: 13px;">شارك في التحدي واختبر معلوماتك الآن!</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    
    if st.button("🚀 الانتقال المباشر لصفحة المسابقة"):
        st.query_params["page"] = "quiz"
        st.rerun()

    # توليد ورسم QR Code مباشر لصفحة المسابقة بالاعتماد على رابط الموقع الحالي
    try:
        # استخراج الرابط الحالي وإضافة ?page=quiz إليه
        current_base_url = st.context.headers.get("Host", "localhost:8501")
        # إذا كان الرابط سحابياً على Streamlit Cloud
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
            <img src="data:image/png;base64,{qr_base64}" style="width: 140px; border-radius: 10px; border: 2px solid #22d3ee; padding: 5px; background: white;">
            </div>
            """,
            unsafe_allow_html=True,
        )
    except Exception:
        pass

# ===========================================================
# بقية الأقسام (التحول الرقمي، الذكاء الاصطناعي، الأمن، المختبر)
# ===========================================================
elif page == "💡 أساسيات التحول الرقمي":
    st.markdown('<div class="main-card"><h2>💡 أساسيات التحول الرقمي</h2><p>استكشاف الحوسبة السحابية وإنترنت الأشياء.</p></div>', unsafe_allow_html=True)
elif page == "🤖 تقنيات الذكاء الاصطناعي المتقدمة":
    st.markdown('<div class="main-card"><h2>🤖 تقنيات الذكاء الاصطناعي</h2><p>التعلم العميق والشبكات العصبية.</p></div>', unsafe_allow_html=True)
elif page == "🔒 الأمن السيبراني والأخلاقيات":
    st.markdown('<div class="main-card"><h2>🔒 الأمن السيبراني</h2><p>حماية البيانات وأخلاقيات التقنية.</p></div>', unsafe_allow_html=True)
elif page == "🧪 مختبر الذكاء الاصطناعي":
    st.markdown('<div class="main-card"><h2>🧪 مختبر التصنيف الذكي</h2></div>', unsafe_allow_html=True)
    user_query = st.text_input("📝 اكتب استفسارك التقني:", key="lab_query_input")
    if user_query:
        st.markdown(f'<div class="fun-card"><h3>النتيجة:</h3><p>مصطلح تقني تم تحليله بنجاح.</p></div>', unsafe_allow_html=True)

# ===========================================================
# صفحة المسابقة المستقلة (يمكن الوصول لها عبر ?page=quiz)
# ===========================================================
elif page == "🎯 التحدي التقني والمسابقة":
    if url_page == "quiz":
        if st.button("⬅️ العودة للرئيسية"):
            st.query_params.clear()
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
                score = sum(1 for a, item in zip(answers, questions) if a == item["answer"])

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
)
