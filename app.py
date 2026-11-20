import streamlit as st
from components.styles import inject_css
from components.header import render_header
from components.image_utils import get_image_base64

st.set_page_config(page_title="Tariffly", page_icon="📊", layout="wide")
inject_css()
render_header("home")

# --- HERO SECTION ---
col1, col2 = st.columns([1.2, 1], gap="medium")
with col1:
    st.markdown(
        '<span style="background: #EAE4FF; color: #4B3A9C; padding: 6px 16px; border-radius: 20px; font-size: 0.9rem; font-weight: 700;">Умный подбор тарифа</span>',
        unsafe_allow_html=True)

    st.markdown(
        '<h1 style="color: #0F172A; font-size: 3.2rem; font-weight: 800; line-height: 1.1; margin-top: 20px; margin-bottom: 20px;">Найдите тариф,<br>который подходит<br>именно вам</h1>',
        unsafe_allow_html=True)
    st.markdown(
        '<p style="color: #64748B; font-size: 1.1rem; line-height: 1.6; margin-bottom: 30px;">Анализируйте свои расходы и получайте<br>рекомендации по лучшим тарифам<br>от всех операторов Кыргызстана.</p>',
        unsafe_allow_html=True)

    if st.button("Подобрать тариф →", type="primary"):
        st.switch_page("pages/1_Загрузка.py")

with col2:
    img_hero = get_image_base64("assets/hero_phone.png")
    if img_hero:
        st.markdown(
            f'<div style="display: flex; justify-content: center; align-items: center; height: 100%;"><img src="data:image/png;base64,{img_hero}" style="max-width: 400px; width: 100%; height: auto;"></div>',
            unsafe_allow_html=True)
    else:
        st.image("assets/hero_phone.png", use_container_width=True)

st.write("")
st.write("")  # Чуть больше отступа перед карточками

# --- КАРТОЧКИ ПРЕИМУЩЕСТВ (Увеличенные) ---
c1, c2, c3, c4 = st.columns(4, gap="medium")

img_phone = get_image_base64("assets/icon_phone.png")
img_globe = get_image_base64("assets/icon_globe.png")
img_sms = get_image_base64("assets/icon_sms.png")
img_money = get_image_base64("assets/icon_money.png")

cards_data = [
    (img_phone, "Минуты", "Анализ звонков"),
    (img_globe, "Интернет", "Анализ трафика"),
    (img_sms, "SMS", "Анализ сообщений"),
    (img_money, "Экономия", "Снижение расходов")
]

for col, (icon_b64, title, subtitle) in zip([c1, c2, c3, c4], cards_data):
    with col:
        # Увеличили padding до 24px, иконку до 48px, шрифты тоже стали больше
        st.markdown(f'''
        <div style="background: white; border: 1px solid #E8E1FB; border-radius: 20px; padding: 24px 20px; display: flex; align-items: center; gap: 16px; box-shadow: 0 8px 24px rgba(116,82,214,0.06); height: 100%;">
            <img src="data:image/png;base64,{icon_b64}" width="48" style="object-fit: contain;">
            <div>
                <div style="font-weight: 800; color: #0F172A; font-size: 1.1rem; margin-bottom: 4px;">{title}</div>
                <div style="color: #64748B; font-size: 0.85rem;">{subtitle}</div>
            </div>
        </div>
        ''', unsafe_allow_html=True)