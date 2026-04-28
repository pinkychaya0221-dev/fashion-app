import streamlit as st
import os

st.set_page_config(page_title="Luxury Style Selector", layout="wide")

st.markdown("""
<style>

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

import streamlit as st
import random
import os

st.title("ランダム音楽プレイヤー")

# 音楽ファイルを入れたフォルダ
music_folder = "music"

# mp3一覧を取得
music_files = [f for f in os.listdir(music_folder) if f.endswith(".mp3")]

if music_files:
    # ボタンを押したらランダム選曲
    if st.button("ランダム再生"):
        selected_music = random.choice(music_files)
        st.write(f"再生中: {selected_music}")
        
        audio_path = os.path.join(music_folder, selected_music)
        st.audio(audio_path)
else:
    st.write("musicフォルダにmp3ファイルを入れてください")

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

def get_background(season):
    if season == "春":
        return "linear-gradient(120deg, #ffe4ec 0%, #fff0f5 40%, #e8f5e9 100%)"
    elif season == "夏":
        return "linear-gradient(120deg, #d1f7ff 0%, #87ceeb 40%, #fffacd 100%)"
    elif season == "秋":
        return "linear-gradient(120deg, #fff3cd 0%, #d2691e 45%, #8b4513 100%)"
    elif season == "冬":
        return "linear-gradient(120deg, #e0f7fa 0%, #e6e6fa 45%, #b0c4de 100%)"

with col3:
    style = st.selectbox("スタイル", ["オフィスカジュアル", "ビジネスカジュアル"])

st.markdown('</div>', unsafe_allow_html=True)

# マッピング
gender_map = {"男性": "men", "女性": "women"}
season_map = {"春": "spring", "夏": "summer", "秋": "autumn", "冬": "winter"}
style_map = {"オフィスカジュアル": "office", "ビジネスカジュアル": "business"}

emoji = {"春": "🌸", "夏": "🌻", "秋": "🍁", "冬": "❄️"}

image_name = f"{season_map[season]}_{gender_map[gender]}_{style_map[style]}.jpg"
comment_map = {
    ("spring", "men", "office"): "春らしい軽やかなジャケットスタイル。清潔感と柔らかさを両立した好印象コーデ。",
    ("spring", "men", "business"): "明るめシャツで季節感を出したビジネスカジュアル。初対面でも好印象。",
    
    ("summer", "men", "office"): "通気性重視の爽やかオフィススタイル。ジャケットは軽量素材がおすすめ。",
    ("summer", "men", "business"): "シャツ1枚でも成立する涼しげなビジカジ。シンプルで清潔感重視。",
    
    ("autumn", "women", "office"): "落ち着いた色味で知的な印象に。秋らしい深みカラーがポイント。",
    ("winter", "women", "business"): "ニット＋コートで上品な防寒ビジカジ。シルエット重視でスタイルアップ。",
}

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
    key = (season_map[season], gender_map[gender], style_map[style])
comment = comment_map.get(key, "このスタイルはシンプルで汎用性の高いコーデです。")

st.markdown(f"""
<div style="
    margin-top: 20px;
    padding: 15px;
    border-radius: 15px;
    background: rgba(255,255,255,0.7);
    font-size: 16px;
    line-height: 1.6;
">
    💡 {comment}
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
