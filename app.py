import streamlit as st
import os

st.set_page_config(page_title="Luxury Style Selector", layout="wide")

st.markdown("""
<style>

/* 背景（グラデーション強化） */
.stApp {
    background: linear-gradient(120deg, #fceabb 0%, #f8b500 30%, #fddb92 60%, #d1fdff 100%);
}

/* ヘッダー */
.header {
    text-align: center;
    padding: 50px 20px;
    color: white;
    background: linear-gradient(135deg, #1f1c2c, #928dab);
    border-radius: 30px;
    box-shadow: 0 15px 40px rgba(0,0,0,0.3);
    margin-bottom: 30px;
}

.title {
    font-size: 50px;
    font-weight: 900;
    letter-spacing: 2px;
}

.subtitle {
    font-size: 18px;
    opacity: 0.9;
}

/* 選択エリア */
.selector {
    background: rgba(255,255,255,0.85);
    padding: 25px;
    border-radius: 25px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    margin-bottom: 30px;
}

/* 結果カード */
.card {
    background: linear-gradient(135deg, #ffffff, #f5f7fa);
    padding: 30px;
    border-radius: 30px;
    box-shadow: 0 20px 50px rgba(0,0,0,0.25);
    text-align: center;
    animation: fadeIn 1s ease-in-out;
}

/* タイトル */
.card-title {
    font-size: 32px;
    font-weight: bold;
    margin-bottom: 10px;
}

/* バッジ */
.badge {
    display: inline-block;
    padding: 8px 16px;
    margin: 5px;
    border-radius: 999px;
    background: linear-gradient(135deg, #667eea, #764ba2);
    color: white;
    font-size: 14px;
}

/* アニメーション */
@keyframes fadeIn {
    from {opacity: 0; transform: translateY(20px);}
    to {opacity: 1; transform: translateY(0);}
}

</style>
""", unsafe_allow_html=True)

# ヘッダー
st.markdown("""
<div class="header">
    <div class="title">✨ Fashion Selector ✨</div>
    <div class="subtitle">あなたに最適なコーデを一瞬で提案</div>
</div>
""", unsafe_allow_html=True)

# 選択UI
st.markdown('<div class="selector">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox("性別", ["男性", "女性"])

with col2:
    season = st.selectbox("季節", ["春", "夏", "秋", "冬"])

with col3:
    style = st.selectbox("スタイル", ["オフィスカジュアル", "ビジネスカジュアル"])

st.markdown('</div>', unsafe_allow_html=True)

# マッピング
gender_map = {"男性": "men", "女性": "women"}
season_map = {"春": "spring", "夏": "summer", "秋": "autumn", "冬": "winter"}
style_map = {"オフィスカジュアル": "office", "ビジネスカジュアル": "business"}

emoji = {"春": "🌸", "夏": "🌻", "秋": "🍁", "冬": "❄️"}

image_name = f"{season_map[season]}_{gender_map[gender]}_{style_map[style]}.jpg"

# コーデ提案
def recommend_outfit(season, gender, style):

    advice_dict = 
        ("春", "ビジネスカジュアル"): "春らしい軽めのジャケットを取り入れたビジネスカジュアルがおすすめです。",
        ("春", "オフィスカジュアル"): "春らしく柔らかい印象のオフィスカジュアルがおすすめです。",
        ("夏", "ビジネスカジュアル"): "夏向けの涼しいビジネスカジュアルがおすすめです。",
        ("夏", "オフィスカジュアル"): "涼しさを重視した軽やかなオフィスカジュアルがおすすめです。",
        ("秋", "ビジネスカジュアル"): "秋らしい落ち着いた色合いのビジネスカジュアルがおすすめです。",
        ("秋", "オフィスカジュアル"): "秋らしい柔らかな雰囲気のオフィスカジュアルがおすすめです。",
        ("冬", "ビジネスカジュアル"): "暖かさを重視した冬のビジネスカジュアルがおすすめです。",
        ("冬", "オフィスカジュアル"): "暖かく上品な冬のオフィスカジュアルがおすすめです。"

# 中央寄せ
left, center, right = st.columns([1,3,1])

with center:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.markdown(f'<div class="card-title">{emoji[season]} {season}のコーデ</div>', unsafe_allow_html=True)

    st.markdown(f"""
    <span class="badge">{gender}</span>
    <span class="badge">{season}</span>
    <span class="badge">{style}</span>
    """, unsafe_allow_html=True)

    if os.path.exists(image_name):
        st.image(image_name, use_container_width=True)
    else:
        st.error("画像が見つかりません")

    st.markdown('</div>', unsafe_allow_html=True)
