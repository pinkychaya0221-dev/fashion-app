import streamlit as st
import os

st.set_page_config(
    page_title="Smart Office Style",
    page_icon="👔",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #f8f6f2 0%, #fdfdfd 45%, #eef3f8 100%);
}

.block-container {
    padding-top: 2rem;
    max-width: 1100px;
}

.hero {
    text-align: center;
    padding: 34px 20px 26px;
    border-radius: 28px;
    background: rgba(255,255,255,0.78);
    box-shadow: 0 12px 35px rgba(0,0,0,0.08);
    margin-bottom: 28px;
}

.hero-title {
    font-size: 42px;
    font-weight: 800;
    letter-spacing: 1px;
    color: #2f3542;
}

.hero-subtitle {
    font-size: 17px;
    color: #6c7078;
    margin-top: 10px;
}

.select-card {
    background: rgba(255,255,255,0.86);
    padding: 24px;
    border-radius: 24px;
    box-shadow: 0 10px 28px rgba(0,0,0,0.07);
    margin-bottom: 26px;
}

.result-card {
    background: #ffffff;
    padding: 26px;
    border-radius: 28px;
    box-shadow: 0 16px 40px rgba(0,0,0,0.10);
    border: 1px solid rgba(0,0,0,0.04);
}

.result-title {
    font-size: 26px;
    font-weight: 700;
    color: #2f3542;
    margin-bottom: 6px;
}

.result-subtitle {
    color: #777;
    font-size: 15px;
    margin-bottom: 18px;
}

.badge {
    display: inline-block;
    padding: 7px 14px;
    border-radius: 999px;
    background: #f1eee8;
    color: #555;
    font-size: 14px;
    margin-right: 8px;
    margin-bottom: 14px;
}

.footer {
    text-align: center;
    color: #999;
    font-size: 13px;
    margin-top: 32px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero">
    <div class="hero-title">Smart Office Style</div>
    <div class="hero-subtitle">季節・性別・スタイルに合わせて、きれいめコーデを提案します</div>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="select-card">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox("Gender / 性別", ["男性", "女性"])

with col2:
    season = st.selectbox("Season / 季節", ["春", "夏", "秋", "冬"])

with col3:
    style = st.selectbox("Style / スタイル", ["オフィスカジュアル", "ビジネスカジュアル"])

st.markdown('</div>', unsafe_allow_html=True)

gender_map = {
    "男性": "men",
    "女性": "women"
}

season_map = {
    "春": "spring",
    "夏": "summer",
    "秋": "autumn",
    "冬": "winter"
}

style_map = {
    "オフィスカジュアル": "office",
    "ビジネスカジュアル": "business"
}

season_emoji = {
    "春": "🌸",
    "夏": "🌻",
    "秋": "🍂",
    "冬": "❄️"
}

image_name = f"{season_map[season]}_{gender_map[gender]}_{style_map[style]}.jpg"

left, center, right = st.columns([0.6, 3.8, 0.6])

with center:
    st.markdown('<div class="result-card">', unsafe_allow_html=True)

    st.markdown(
        f'<div class="result-title">{season_emoji[season]} {season}の{style}コーデ</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="result-subtitle">選択条件に合わせたおすすめスタイル</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f"""
        <span class="badge">{gender}</span>
        <span class="badge">{season}</span>
        <span class="badge">{style}</span>
        """,
        unsafe_allow_html=True
    )

    if os.path.exists(image_name):
        st.image(image_name, use_container_width=True)
    else:
        st.warning(f"画像がまだありません：{image_name}")

    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('<div class="footer">Office coordinate guide｜Seasonal styling app</div>', unsafe_allow_html=True)
