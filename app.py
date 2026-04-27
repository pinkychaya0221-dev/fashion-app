import streamlit as st
import os

st.set_page_config(
    page_title="コーデ提案アプリ",
    page_icon="👔",
    layout="wide"
)

st.markdown("""
<style>
.main {
    background-color: #fafafa;
}
.title {
    text-align: center;
    font-size: 36px;
    font-weight: bold;
}
.subtitle {
    text-align: center;
    color: #666;
    font-size: 18px;
    margin-bottom: 30px;
}
.card {
    background-color: white;
    padding: 24px;
    border-radius: 18px;
    box-shadow: 0 4px 16px rgba(0,0,0,0.08);
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">ビジネスコーデ提案アプリ</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">季節・性別・スタイルを選ぶだけで、おすすめコーデを表示します</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox("性別", ["男性", "女性"])

with col2:
    season = st.selectbox("季節", ["春", "夏", "秋", "冬"])

with col3:
    style = st.selectbox("スタイル", ["オフィスカジュアル", "ビジネスカジュアル"])

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

image_name = f"{season_map[season]}_{gender_map[gender]}_{style_map[style]}.jpg"

st.markdown("---")

left, center, right = st.columns([1, 3, 1])

with center:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader(f"{season}の{style}コーデ")
    st.write(f"選択条件：{gender} / {season} / {style}")

    if os.path.exists(image_name):
        st.image(image_name, use_container_width=True)
    else:
        st.warning(f"画像がまだありません：{image_name}")

    st.markdown('</div>', unsafe_allow_html=True)
