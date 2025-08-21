import streamlit as st
import random
# إعداد الصفحة
st.set_page_config(page_title="إشارة خيار الجيب — النسخة التجريبية")

# العنوان الرئيسي
st.title("📊 إشارة خيار الجيب — النسخة التجريبية")
st.markdown("أداة تجريبية لإشارات بيع / شراء")

# واجهة الإدخال
st.subheader("إعدادات التحليل")
asset = st.selectbox("اختر الأصل:", ["EUR/USD", "GBP/USD", "USD/JPY"])
timeframe = st.selectbox("الإطار الزمني:", ["15 دقيقة", "ساعة", "يوم"])

# زر التحليل
if st.button("تحليل"):
    signal = random.choice(["✅ شراء", "❌ بيع", "⏳ انتظار"])
    st.success(f"الإشارة الحالية ({signal}) على إطار {timeframe} لزوج {asset}")
