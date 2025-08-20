import streamlit as st
import random

st.set_page_config(page_title="إشارة خيار الجيب", page_icon="📊", layout="centered")

st.title("📊 إشارة خيار الجيب (نسخة عربية)")
st.markdown("أداة تجريبية لإشارات بيع / شراء")

# واجهة الإدخال
st.subheader("إعدادات التحليل")
asset = st.selectbox("اختر الأصل:", ["EUR/USD", "GBP/USD", "USD/JPY", "BTC/USD"])
timeframe = st.selectbox("الإطار الزمني:", ["دقيقة", "5 دقائق", "15 دقيقة", "ساعة"])

# زر التحليل
if st.button("تحليل"):
    signal = random.choice(["شراء ✅", "بيع ❌", "انتظار ⏳"])
    st.success(f"الإشارة الحالية لـ {asset} على إطار {timeframe} هي: **{signal}**")

st.info("⚠️ هذه النسخة تجريبية تعليمية، وليست توصية مالية.")
