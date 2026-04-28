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

def get_background(season):
    if season == "春":
        return "linear-gradient(120deg, #ffe4ec 0%, #fff0f5 40%, #e8f5e9 100%)"
    elif season == "夏":
        return "linear-gradient(120deg, #d1f7ff 0%, #87ceeb 40%, #fffacd 100%)"
    elif season == "秋":
        return "linear-gradient(120deg, #fff3cd 0%, #d2691e 45%, #8b4513 100%)"
    elif season == "冬":
        return "linear-gradient(120deg, #e0f7fa 0%, #e6e6fa 45%, #b0c4de 100%)"

def get_animation_html(season):
    if season == "夏":
        return """
        <div class="fireworks">
            <span>🎆</span><span>🎇</span><span>🎆</span>
        </div>
        """
    else:
        icon = {"春": "🌸", "秋": "🍂", "冬": "❄"}[season]
        return f"""
        <div class="floating">
            <span>{icon}</span><span>{icon}</span><span>{icon}</span><span>{icon}</span>
            <span>{icon}</span><span>{icon}</span><span>{icon}</span><span>{icon}</span>
        </div>
        """

st.markdown(f"""
<style>
.floating {{
    position: fixed;
    inset: 0;
    pointer-events: none;
    overflow: hidden;
    z-index: 0;
}}

.floating span {{
    position: absolute;
    top: -50px;
    font-size: 28px;
    animation: fall 8s linear infinite;
    opacity: 0.8;
}}

.floating span:nth-child(1) {{ left: 5%; animation-delay: 0s; }}
.floating span:nth-child(2) {{ left: 15%; animation-delay: 1s; }}
.floating span:nth-child(3) {{ left: 25%; animation-delay: 2s; }}
.floating span:nth-child(4) {{ left: 40%; animation-delay: 0.5s; }}
.floating span:nth-child(5) {{ left: 55%; animation-delay: 1.5s; }}
.floating span:nth-child(6) {{ left: 70%; animation-delay: 2.5s; }}
.floating span:nth-child(7) {{ left: 85%; animation-delay: 3s; }}
.floating span:nth-child(8) {{ left: 95%; animation-delay: 4s; }}

@keyframes fall {{
    0% {{ transform: translateY(-50px) rotate(0deg); opacity: 0; }}
    10% {{ opacity: 1; }}
    100% {{ transform: translateY(110vh) rotate(360deg); opacity: 0; }}
}}

.fireworks {{
    position: fixed;
    inset: 0;
    pointer-events: none;
    z-index: 0;
}}

.fireworks span {{
    position: absolute;
    font-size: 42px;
    animation: fireworks 2.5s ease-in-out infinite;
}}

.fireworks span:nth-child(1) {{ left: 20%; top: 20%; animation-delay: 0s; }}
.fireworks span:nth-child(2) {{ left: 50%; top: 15%; animation-delay: 0.8s; }}
.fireworks span:nth-child(3) {{ left: 75%; top: 25%; animation-delay: 1.6s; }}

@keyframes fireworks {{
    0% {{ transform: scale(0); opacity: 0; }}
    40% {{ transform: scale(1.5); opacity: 1; }}
    100% {{ transform: scale(0); opacity: 0; }}
}}
</style>

{get_animation_html(season)}
""", unsafe_allow_html=True)

bg = get_background(season)

st.markdown(f"""
<style>
.stApp {{
    background: {bg} !important;
}}
</style>
""", unsafe_allow_html=True)

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
