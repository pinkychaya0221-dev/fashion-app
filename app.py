import streamlit as st
import os
import streamlit.components.v1 as components

st.set_page_config(page_title="Luxury Style Selector", layout="wide")

st.markdown("""
<style>

/* ヘッダー */
.header {
    text-align: center;
    padding: 50px 20px;
    color: white;
    background: rgba(255,255,255,0.2);
backdrop-filter: blur(10px);
    border-radius: 30px;
    box-shadow: 0 15px 40px rgba(0,0,0,0.3);
    margin-bottom: 30px;
}

.title {
    font-size: 50px;
    font-weight: 900;
    letter-spacing: 2px;
    color: #555;
}

.subtitle {
    font-size: 18px;
    opacity: 0.9;
    color: #555;
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

    st.markdown(audio_html, unsafe_allow_html=True)
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
    <div class="title">👔Style Navi</div>
    <div class="subtitle">あなたに最適なコーデを瞬時に提案</div>
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

bg = get_background(season)

def get_animation_html(season):
    if season == "春":
        icon = "🌸"
    elif season == "夏":
        icon = "🎆"
    elif season == "秋":
        icon = "🍂"
    else:
        icon = "❄️"

    return f"""
    <div class="season-animation">
        <span>{icon}</span><span>{icon}</span><span>{icon}</span><span>{icon}</span>
        <span>{icon}</span><span>{icon}</span><span>{icon}</span><span>{icon}</span>
    </div>
    """

animation_html = get_animation_html(season)

st.markdown(f"""
<style>
.stApp {{
    background: {bg} !important;
}}

.season-animation {{
    position: fixed;
    inset: 0;
    pointer-events: none;
    overflow: hidden;
    z-index: 999;
}}

.season-animation span {{
    position: absolute;
    top: -50px;
    font-size: 32px;
    animation: fall 8s linear infinite;
}}

.season-animation span:nth-child(1) {{ left: 5%; animation-delay: 0s; }}
.season-animation span:nth-child(2) {{ left: 18%; animation-delay: 1s; }}
.season-animation span:nth-child(3) {{ left: 30%; animation-delay: 2s; }}
.season-animation span:nth-child(4) {{ left: 45%; animation-delay: 0.5s; }}
.season-animation span:nth-child(5) {{ left: 60%; animation-delay: 1.5s; }}
.season-animation span:nth-child(6) {{ left: 75%; animation-delay: 2.5s; }}
.season-animation span:nth-child(7) {{ left: 88%; animation-delay: 3s; }}
.season-animation span:nth-child(8) {{ left: 95%; animation-delay: 4s; }}

@keyframes fall {{
    0% {{ transform: translateY(-60px) rotate(0deg); opacity: 0; }}
    10% {{ opacity: 1; }}
    100% {{ transform: translateY(110vh) rotate(360deg); opacity: 0; }}
}}
</style>

""", unsafe_allow_html=True)

components.html(animation_html, height=0)

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
    ("spring", "men", "office"): "春の空気に合う軽やかなコーデ。清潔感とやわらかさで好印象。",
    ("spring", "men", "business"): "落ち着いたカラーでまとめたビジネスカジュアル。初対面でも好印象。",
    ("spring", "women", "office"): "春のやわらかい空気にぴったりの軽やかコーデ。",
    ("spring", "women", "business"): "春らしい抜け感で自然体に仕上がる着こなし。",
    
    ("summer", "men", "office"): "軽やかな素材感でまとめたオフィスコーデ。暑い日でもすっきりとした印象に。",
    ("summer", "men", "business"): "シンプルで整った印象のビジネスカジュアル。気温に合わせて調節しやすい着こなし。",
    ("summer", "women", "office"): "さらっと着れて見た目も爽やかなスタイル。",
    ("summer", "women", "business"): "やわらかな雰囲気でまとめた夏のビジネスカジュアル。清潔感のある上品な印象に。",
    
    ("autumn", "men", "office"): "通気性重視の爽やかオフィススタイル。ジャケットは軽量素材がおすすめ。",
    ("autumn", "men", "business"): "シャツ1枚でも成立する涼しげなビジカジ。シンプルで清潔感重視。",
    ("autumn", "women", "office"): "通気性重視の爽やかオフィススタイル。ジャケットは軽量素材がおすすめ。",
    ("autumn", "women", "business"): "シャツ1枚でも成立する涼しげなビジカジ。シンプルで清潔感重視。",

    ("winter", "men", "office"): "落ち着いた色味で知的な印象に。秋らしい深みカラーがポイント。",
    ("winter", "men", "business"): "ニット＋コートで上品な防寒ビジカジ。シルエット重視でスタイルアップ。",
    ("winter", "women", "office"): "落ち着いた色味で知的な印象に。秋らしい深みカラーがポイント。",
    ("winter", "women", "business"): "ニット＋コートで上品な防寒ビジカジ。シルエット重視でスタイルアップ。",
}

import random
import base64

music_folder = "music"

if not os.path.exists(music_folder):
    st.error("musicフォルダがありません")
else:
    music_files = [
        f for f in os.listdir(music_folder)
        if f.endswith((".mp3", ".wav"))
    ]

    if not music_files:
        st.warning("音楽ファイルがありません")
    else:
        if "selected_music" not in st.session_state:
            st.session_state.selected_music = random.choice(music_files)

        selected_music = st.session_state.selected_music
        music_path = os.path.join(music_folder, selected_music)

        with open(music_path, "rb") as f:
            audio_bytes = f.read()
            audio_base64 = base64.b64encode(audio_bytes).decode()

        audio_html = f"""
        <audio autoplay loop onloadeddata="this.volume=0.2">
            <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
        </audio>
        """

        st.markdown(audio_html, unsafe_allow_html=True)

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
