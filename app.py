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

# رابط Google Apps Script Web App (ضع رابطك هنا)
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
# تنسيقات CSS: لوحة ألوان عصرية (Aurora / Glassmorphism) + استجابة كاملة للجوال
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

    /* خلفية عصرية داكنة بتدرج شفقي (Aurora) */
    .stApp {{
        background: radial-gradient(circle at 15% 0%, #1b1035 0%, transparent 45%),
                    radial-gradient(circle at 85% 15%, #072a3d 0%, transparent 50%),
                    linear-gradient(160deg, #05060f 0%, #0b0f2e 45%, #150a30 100%);
        background-attachment: fixed;
        color: #eef2ff !important;
    }}

    /* منع التمرير الأفقي على الجوال */
    html, body {{
        overflow-x: hidden !important;
    }}

    .block-container {{
        padding-top: 1.4rem !important;
        padding-left: clamp(0.6rem, 3vw, 2rem) !important;
        padding-right: clamp(0.6rem, 3vw, 2rem) !important;
        max-width: 100% !important;
    }}

    /* الشعار الدائري باللمعة العصرية */
    .sphere-logo-container {{
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 10px 0;
    }}

    .sphere-logo {{
        width: 100px;
        height: 100px;
        border-radius: 50%;
        object-fit: cover;
        border: 3px solid transparent;
        background:
            linear-gradient(#0b0f2e, #0b0f2e) padding-box,
            linear-gradient(135deg, #22d3ee, #a855f7, #f472b6) border-box;
        box-shadow: 0 0 24px rgba(168, 85, 247, 0.45), 0 0 10px rgba(34, 211, 238, 0.35);
    }}

    @media (max-width: 640px) {{
        .sphere-logo {{ width: 76px; height: 76px; }}
    }}

    /* بطاقات زجاجية عصرية */
    .main-card {{
        background: rgba(255, 255, 255, 0.05);
        backdrop-filter: blur(14px);
        -webkit-backdrop-filter: blur(14px);
        border: 1px solid rgba(255, 255, 255, 0.10);
        border-radius: 20px;
        padding: clamp(16px, 3vw, 26px);
        margin-top: 8px;
        margin-bottom: 20px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.35);
        color: #eef2ff !important;
        word-break: break-word;
    }}

    .fun-card {{
        background: rgba(255, 255, 255, 0.045);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border-radius: 16px;
        padding: clamp(14px, 2.5vw, 20px);
        margin: 10px 0;
        box-shadow: 0 6px 20px rgba(0,0,0,0.28);
        border-right: 5px solid #22d3ee;
        border-top: 1px solid rgba(255,255,255,0.06);
        border-bottom: 1px solid rgba(255,255,255,0.06);
        border-left: 1px solid rgba(255,255,255,0.06);
        color: #eef2ff !important;
        word-break: break-word;
    }}

    .fun-card h3, .fun-card h4 {{
        background: linear-gradient(90deg, #22d3ee, #a855f7);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        display: inline-block;
    }}

    .badge {{
        display: inline-block;
        padding: 3px 12px;
        border-radius: 999px;
        font-size: 12px;
        font-weight: 700;
        margin-bottom: 8px;
        background: linear-gradient(90deg, rgba(34,211,238,0.18), rgba(168,85,247,0.18));
        border: 1px solid rgba(168,85,247,0.4);
        color: #c4b5fd !important;
    }}

    .title-glow {{
        font-size: clamp(20px, 4.6vw, 38px);
        font-weight: 900;
        background: linear-gradient(90deg, #22d3ee, #a855f7, #f472b6);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        line-height: 1.35;
    }}

    .subtitle {{
        text-align: center;
        color: #94a3b8;
        font-size: clamp(12px, 2.4vw, 15px);
    }}

    hr {{
        border-color: rgba(255,255,255,0.08) !important;
    }}

    .stRadio label, .stRadio div, .stRadio p {{
        color: #eef2ff !important;
        font-size: clamp(13px, 2.2vw, 15px) !important;
    }}

    .stTextInput input {{
        background-color: rgba(255,255,255,0.06) !important;
        color: #eef2ff !important;
        border: 1px solid rgba(34,211,238,0.5) !important;
        border-radius: 10px !important;
        text-align: right !important;
    }}

    .stButton>button, .stFormSubmitButton>button {{
        background: linear-gradient(90deg, #0ea5e9, #a855f7);
        color: white;
        font-weight: 700;
        font-size: clamp(14px, 2.4vw, 16px);
        border-radius: 12px;
        padding: 12px 24px;
        border: none;
        box-shadow: 0 4px 16px rgba(168, 85, 247, 0.35);
        transition: all 0.2s ease;
        width: 100%;
        min-height: 46px;
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

    /* توسيع مساحة اللمس للأزرار الشعاعية على الجوال */
    .stRadio > div {{ gap: 6px; }}

    /* تكديس الأعمدة بسلاسة على الشاشات الصغيرة (سلوك ستريمليت الافتراضي + دعم بصري) */
    @media (max-width: 640px) {{
        div[data-testid="column"] {{
            width: 100% !important;
            flex: 1 1 100% !important;
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
col1, col2 = st.columns([1, 4])
with col1:
    if logo_base64:
        st.markdown(
            f"""
            <div class="sphere-logo-container" style="margin:0;">
                <img src="data:image/jpeg;base64,{logo_base64}" class="sphere-logo" style="width:64px; height:64px;">
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.image("logo.jpg", width=64)
with col2:
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
        <p style="font-size:16px; color:#cbd5e1; line-height:1.8;">
        نعيش اليوم ثورة تكنولوجية غير مسبوقة يقودها الذكاء الاصطناعي، الحوسبة السحابية، وتحليل البيانات الضخمة.
        هذه المنصة صُممت خصيصًا لتزويدك بالمفاهيم الأساسية والمتقدمة اللازمة لمواكبة متطلبات سوق العمل الرقمي الحديث،
        وتأهيلك لاختيار تخصصات جامعية ومسارات مهنية واعدة في هذا المجال.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            '<div class="fun-card"><h3>🌐 التحول الرقمي</h3>'
            '<p>البنى التحتية، إنترنت الأشياء (IoT)، والحوسبة السحابية بأنواعها الثلاثة.</p></div>',
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            '<div class="fun-card"><h3>🧠 نماذج الذكاء</h3>'
            '<p>التعلم الآلي، الشبكات العصبية، معالجة اللغة الطبيعية، والنماذج التوليدية.</p></div>',
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            '<div class="fun-card"><h3>🛡️ أمن المعلومات</h3>'
            '<p>التهديدات السيبرانية الشائعة، وأخلاقيات استخدام خوارزميات الذكاء الاصطناعي.</p></div>',
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class="fun-card">
        <h4>📌 لماذا تهمك هذه المهارات؟</h4>
        <p style="line-height:1.8; font-size:15.5px;">
        وفقًا لتقارير المنتدى الاقتصادي العالمي، فإن مهارات التفكير التحليلي، التعامل مع الذكاء الاصطناعي والبيانات الضخمة،
        والوعي بالأمن السيبراني هي من بين أكثر المهارات طلبًا في سوق العمل حتى نهاية هذا العقد. البدء المبكر في فهم
        هذه المفاهيم يمنحك أفضلية حقيقية في مسارك الجامعي والمهني القادم.
        </p>
        </div>
        """,
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
        <p style="font-size:15.5px; line-height:1.8;">
        التحول الرقمي ليس مجرد استخدام أجهزة حاسوب، بل هو إعادة هندسة شاملة للعمليات والخدمات
        باستخدام التقنية لرفع الكفاءة، وتحسين تجربة المستخدم، واتخاذ قرارات مبنية على البيانات
        بدلًا من التخمين.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### ☁️ أنواع الحوسبة السحابية")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            '<div class="fun-card"><h4>IaaS</h4><p>بنية تحتية كخدمة: خوادم وتخزين افتراضي جاهز للاستخدام، مثل AWS EC2.</p></div>',
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            '<div class="fun-card"><h4>PaaS</h4><p>منصة كخدمة: بيئة جاهزة لبناء وتشغيل التطبيقات دون القلق بشأن الخوادم.</p></div>',
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            '<div class="fun-card"><h4>SaaS</h4><p>برمجيات كخدمة: تطبيقات جاهزة تُستخدم مباشرة عبر الإنترنت، مثل Google Docs.</p></div>',
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class="fun-card">
        <h3>🔗 إنترنت الأشياء (IoT)</h3>
        <p style="font-size:15.5px; line-height:1.8;">
        هو شبكة من الأجهزة المادية (حساسات، ساعات ذكية، سيارات، أجهزة منزلية) المتصلة بالإنترنت
        والقادرة على جمع البيانات وتبادلها واتخاذ إجراءات دون تدخل بشري مباشر، وهو ما يقوم عليه
        مفهوم "المدن الذكية" و"المصانع الذكية".
        </p>
        </div>
        <div class="fun-card">
        <h3>📊 البيانات الضخمة (Big Data)</h3>
        <p style="font-size:15.5px; line-height:1.8;">
        تُوصف عادة بخصائص الـ 5V: الحجم (Volume)، السرعة (Velocity)، التنوع (Variety)،
        الصدقية (Veracity)، والقيمة (Value). الشركات تستخدم هذه البيانات لفهم سلوك العملاء
        وتحسين قراراتها.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ===========================================================
# تقنيات الذكاء الاصطناعي المتقدمة
# ===========================================================
elif page == "🤖 تقنيات الذكاء الاصطناعي المتقدمة":
    st.markdown('<div class="main-card"><h2>🤖 عمق خوارزميات الذكاء الاصطناعي</h2></div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="fun-card">
        <h3>من التعلم الآلي إلى التعلم العميق</h3>
        <p style="font-size:15.5px; line-height:1.8;">
        الذكاء الاصطناعي مجال واسع يندرج تحته "التعلم الآلي" (Machine Learning)، وهو تعليم الحاسوب
        اكتشاف الأنماط من البيانات دون برمجته صراحة لكل حالة. أما "التعلم العميق" (Deep Learning)
        فهو فرع متقدم يحاكي بنية الخلايا العصبية في الدماغ البشري عبر طبقات متعددة لمعالجة مهام
        معقدة مثل التعرف على الصور والصوت.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### 🧩 أنواع التعلم الآلي الثلاثة")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            '<div class="fun-card"><h4>👨‍🏫 تعلم موجَّه</h4>'
            '<p>يتعلم النموذج من بيانات مُصنَّفة مسبقًا (سؤال وجواب)، مثل تصنيف البريد كمزعج أو غير مزعج.</p></div>',
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            '<div class="fun-card"><h4>🔍 تعلم غير موجَّه</h4>'
            '<p>يكتشف النموذج الأنماط والتجمعات بنفسه دون تصنيفات جاهزة، مثل تجميع العملاء حسب سلوك الشراء.</p></div>',
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            '<div class="fun-card"><h4>🎮 تعلم تعزيزي</h4>'
            '<p>يتعلم النموذج بالمحاولة والخطأ عبر مكافآت وعقوبات، كما في الروبوتات وألعاب الفيديو الذكية.</p></div>',
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class="fun-card">
        <h3>💬 معالجة اللغة الطبيعية (NLP) والنماذج التوليدية</h3>
        <p style="font-size:15.5px; line-height:1.8;">
        هي الفرع الذي يمكّن الحاسوب من فهم وتوليد اللغة البشرية، وهي الأساس الذي تقوم عليه
        النماذج اللغوية الكبيرة (LLMs) مثل الشات بوت الحديثة، التي تولّد نصوصًا وصورًا بناءً على
        احتمالات إحصائية متعلَّمة من كميات هائلة من النصوص، لا عبر "فهم" حقيقي كما لدى الإنسان.
        </p>
        </div>
        <div class="fun-card">
        <h3>👁️ رؤية الحاسوب (Computer Vision)</h3>
        <p style="font-size:15.5px; line-height:1.8;">
        تقنية تمكّن الأنظمة من "رؤية" وتحليل الصور والفيديو، وتُستخدم في التعرف على الوجوه،
        السيارات ذاتية القيادة، وتحليل الصور الطبية لمساعدة الأطباء على تشخيص أدق وأسرع.
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

    st.markdown("### ⚠️ أبرز التهديدات السيبرانية")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            '<div class="fun-card"><h4>🎣 التصيّد الاحتيالي</h4>'
            '<p>رسائل أو مواقع مزيفة تخدع المستخدم لسرقة بياناته أو كلمات مروره.</p></div>',
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            '<div class="fun-card"><h4>🦠 البرمجيات الخبيثة</h4>'
            '<p>برامج ضارة (فيروسات، برامج تجسس) تُصيب الأجهزة لسرقة البيانات أو تعطيلها.</p></div>',
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            '<div class="fun-card"><h4>🔐 برمجيات الفدية</h4>'
            '<p>تُشفّر بيانات الضحية وتطالب بفدية مالية مقابل فك التشفير.</p></div>',
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div class="fun-card">
        <h3>🛡️ خطوط الدفاع الأساسية</h3>
        <p style="font-size:15.5px; line-height:1.8;">
        تفعيل المصادقة الثنائية (2FA)، استخدام كلمات مرور قوية وفريدة لكل حساب، تحديث الأنظمة
        والتطبيقات دوريًا لسد الثغرات الأمنية، وعدم النقر على روابط أو مرفقات من مصادر غير موثوقة.
        </p>
        </div>
        <div class="fun-card">
        <h3>⚖️ أخلاقيات الذكاء الاصطناعي</h3>
        <p style="font-size:15.5px; line-height:1.8;">
        من أبرز القضايا الأخلاقية: <b>التحيّز الخوارزمي</b> (عندما تتعلم النماذج تحيزات موجودة في
        بيانات التدريب)، <b>خصوصية البيانات</b> (كيف تُجمع بيانات المستخدمين وتُستخدم)،
        و<b>التزييف العميق (Deepfake)</b> الذي يُستخدم لإنشاء صور أو مقاطع فيديو مزيفة تبدو حقيقية،
        مما يستدعي وعيًا نقديًا عند التعامل مع أي محتوى رقمي.
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

    st.markdown(
        """
        <div class="fun-card">
        <p style="font-size:15px; line-height:1.8;">
        هذا المختبر يحاكي بشكل مبسّط الخطوة الأولى التي تقوم بها كثير من أنظمة تصنيف النصوص:
        البحث عن كلمات مفتاحية دالة لتحديد التصنيف الأنسب. الأنظمة الحقيقية (مثل نماذج NLP) تستخدم
        بدلًا من ذلك تمثيلات رياضية معقدة للكلمات (Embeddings)، لكن الفكرة الأساسية للتصنيف متشابهة.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    categories = {
        "الذكاء الاصطناعي": ["ذكاء", "تعلم", "خوارزمية", "نموذج", "شبكة عصبية", "روبوت"],
        "الأمن السيبراني": ["اختراق", "تصيد", "فيروس", "كلمة مرور", "حماية", "فدية"],
        "الحوسبة السحابية": ["سحابة", "خادم", "تخزين", "iaas", "paas", "saas"],
        "إنترنت الأشياء": ["حساس", "جهاز ذكي", "استشعار", "iot", "منزل ذكي"],
    }

    user_query = st.text_input(
        "📝 اكتب جملة أو استفسارًا تقنيًا وسيحاول المصنّف تخمين مجاله:",
        placeholder="مثال: كيف يحمي جدار الحماية الشبكة من الاختراق؟",
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
                f'<p>عدد الكلمات المفتاحية التي طابقت النص: {scores[best_cat]}</p></div>',
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
