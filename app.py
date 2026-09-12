# -*- coding: utf-8 -*-
"""
منصة تفاعلية متقدمة عن التقنية والذكاء الاصطناعي للمرحلة الثانوية
أكاديمية نمو العالي للتدريب - Numo Academy
تشغيل: streamlit run app.py
"""

import streamlit as st
import random
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
GOOGLE_SHEET_WEB_APP_URL = "ضع_رابط_ويب_جوجل_هنا"

# دالة لتحويل الشعار إلى Base64
def get_image_base64(path):
    try:
        with open(path, "rb") as f:
            data = f.read()
        return base64.b64encode(data).decode("utf-8")
    except Exception:
        return ""

logo_base64 = get_image_base64("logo.jpg")

# ---------------------------------------------------------
# تنسيقات CSS: إصلاح الهامش العلوي لمنع الاختفاء + دوران الشعار
# ---------------------------------------------------------
st.markdown(
    f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Tajawal:wght@400;700;900&display=swap');

    html, body, [class*="css"], .stMarkdown, p, span, label, div, h1, h2, h3, h4, h5, h6 {{
        font-family: 'Tajawal', sans-serif !important;
        direction: rtl !important;
        text-align: right !important;
    }}

    .stApp {{
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #311042 100%);
        background-size: 400% 400%;
        animation: gradientShift 18s ease infinite;
        color: #f8fafc !important;
    }}

    @keyframes gradientShift {{
        0% {{background-position: 0% 50%;}}
        50% {{background-position: 100% 50%;}}
        100% {{background-position: 0% 50%;}}
    }}

    /* زيادة الهامش العلوي بمسافة كافية جداً لعدم تغطية العنوان بواسطة شريط المنصة */
    .block-container {{
        padding-top: 6rem !important;
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        max-width: 100% !important;
    }}

    /* حاوية الشعار المجسم ثلاثي الأبعاد */
    .sphere-logo-container {{
        perspective: 1000px;
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 15px 0;
    }}

    /* دوران أفقي حقيقي حول المحور Y */
    .sphere-logo {{
        width: 110px;
        height: 110px;
        border-radius: 50%;
        object-fit: cover;
        border: 4px solid #38bdf8;
        box-shadow: inset 0 0 15px rgba(0,0,0,0.6), 0 0 25px rgba(56, 189, 248, 0.6);
        animation: horizontalSpin 6s linear infinite;
        transform-style: preserve-3d;
    }}

    @keyframes horizontalSpin {{
        0% {{ transform: rotateY(0deg); }}
        100% {{ transform: rotateY(360deg); }}
    }}

    .main-card {{
        background: rgba(30, 41, 59, 0.85);
        border-radius: 20px;
        padding: 20px;
        margin-top: 15px;
        margin-bottom: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.4);
        border: 1px solid rgba(56, 189, 248, 0.2);
        color: #f8fafc !important;
        word-break: break-word;
    }}

    .fun-card {{
        background: rgba(15, 23, 42, 0.9);
        border-radius: 16px;
        padding: 18px;
        margin: 10px 0;
        box-shadow: 0 6px 18px rgba(0,0,0,0.3);
        border-right: 6px solid #38bdf8;
        border-left: 1px solid rgba(255,255,255,0.05);
        border-top: 1px solid rgba(255,255,255,0.05);
        border-bottom: 1px solid rgba(255,255,255,0.05);
        color: #f8fafc !important;
        word-break: break-word;
    }}

    .fun-card h3, .fun-card h4 {{
        color: #38bdf8 !important;
    }}

    .title-glow {{
        font-size: 26px;
        font-weight: 900;
        background: linear-gradient(90deg, #38bdf8, #818cf8, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: right;
        line-height: 1.4;
    }}

    @media (min-width: 768px) {{
        .title-glow {{
            font-size: 34px;
        }}
    }}

    .stRadio label, .stRadio div {{
        color: #f8fafc !important;
        font-size: 15px !important;
    }}

    .stTextInput input {{
        background-color: rgba(15, 23, 42, 0.8) !important;
        color: white !important;
        border: 1px solid #38bdf8 !important;
        border-radius: 10px !important;
        text-align: right !important;
    }}

    .stButton>button {{
        background: linear-gradient(90deg, #0284c7, #7c3aed);
        color: white;
        font-weight: 700;
        font-size: 16px;
        border-radius: 12px;
        padding: 10px 24px;
        border: none;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        transition: all 0.2s ease;
        width: 100%;
    }}
    .stButton>button:hover {{
        transform: translateY(-2px);
        box-shadow: 0 6px 16px rgba(56, 189, 248, 0.4);
        color: white !important;
    }}

    section[data-testid="stSidebar"] {{
        background: linear-gradient(180deg, #0f172a, #1e1b4b);
        border-left: 1px solid rgba(255,255,255,0.1);
    }}
    
    section[data-testid="stSidebar"] * {{
        color: #f8fafc !important;
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

    st.markdown("<h3 style='text-align: center; color: #38bdf8; margin-top: 5px;'>أكاديمية نمو العالي</h3>", unsafe_allow_html=True)
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
        key="main_sidebar_nav_v2"
    )
    
    st.markdown("---")
    st.markdown("<p style='text-align: center; font-size: 13px; color: #94a3b8;'>مخصص لطلبة المرحلة الثانوية 🎓</p>", unsafe_allow_html=True)

# ---------------------------------------------------------
# رأس الصفحة
# ---------------------------------------------------------
col1, col2 = st.columns([4, 1])
with col2:
    if logo_base64:
        st.markdown(
            f"""
            <div class="sphere-logo-container" style="margin: 0;">
                <img src="data:image/jpeg;base64,{logo_base64}" class="sphere-logo" style="width: 75px; height: 75px;">
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.image("logo.jpg", width=75)
with col1:
    st.markdown('<div class="title-glow">منصة الابتكار الرقمي والذكاء الاصطناعي</div>', unsafe_allow_html=True)
    st.markdown("<p style='text-align: right; color: #94a3b8; font-size: 13px;'>برنامج إثراء مهارات المستقبل للمرحلة الثانوية — أكاديمية نمو العالي</p>", unsafe_allow_html=True)

st.markdown("---")

# ---------------------------------------------------------
# الأقسام
# ---------------------------------------------------------
if page == "🏠 الرئيسية":
    st.markdown(
        """
        <div class="main-card" style="text-align: center;">
        <h2>مرحبًا بك في بوابة مهندسي وقادة المستقبل الرقمي! 🚀</h2>
        <p style="font-size: 16px; color: #cbd5e1; line-height: 1.6;">
        نعيش اليوم ثورة تكنولوجية غير مسبوقة يقودها الذكاء الاصطناعي، الحوسبة السحابية، وتحليل البيانات الضخمة.
        هذه المنصة صُممت خصيصًا لتزويد طلاب المرحلة الثانوية بالمفاهيم الأساسية والمتقدمة لمواكبة متطلبات العصر الرقمي الحديث.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="fun-card"><h3>🌐 التحول الرقمي</h3><p>فهم البنى التحتية، إنترنت الأشياء (IoT)، وتطبيقات الحوسبة الحديثة.</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="fun-card"><h3>🧠 نماذج الذكاء</h3><p>التعرف على الشبكات العصبية، التعلم العميق، ومعالجة اللغات الطبيعية (NLP).</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="fun-card"><h3>🛡️ أمن المعلومات</h3><p>استكشاف أساسيات الأمن السيبراني وأخلاقيات استخدام خوارزميات الذكاء الاصطناعي.</p></div>', unsafe_allow_html=True)

elif page == "💡 أساسيات التحول الرقمي":
    st.markdown('<div class="main-card"><h2>💡 أساسيات التحول الرقمي والتقنيات الناشئة</h2></div>', unsafe_allow_html=True)
    st.markdown('<div class="fun-card"><h3>ما هو التحول الرقمي؟</h3><p style="font-size: 16px; line-height: 1.7;">التحول الرقمي ليس مجرد استخدام أجهزة حاسوب، بل هو إعادة هندسة شاملة للعمليات والخدمات باستخدام التقنية لرفع الكفاءة.</p></div>', unsafe_allow_html=True)

elif page == "🤖 تقنيات الذكاء الاصطناعي المتقدمة":
    st.markdown('<div class="main-card"><h2>🤖 عمق خوارزميات الذكاء الاصطناعي</h2></div>', unsafe_allow_html=True)
    st.markdown('<div class="fun-card"><h3>من التعلم الآلي إلى التعلم العميق</h3><p style="font-size: 16px; line-height: 1.7;">التعلم العميق فرع متقدم يحاكي بنية الخلايا العصبية في الدماغ البشري لمعالجة المهام المعقدة.</p></div>', unsafe_allow_html=True)

elif page == "🔒 الأمن السيبراني والأخلاقيات":
    st.markdown('<div class="main-card"><h2>🔒 الأمن السيبراني وأخلاقيات التقنية</h2></div>', unsafe_allow_html=True)
    st.markdown('<div class="fun-card"><h3>حماية الفضاء الرقمي وأخلاقيات الذكاء الاصطناعي</h3><p style="font-size: 16px; line-height: 1.7;">التأمين الرقمي وحماية خصوصية الأفراد تمثل ركيزة أساسية في العصر الحديث.</p></div>', unsafe_allow_html=True)

elif page == "🧪 مختبر الذكاء الاصطناعي":
    st.markdown('<div class="main-card"><h2>🧪 محاكي خوارزميات معالجة النصوص الذكية</h2></div>', unsafe_allow_html=True)
    user_query = st.text_input("📝 أدخل استفسارك التقني أو الكلمة المفتاحية:", placeholder="مثال: الأمن السيبراني، سحابة", key="lab_query_input_v2")
    if user_query:
        with st.spinner("🔄 جاري المعالجة..."):
            time.sleep(1)
        st.markdown(f'<div class="fun-card"><h3>النتيجة:</h3><p>موضوع "{user_query}" يمثل ركيزة حيوية في التحول الرقمي الحديث.</p></div>', unsafe_allow_html=True)

elif page == "🎯 التحدي التقني والمسابقة":
    st.markdown('<div class="main-card"><h2>🎯 التحدي التقني النهائي (اختبر معلوماتك وسجل بالمسابقة)</h2></div>', unsafe_allow_html=True)

    with st.form("competition_form_v2"):
        st.markdown("### بيانات المتسابق:")
        participant_name = st.text_input("👤 الاسم الكامل:", key="comp_name_v2")
        participant_phone = st.text_input("📱 رقم الجوال (مثال: 05XXXXXXXX):", key="comp_phone_v2")

        st.markdown("---")
        st.markdown("### أسئلة التحدي:")

        q1 = st.radio("1. أي مما يلي يُعتبر المكون الأساسي الذي يحاكي الشبكات العصبية للبشر؟", ["الخوارزميات التقليدية", "الشبكات العصبية العميقة (Deep Neural Networks)", "جداول البيانات الثابتة"], index=None, key="q1_radio_v2")
        q2 = st.radio("2. ما هي الفائدة الرئيسية للحوسبة السحابية للشركات؟", ["الاعتماد كليًا على الخوادم المحلية", "مرونة الوصول للموارد وخفض التكاليف التشغيلية", "إبطاء معالجة البيانات"], index=None, key="q2_radio_v2")
        q3 = st.radio("3. أي من الآتي يمثل ممارسة صحيحة في الأمن السيبراني الشخصي؟", ["استخدام كلمة مرور موحدة وسهلة", "تفعيل المصادقة الثنائية (2FA) وتحديث البرمجيات دورياً", "النقر على الروابط غير المعروفة"], index=None, key="q3_radio_v2")

        submitted = st.form_submit_button("🚀 إرسال الإجابات وتسجيل المشاركة")

        if submitted:
            if not participant_name.strip() or not participant_phone.strip():
                st.error("⚠️ الرجاء إدخال الاسم ورقم الجوال بشكل صحيح قبل الإرسال.")
            else:
                score = 0
                if q1 == "الشبكات العصبية العميقة (Deep Neural Networks)":
                    score += 1
                if q2 == "مرونة الوصول للموارد وخفض التكاليف التشغيلية":
                    score += 1
                if q3 == "تفعيل المصادقة الثنائية (2FA) وتحديث البرمجيات دورياً":
                    score += 1

                st.success(f"🎉 شكرًا لك يا {participant_name}! تم استلام إجاباتك بنجاح.")
                st.markdown(f"""
                <div class="fun-card" style="text-align: center;">
                <h3>📊 نتيجتك النهائية في التحدي:</h3>
                <h1 style="color: #38bdf8;">{score} / 3</h1>
                <p>تم حفظ بياناتك وجوالك ({participant_phone}) في جدول الأكاديمية السحابي بنجاح.</p>
                </div>
                """, unsafe_allow_html=True)

                if score == 3:
                    st.balloons()
                    st.markdown("<h3 style='text-align: center; color: #4ade80;'>🏆 أداء ممتاز! لقد اجتزت التحدي بجدارة واستحقاق.</h3>", unsafe_allow_html=True)

                try:
                    payload = {
                        "name": participant_name,
                        "phone": participant_phone,
                        "score": score,
                        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    }
                    if GOOGLE_SHEET_WEB_APP_URL != "ضع_رابط_ويب_جوجل_هنا":
                        requests.post(GOOGLE_SHEET_WEB_APP_URL, json=payload)
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
