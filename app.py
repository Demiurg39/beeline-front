import streamlit as st
from components.styles import inject_css
from components.header import render_header
from components.image_utils import get_image_base64

st.set_page_config(page_title="Tariffly", page_icon="📊", layout="wide")
inject_css()
render_header("home")

# Hero Section
col1, col2 = st.columns([1.1, 1])
with col1:
    st.markdown(
        '<span style="background: #EAE4FF; color: #4B3A9C; padding: 6px 16px; border-radius: 20px; font-size: 0.9rem; font-weight: 700;">Умный подбор тарифа</span>',
        unsafe_allow_html=True)
    st.markdown(
        '<h1 style="color: #252044; font-size: 3.5rem; font-weight: 800; line-height: 1.1; margin-top: 20px; margin-bottom: 20px;">Найдите самый<br>выгодный<br>мобильный тариф</h1>',
        unsafe_allow_html=True)
    st.markdown(
        '<p style="color: #6E688F; font-size: 1.1rem; line-height: 1.6; margin-bottom: 30px;">Загрузите детализацию расходов за последние три месяца, и мы подберём тариф, который поможет вам экономить.</p>',
        unsafe_allow_html=True)

    if st.button("Подобрать тариф →", type="primary"):
        st.switch_page("pages/1_Загрузка.py")

with col2:
    # Вставляем красивую картинку смартфона
    # use_container_width=True заставит картинку подстроиться под ширину колонки
    st.image("assets/hero_phone.png", use_container_width=True)

st.write("---")

# Карточки преимуществ
# Карточки преимуществ
c1, c2, c3, c4 = st.columns(4)

# Получаем base64 строки для картинок
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
        # Вставляем base64 в src
        st.markdown(f'''
        <div style="background: white; border: 1px solid #E8E1FB; border-radius: 16px; padding: 16px; display: flex; align-items: center; gap: 16px; box-shadow: 0 4px 12px rgba(0,0,0,0.02);">
            <img src="data:image/png;base64,{icon_b64}" width="50" style="object-fit: contain;">
            <div>
                <div style="font-weight: 700; color: #252044; font-size: 1rem; margin-bottom: 2px;">{title}</div>
                <div style="color: #6E688F; font-size: 0.8rem;">{subtitle}</div>
            </div>
        </div>
        ''', unsafe_allow_html=True)

st.write("")
st.write("")
st.write("")

# Оборачиваем все в контейнер с фоном
st.markdown('<div style="background: white; border: 1px solid #E8E1FB; border-radius: 24px; padding: 40px; box-shadow: 0 10px 30px rgba(116,82,214,0.05);">', unsafe_allow_html=True)
st.markdown('<h2 style="text-align: center; color: #252044; font-weight: 800; margin-bottom: 40px; margin-top: 0;">Как это работает?</h2>', unsafe_allow_html=True)

step1, arrow1, step2, arrow2, step3 = st.columns([2, 1, 2, 1, 2])

def render_step(col, num, title, text):
    with col:
        st.markdown(f'''
        <div style="text-align: center;">
            <div style="background: #EFEAFF; color: #7452D6; width: 48px; height: 48px; border-radius: 50%; display: flex; align-items: center; justify-content: center; font-weight: 800; margin: 0 auto 16px auto; font-size: 1.4rem;">{num}</div>
            <div style="font-weight: 800; color: #252044; font-size: 1.1rem; margin-bottom: 8px;">{title}</div>
            <div style="color: #6E688F; font-size: 0.9rem; line-height: 1.5;">{text}</div>
        </div>
        ''', unsafe_allow_html=True)

def render_arrow(col):
    with col:
        st.markdown('<div style="text-align: center; color: #C9B8F5; font-size: 1.5rem; margin-top: 15px;">→</div>', unsafe_allow_html=True)

render_step(step1, "1", "Загрузите номер", "Введите свой номер телефона")
render_arrow(arrow1)
render_step(step2, "2", "Получите анализ", "ИИ изучит ваши расходы")
render_arrow(arrow2)
render_step(step3, "3", "Экономьте", "Перейдите на выгодный тариф")

st.markdown('</div>', unsafe_allow_html=True) # Закрываем контейнер