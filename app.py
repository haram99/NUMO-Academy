# -*- coding: utf-8 -*-
"""
منصة تفاعلية متقدمة عن التقنية والذكاء الاصطناعي للمرحلة الثانوية
أكاديمية نمو العالي للتدريب - Numo Academy
تشغيل: streamlit run app.py
"""

import streamlit as st
import random
import time
import pandas as pd
from datetime import datetime
import base64

# ---------------------------------------------------------
# إعدادات الصفحة العامة
# ---------------------------------------------------------
st.set_page_config(
    page_title="مستقبل التقنية والذكاء الاصطناعي 🚀",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded",
)

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
# تنسيقات CSS: إصلاح الهامش العلوي لمنع التداخل وتجسيم الشعار
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

    /* إضافة هامش علوي للمحتوى الرئيسي لكي لا يتداخل مع شريط Streamlit العلوي */
    .block-container {{
        padding-top: 3rem !important;
    }}

    /* حاوية الشعار المجسم ثلاثي الأبعاد */
    .sphere-logo-container {{
        perspective: 800px;
        display: flex;
        justify-content: center;
        align-items: center;
        margin: 15px 0;
    }}

    /* حركة دوران أفقية (يمين ويسار) على المحور Y فقط دون انقلاب */
    .sphere-logo {{
        width: 120px;
        height: 120px;
        border-radius: 50%;
        object-fit: cover;
        border: 4px solid #38bdf8;
        box-shadow: inset 0 0 15px rgba(0,0,0,0.6), 0 0 25px rgba(56, 189, 248, 0.6);
        animation: sphereRotateY 6s ease-in-out infinite alternate;
        transform-style: preserve-3d;
    }}

    @keyframes sphereRotateY {{
        0% {{
            transform: rotateY(-45deg);
            box-shadow: inset 15px 0 15px rgba(0,0,0,0.5), -10px 5px 20px rgba(56,189,248,0.4);
        }}
        50% {{
            transform: rotateY(0deg);
            box-shadow: inset 0 0 15px rgba(0,0,0,0.1), 0 5px 25px rgba(56,189,248,0.8);
        }}
        100% {{
            transform: rotateY(45deg);
            box-shadow: inset -15px 0 15px rgba(0,0,0,0.5), 10px 5px 20px rgba(56,189,248,0.4);
        }}
    }}

    .main-card {{
        background: rgba(30, 41, 59, 0.85);
        border-radius: 20px;
        padding: 30px;
        margin-top: 15px;
        margin-bottom: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.4);
        border: 1px solid rgba(56, 189, 248, 0.2);
        color: #f8fafc !important;
    }}

    .fun-card {{
        background: rgba(15, 23, 42, 0.9);
        border-radius: 16px;
        padding: 22px;
        margin: 12px 0;
        box-shadow: 0 6px 18px rgba(0,0,0,0.3);
        border-right: 6px solid #38bdf8;
        border-left: 1px solid rgba(255,255,255,0.05);
        border-top: 1px solid rgba(255,255,255,0.05);
        border-bottom: 1px solid rgba(255,255,255,0.05);
        color: #f8fafc !important;
    }}

    .fun-card h3, .fun-card h4 {{
        color: #38bdf8 !important;
    }}

    .title-glow {{
        font-size: 38px;
        font-weight: 900;
        background: linear-gradient(90deg, #38bdf8, #818cf8, #c084fc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
    }}

    .stRadio label, .stRadio div {{
        color: #f8fafc !important;
        font-size: 16px !important;
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
# الشريط الجانبي: الشعار المجسم المتحرك والتنقل
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
    )
    st.markdown("---")
    st.markdown("<p style='text-align: center; font-size: 13px; color: #94a3b8;'>مخصص لطلبة المرحلة الثانوية 🎓</p>", unsafe_allow_html=True)

# ---------------------------------------------------------
# رأس الصفحة
# ---------------------------------------------------------
col1, col2 = st.columns([1, 5])
with col1:
    if logo_base64:
        st.markdown(
            f"""
            <div class="sphere-logo-container" style="margin: 0;">
                <img src="data:image/jpeg;base64,{logo_base64}" class="sphere-logo" style="width: 80px; height: 80px;">
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.image("logo.jpg", width=80)
with col2:
    st.markdown('<div class="title-glow" style="margin-top: 10px;">منصة الابتكار الرقمي والذكاء الاصطناعي</div>', unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: #94a3b8;'>برنامج إثراء مهارات المستقبل للمرحلة الثانوية — أكاديمية نمو العالي للتدريب</p>", unsafe_allow_html=True)

st.markdown("---")

# ---------------------------------------------------------
# 1. الرئيسية
# ---------------------------------------------------------
if page == "🏠 الرئيسية":
    st.markdown(
        """
        <div class="main-card" style="text-align: center;">
        <h2>مرحبًا بك في بوابة مهندسي وقادة المستقبل الرقمي! 🚀</h2>
        <p style="font-size: 18px; color: #cbd5e1; line-height: 1.6;">
        نعيش اليوم ثورة تكنولوجية غير مسبوقة يقودها الذكاء الاصطناعي، الحوسبة السحابية، وتحليل البيانات الضخمة.
        هذه المنصة صُممت خصيصًا لتزويد طلاب المرحلة الثانوية بالمفاهيم الأساسية والمتقدمة لمواكبة متطلبات العصر الرقمي الحديث.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown(
            '<div class="fun-card"><h3>🌐 التحول الرقمي</h3><p>فهم البنى التحتية، إنترنت الأشياء (IoT)، وتطبيقات الحوسبة الحديثة.</p></div>',
            unsafe_allow_html=True,
        )
    with c2:
        st.markdown(
            '<div class="fun-card"><h3>🧠 نماذج الذكاء</h3><p>التعرف على الشبكات العصبية، التعلم العميق، ومعالجة اللغات الطبيعية (NLP).</p></div>',
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            '<div class="fun-card"><h3>🛡️ أمن المعلومات</h3><p>استكشاف أساسيات الأمن السيبراني وأخلاقيات استخدام خوارزميات الذكاء الاصطناعي.</p></div>',
            unsafe_allow_html=True,
        )

# ---------------------------------------------------------
# 2. أساسيات التحول الرقمي
# ---------------------------------------------------------
elif page == "💡 أساسيات التحول الرقمي":
    st.markdown('<div class="main-card"><h2>💡 أساسيات التحول الرقمي والتقنيات الناشئة</h2></div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="fun-card">
        <h3>ما هو التحول الرقمي؟</h3>
        <p style="font-size: 16px; line-height: 1.7;">
        التحول الرقمي ليس مجرد استخدام أجهزة حاسوب، بل هو إعادة هندسة شاملة للعمليات والخدمات باستخدام التقنية لرفع الكفاءة.
        يشمل ذلك الحوسبة السحابية (Cloud Computing) التي تتيح تخزين ومعالجة البيانات عن بُعد، وإنترنت الأشياء (IoT) الذي يربط الأجهزة المادية بشبكة الإنترنت لتبادل البيانات واتخاذ القرار التلقائي.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### 📊 ركائز التقنية الحديثة في العصر الحالي:")
    techs = [
        ("☁️", "الحوسبة السحابية", "توفير موارد الحاسب الآلي كخدمة عبر الإنترنت عند الطلب دون إدارة محلية معقدة."),
        ("📈", "البيانات الضخمة (Big Data)", "تحليلات كميات هائلة من البيانات لاستخراج رؤى وقرارات استراتيجية دقيقة."),
        ("🔗", "تقنية السجل الموزع (Blockchain)", "نظُم قواعد بيانات آمنة ولامركزية تضمن موثوقية وشفافية المعاملات الرقمية."),
        ("🌐", "إنترنت الأشياء (IoT)", "ربط المستشعرات والأجهزة بالشبكة لتتواصل وتتفاعل مع البيئة المحيطة ذاتيًا.")
    ]
    
    col1, col2 = st.columns(2)
    for i, (icon, title, desc) in enumerate(techs):
        target_col = col1 if i % 2 == 0 else col2
        with target_col:
            st.markdown(f'<div class="fun-card"><h4>{icon} {title}</h4><p>{desc}</p></div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# 3. تقنيات الذكاء الاصطناعي المتقدمة
# ---------------------------------------------------------
elif page == "🤖 تقنيات الذكاء الاصطناعي المتقدمة":
    st.markdown('<div class="main-card"><h2>🤖 عمق خوارزميات الذكاء الاصطناعي</h2></div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="fun-card">
        <h3>من التعلم الآلي (Machine Learning) إلى التعلم العميق (Deep Learning)</h3>
        <p style="font-size: 16px; line-height: 1.7;">
        الذكاء الاصطناعي هو المجال الأوسع، وتحته يندرج <b>التعلم الآلي</b> الذي يعتمد على خوارزميات تستخرج أنماطًا من البيانات. 
        أما <b>التعلم العميق</b> فهو فرع متقدم يحاكي بنية الخلايا العصبية في الدماغ البشري (Neural Networks) لمعالجة مهام شديدة التعقيد مثل القيادة الذاتية وترجمة اللغات الفورية.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### 🔬 مجالات تطبيقية رئيسية:")
    st.markdown(
        """
        *   🗣️ **معالجة اللغات الطبيعية (NLP):** تمكين الأنظمة من فهم وتحليل وتوليد النصوص والأصوات البشرية (مثل النماذج اللغوية الكبيرة).
        *   👁️ **رؤية الكمبيوتر (Computer Vision):** تدريب الأنظمة على تفسير وتحليل الصور ومقاطع الفيديو بدقة فائقة تفوق أحيانًا القدرة البشرية.
        *   🤖 **الأنظمة الذكية المستقلة:** الروبوتات والمركبات ذاتية القيادة التي تتخذ قراراتها في الزمن الحقيقي (Real-time).
        """,
    )

# ---------------------------------------------------------
# 4. الأمن السيبراني والأخلاقيات
# ---------------------------------------------------------
elif page == "🔒 الأمن السيبراني والأخلاقيات":
    st.markdown('<div class="main-card"><h2>🔒 الأمن السيبراني وأخلاقيات التقنية</h2></div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="fun-card">
        <h3>حماية الفضاء الرقمي</h3>
        <p style="font-size: 16px; line-height: 1.7;">
        مع زيادة الاعتماد على التقنية، تصبح حماية البيانات والبنى التحتية من الهجمات السيبرانية أولوية قصوى للدول والشركات.
        يشمل الأمن السيبراني تأمين الشبكات، تشفير البيانات، واكتشاف الثغرات الأمنية قبل استغلالها.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="fun-card">
        <h3>⚖️ أخلاقيات الذكاء الاصطناعي</h3>
        <p style="font-size: 16px; line-height: 1.7;">
        يطرح التطور السريع للذكاء الاصطناعي تحديات أخلاقية، مثل:
        <br>1. <b>الخصوصية:</b> حماية بيانات الأفراد الشخصية من الاستخدام غير المرخص.
        <br>2. <b>التحيز الخوارزمي:</b> ضمان حيادية الأنظمة الذكية وعدم تمييزها بناءً على العرق أو الجنس.
        <br>3. <b>المسؤولية القانونية:</b> تحديد المسؤول عن الأخطاء التي ترتكبها الأنظمة الذاتية.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

# ---------------------------------------------------------
# 5. مختبر الذكاء الاصطناعي
# ---------------------------------------------------------
elif page == "🧪 مختبر الذكاء الاصطناعي":
    st.markdown('<div class="main-card"><h2>🧪 محاكي خوارزميات معالجة النصوص الذكية</h2></div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="fun-card"><p>أدخل نصًا أو استفسارًا تقنيًا، وسيقوم النموذج المحاكي بتحليل محتواه وتصنيفه وتوليد استجابة علمية مبدئية:</p></div>',
        unsafe_allow_html=True,
    )

    user_query = st.text_input("📝 أدخل استفسارك التقني أو الكلمة المفتاحية:", placeholder="مثال: الأمن السيبراني، سحابة، خوارزمية")

    knowledge_base = {
        "أمن": "🛡️ التحليل: يقع هذا الاستفسار ضمن نطاق (الأمن السيبراني وحماية البيانات). النصائح: تفعيل المصادقة الثنائية وتجنب الروابط الوهمية.",
        "سحاب": "☁️ التحليل: يتعلق الاستفسار بـ (الحوسبة السحابية). المزايا: مرونة التشغيل، خفض التكاليف التشغيلية، والوصول العالمي للبيانات.",
        "ذكاء": "🧠 التحليل: يتعلق بـ (الذكاء الاصطناعي). التوجهات الحديثة تركز على النماذج التوليدية وتعلم الآلة المتقدم.",
        "برمج": "💻 التحليل: يتعلق بـ (هندسة البرمجيات وتطوير الأنظمة). يُنصح باتباع مبادئ البرمجة نظيفة الكود واختبارات الجودة الآلية."
    }

    if user_query:
        with st.spinner("🔄 جاري معالجة النص عبر النموذج وتحليل الأنماط..."):
            time.sleep(1)
        
        match_found = False
        for key, val in knowledge_base.items():
            if key in user_query:
                st.markdown(f'<div class="fun-card"><h3>نتيجة التحليل الذكي:</h3><p style="font-size: 18px;">{val}</p></div>', unsafe_allow_html=True)
                match_found = True
                break
        
        if not match_found:
            st.markdown(f'<div class="fun-card"><h3>نتيجة التحليل الذكي:</h3><p style="font-size: 18px;">🤖 استجابة عامة: موضوع "{user_query}" يمثل أحد الركائز الحيوية في مسيرة التحول الرقمي والابتكار التقني الحديث.</p></div>', unsafe_allow_html=True)

# ---------------------------------------------------------
# 6. التحدي التقني والمسابقة
# ---------------------------------------------------------
elif page == "🎯 التحدي التقني والمسابقة":
    st.markdown('<div class="main-card"><h2>🎯 التحدي التقني النهائي (اختبر معلوماتك وسجل بالمسابقة)</h2></div>', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="fun-card">
        <p>أجب عن الأسئلة التقنية التالية، ثم أدخل بياناتك (الاسم ورقم الجوال) لتسجيل درجاتك في سجلات أكاديمية نمو العالي للتدريب! 🏆</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    with st.form("competition_form"):
        st.markdown("### بيانات المتسابق:")
        participant_name = st.text_input("👤 الاسم الكامل:")
        participant_phone = st.text_input("📱 رقم الجوال (مثال: 05XXXXXXXX):")

        st.markdown("---")
        st.markdown("### أسئلة التحدي:")

        q1 = st.radio(
            "1. أي مما يلي يُعتبر المكون الأساسي الذي يحاكي الشبكات العصبية للبشر في الذكاء الاصطناعي المتقدم؟",
            ["الخوارزميات التقليدية", "الشبكات العصبية العميقة (Deep Neural Networks)", "جداول البيانات الثابتة"],
            index=None
        )

        q2 = st.radio(
            "2. ما هي الفائدة الرئيسية للحوسبة السحابية للشركات؟",
            ["الاعتماد كليًا على الخوادم المحلية الصعبة الصيانة", "مرونة الوصول للموارد وخفض التكاليف التشغيلية", "إبطاء معالجة البيانات لحمايتها"],
            index=None
        )

        q3 = st.radio(
            "3. أي من الآتي يمثل ممارسة صحيحة في الأمن السيبراني الشخصي؟",
            ["استخدام كلمة مرور موحدة وسهلة لكل الحسابات", "تفعيل المصادقة الثنائية (2FA) وتحديث البرمجيات دورياً", "النقر على الروابط غير المعروفة لغرض الفحص"],
            index=None
        )

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
                <p>تم حفظ بياناتك ورقم جوالك ({participant_phone}) في قاعدة بيانات الأكاديمية بنجاح.</p>
                </div>
                """, unsafe_allow_html=True)

                if score == 3:
                    st.balloons()
                    st.markdown("<h3 style='text-align: center; color: #4ade80;'>🏆 أداء ممتاز! لقد اجتزت التحدي بجدارة واستحقاق.</h3>", unsafe_allow_html=True)

                try:
                    data = {
                        "الاسم": [participant_name],
                        "رقم الجوال": [participant_phone],
                        "الدرجة": [score],
                        "وقت التسجيل": [datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
                    }
                    df = pd.DataFrame(data)
                    
                    try:
                        df_existing = pd.read_csv("participants_results.csv")
                        df_combined = pd.concat([df_existing, df], ignore_index=True)
                        df_combined.to_csv("participants_results.csv", index=False, encoding="utf-8-sig")
                    except FileNotFoundError:
                        df.to_csv("participants_results.csv", index=False, encoding="utf-8-sig")
                        
                except Exception as e:
                    print(f"خطأ في الحفظ: {e}")

# ---------------------------------------------------------
# تذييل الصفحة
# ---------------------------------------------------------
st.markdown("---")
st.markdown(
    """
    <div style="text-align:center; color:#94a3b8; font-size:14px;">
    🎓 أكاديمية نمو العالي للتدريب © 2026 — بناء القدرات الرقمية لشباب المستقبل 🌟
    </div>
    """,
    unsafe_allow_html=True,
)
