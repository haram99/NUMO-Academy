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
# تنسيقات CSS: إصلاح تداخل النصوص، ضبط الاتجاهات، وتحسين العرض على الجوال
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
        padding-top: 4.5rem !important;
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

    /* إصلاح البطاقات ومنع أي تداخل في النصوص على الجوال */
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
        word-break: normal;
        overflow-wrap: break-word;
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
        word-break: normal;
        overflow-wrap: break-word;
    }}

    .fun-card h3, .fun-card h4 {{
        background: linear-gradient(90deg, #22d3ee, #a855f7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: block;
        margin-bottom: 6px;
    }}

    .badge {{
        display: inline-block;
        padding: 3px 10px;
        border-radius: 999px;
        font-size: 11px;
        font-weight: 700;
        margin-bottom: 8px;
        background: linear-gradient(90deg, rgba(34,211,238,0.18), rgba(168,85,247,0.18));
        border: 1px solid rgba(168,85,247,0.4);
        color: #c4b5fd !important;
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

    hr {{
        border-color: rgba(255,255,255,0.08) !important;
    }}

    .stRadio label, .stRadio div, .stRadio p {{
        color: #eef2ff !important;
        font-size: clamp(13px, 2.2vw, 15px) !important;
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
        transition: all 0.2s ease;
        width: 100%;
        min-height: 44px;
    }}
    .stButton>button:hover, .stFormSubmitButton>button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 8px 20px rgba(34, 211, 238, 0.45);
        color: white !important;
    }}

    section[data-testid="stSidebar"] {{
        background: linear-gradient(180deg, #05060f, #150a30);
        border-left: 1px solid rgba(255,255,255,0.08);
    }}

    section[data-testid="stSidebar"] * {{
        color: #eef2ff !important;
    }}

    .stRadio > div {{ gap: 6px; }}

    /* تكديس الأعمدة بسلاسة تامة على الجوال دون أي تداخل */
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
# الشريط الجانبي
# ---------------------------------------------------------
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
        key="main_navigation",
    )

    st.markdown("---")
    st.markdown(
        "<p style='text-align:center; font-size:12px; color:#94a3b8;'>مخصص لطلبة المرحلة الثانوية 🎓</p>",
        unsafe_allow_html=True,
    )

# ---------------------------------------------------------
# رأس الصفحة
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
    st.markdown(
        "<p class='subtitle'>برنامج إثراء مهارات المستقبل للمرحلة الثانوية — أكاديمية نمو العالي</p>",
        unsafe_allow_html=True,
    )

st.markdown("---")

# ---------------------------------------------------------
# تهيئة حالة الجلسة
# ---------------------------------------------------------
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

    # زر مباشر وسريع للمسابقة يظهر بوضوح تام على الجوال في الصفحة الرئيسية
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
        st.session_state.main_navigation = "🎯 التحدي التقني والمسابقة"
        st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            '<div class="fun-card"><h3>🌐 التحول الرقمي</h3>'
            '<p style="font-size: 14px;">البنى التحتية، إنترنت الأشياء (IoT)، والحوسبة السحابية.</p></div>',
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            '<div class="fun-card"><h3>🧠 نماذج الذكاء</h3>'
            '<p style="font-size: 14px;">التعلم الآلي، الشبكات العصبية، ومعالجة اللغات الطبيعية.</p></div>',
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            '<div class="fun-card"><h3>🛡️ أمن المعلومات</h3>'
            '<p style="font-size: 14px;">التهديدات السيبرانية الشائعة وأخلاقيات خوارزميات الذكاء.</p></div>',
            unsafe_allow_html=True,
        )

# ===========================================================
# أساسيات التحول الرقمي
# ===========================================================
elif page == "💡 أساسيات التحول الرقمي":
    st.markdown('<div class="main-card"><h2>💡 أساسيات التحول الرقمي والتقنيات الناشئة</h2></div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="fun-card">
        <h3>ما هو التحول الرقمي؟</h3>
        <p style="font-size:15px; line-height:1.7;">
        التحول الرقمي ليس مجرد استخدام أجهزة حاسوب، بل هو إعادة هندسة شاملة للعمليات والخدمات
        باستخدام التقنية لرفع الكفاءة، وتحسين تجربة المستخدم، واتخاذ قرارات مبنية على البيانات.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="fun-card"><h4>IaaS</h4><p style="font-size:14px;">بنية تحتية كخدمة وتخزين افتراضي.</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="fun-card"><h4>PaaS</h4><p style="font-size:14px;">منصة كخدمة لتشغيل التطبيقات.</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="fun-card"><h4>SaaS</h4><p style="font-size:14px;">برمجيات جاهزة عبر الإنترنت.</p></div>', unsafe_allow_html=True)

# ===========================================================
# تقنيات الذكاء الاصطناعي المتقدمة
# ===========================================================
elif page == "🤖 تقنيات الذكاء الاصطناعي المتقدمة":
    st.markdown('<div class="main-card"><h2>🤖 عمق خوارزميات الذكاء الاصطناعي</h2></div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="fun-card">
        <h3>من التعلم الآلي إلى التعلم العميق</h3>
        <p style="font-size:15px; line-height:1.7;">
        الذكاء الاصطناعي مجال واسع يندرج تحته "التعلم الآلي"، بينما يحاكي "التعلم العميق" بنية الخلايا
        العصبية في الدماغ البشري عبر طبقات متعددة لمعالجة مهام معقدة.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ===========================================================
# الأمن السيبراني والأخلاقيات
# ===========================================================
elif page == "🔒 الأمن السيبراني والأخلاقيات":
    st.markdown('<div class="main-card"><h2>🔒 الأمن السيبراني وأخلاقيات التقنية</h2></div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="fun-card">
        <h3>أبرز التهديدات وسبل الحماية</h3>
        <p style="font-size:15px; line-height:1.7;">
        يشمل الأمن السيبراني حماية الأنظمة والشبكات من الهجمات الرقمية كالتصيد الاحتيالي والبرمجيات الخبيثة،
        مع الالتزام بالمعايير الأخلاقية للتعامل مع البيانات.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ===========================================================
# مختبر الذكاء الاصطناعي
# ===========================================================
elif page == "🧪 مختبر الذكاء الاصطناعي":
    st.markdown('<div class="main-card"><h2>🧪 محاكي تصنيف النصوص بالكلمات المفتاحية</h2></div>', unsafe_allow_html=True)

    categories = {
        "الذكاء الاصطناعي": ["ذكاء", "تعلم", "خوارزمية", "نموذج", "شبكة عصبية", "روبوت"],
        "الأمن السيبراني": ["اختراق", "تصيد", "فيروس", "كلمة مرور", "حماية", "فدية"],
        "الحوسبة السحابية": ["سحابة", "خادم", "تخزين", "iaas", "paas", "saas"],
        "إنترنت الأشياء": ["حساس", "جهاز ذكي", "استشعار", "iot", "منزل ذكي"],
    }

    user_query = st.text_input(
        "📝 اكتب جملة أو استفسارًا تقنيًا وسيحاول المصنّف تخمين مجاله:",
        placeholder="مثال: كيف يحمي جدار الحماية الشبكة؟",
        key="lab_query_input",
    )

    if user_query:
        with st.spinner("🔄 جاري تحليل النص..."):
            time.sleep(0.8)

        text = user_query.lower()
        scores = {cat: sum(1 for kw in kws if kw in text) for cat, kws in categories.items()}
        best_cat = max(scores, key=scores.get)
        total_hits = sum(scores.values())

        if total_hits == 0:
            st.markdown(
                '<div class="fun-card"><h3>النتيجة</h3>'
                '<p>لم يتعرف المصنّف على كلمات مفتاحية واضحة. جرّب إضافة مصطلحات تقنية أكثر تحديدًا.</p></div>',
                unsafe_allow_html=True,
            )
        else:
            confidence = int((scores[best_cat] / total_hits) * 100)
            st.markdown(
                f'<div class="fun-card"><h3>التصنيف المقترح: {best_cat}</h3>'
                f'<p>عدد الكلمات المفتاحية المطابقة: {scores[best_cat]}</p></div>',
                unsafe_allow_html=True,
            )
            st.progress(confidence, text=f"نسبة الثقة التقريبية: {confidence}%")
            st.session_state.lab_history.append((user_query, best_cat))

    if st.session_state.lab_history:
        st.markdown("### 🕓 سجلّ المحاولات الأخيرة")
        for q, cat in reversed(st.session_state.lab_history[-5:]):
            st.markdown(f'<div class="fun-card">📝 "{q}" ← <b>{cat}</b></div>', unsafe_allow_html=True)

# ===========================================================
# التحدي التقني والمسابقة
# ===========================================================
elif page == "🎯 التحدي التقني والمسابقة":
    st.markdown('<div class="main-card"><h2>🎯 التحدي التقني النهائي (اختبر معلوماتك وسجل بالمسابقة)</h2></div>', unsafe_allow_html=True)

    with st.form("competition_form"):
        st.markdown("### بيانات المتسابق:")
        participant_name = st.text_input("👤 الاسم الكامل:", key="comp_name")
        participant_phone = st.text_input("📱 رقم الجوال (مثال: 05XXXXXXXX):", key="comp_phone")

        st.markdown("---")
        st.markdown("### أسئلة التحدي:")

        questions = [
            {
                "q": "1. مؤسسة تريد تحليل سلوك آلاف العملاء دون امتلاك تصنيفات جاهزة لبياناتهم، فما نوع التعلم الآلي الأنسب؟",
                "options": [
                    "تعلم موجَّه (Supervised Learning)",
                    "تعلم غير موجَّه (Unsupervised Learning)",
                    "تعلم تعزيزي (Reinforcement Learning)",
                ],
                "answer": "تعلم غير موجَّه (Unsupervised Learning)",
                "explain": "التعلم غير الموجَّه مناسب هنا لأنه يكتشف الأنماط والتجمعات في البيانات دون الحاجة لتصنيفات مسبقة.",
            },
            {
                "q": "2. شركة ناشئة تريد إطلاق تطبيق بسرعة دون بناء أو إدارة خوادمها الخاصة، ما نوع الخدمة السحابية الأنسب؟",
                "options": ["IaaS", "PaaS", "SaaS"],
                "answer": "PaaS",
                "explain": "منصة كخدمة (PaaS) توفر بيئة جاهزة لتطوير ونشر التطبيقات دون القلق بشأن إدارة البنية التحتية.",
            },
            {
                "q": "3. تلقيت رسالة بريد إلكتروني تطلب تحديث كلمة مرور حسابك البنكي عبر رابط غريب، ما نوع الهجوم الأرجح؟",
                "options": ["برمجية فدية", "تصيّد احتيالي (Phishing)", "هجوم حجب خدمة"],
                "answer": "تصيّد احتيالي (Phishing)",
                "explain": "هذا النمط الكلاسيكي من التصيّد الاحتيالي يعتمد على خداع الضحية لإدخال بياناته في موقع مزيف.",
            },
            {
                "q": "4. ما الذي يميّز التعلم العميق (Deep Learning) عن التعلم الآلي التقليدي؟",
                "options": [
                    "استخدام طبقات متعددة من الشبكات العصبية لاستخلاص أنماط معقدة تلقائيًا",
                    "الاعتماد الكامل على قواعد مبرمجة يدويًا لكل حالة",
                    "عدم الحاجة لأي بيانات تدريب على الإطلاق",
                ],
                "answer": "استخدام طبقات متعددة من الشبكات العصبية لاستخلاص أنماط معقدة تلقائيًا",
                "explain": "التعلم العميق يستخدم شبكات عصبية متعددة الطبقات قادرة على استخلاص خصائص معقدة من البيانات الخام تلقائيًا.",
            },
            {
                "q": "5. لماذا يُعد التحيّز الخوارزمي (Algorithmic Bias) قضية أخلاقية مهمة؟",
                "options": [
                    "لأنه يزيد من سرعة تنفيذ النموذج",
                    "لأن النموذج قد يتعلم ويكرر تحيزات موجودة في بيانات التدريب، مما يؤثر على عدالة القرارات",
                    "لأنه يقلل من تكلفة تشغيل الخوادم",
                ],
                "answer": "لأن النموذج قد يتعلم ويكرر تحيزات موجودة في بيانات التدريب، مما يؤثر على عدالة القرارات",
                "explain": "إذا كانت بيانات التدريب متحيزة، فإن النموذج ينقل هذا التحيّز إلى قراراته، ما قد يؤدي لنتائج غير عادلة تجاه فئات معينة.",
            },
            {
                "q": "6. ما أفضل ممارسة أمنية شخصية من بين التالي؟",
                "options": [
                    "استخدام نفس كلمة المرور لكل الحسابات لتسهيل تذكرها",
                    "تفعيل المصادقة الثنائية (2FA) وتحديث البرمجيات دوريًا",
                    "مشاركة كلمة المرور مع الأصدقاء المقربين فقط",
                ],
                "answer": "تفعيل المصادقة الثنائية (2FA) وتحديث البرمجيات دوريًا",
                "explain": "المصادقة الثنائية تضيف طبقة حماية إضافية حتى لو سُرقت كلمة المرور، والتحديثات الدورية تسد الثغرات الأمنية المعروفة.",
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

                st.markdown("### 📖 مراجعة الإجابات")
                for a, item in zip(answers, questions):
                    correct = a == item["answer"]
                    icon = "✅" if correct else "❌"
                    st.markdown(
                        f'<div class="fun-card">{icon} <b>{item["q"]}</b><br>'
                        f'الإجابة الصحيحة: {item["answer"]}<br>'
                        f'<span style="color:#94a3b8;">{item["explain"]}</span></div>',
                        unsafe_allow_html=True,
                    )

                if score == len(questions):
                    st.balloons()
                    st.markdown(
                        "<h3 style='text-align:center; color:#4ade80;'>🏆 أداء ممتاز! لقد اجتزت التحدي بجدارة واستحقاق.</h3>",
                        unsafe_allow_html=True,
                    )

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
