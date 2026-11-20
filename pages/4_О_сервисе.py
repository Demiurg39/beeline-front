import streamlit as st
from components.styles import inject_css
from components.header import render_header
from components.image_utils import get_image_base64
from components.cards import UICards
from templates.about_html import get_hero_html, get_step_html, get_info_card_html

st.set_page_config(page_title="О сервисе — Tariffly", layout="wide")
inject_css()
render_header("about")

def get_icon(name):
    return get_image_base64(f"assets/{name}.png")

icon_hero = get_icon("hero_phone")
icon_check = get_icon("icon_check_circle")
icon_shield = get_icon("db_phone")
icon_support = get_icon("icon_sms")

# Hero
st.markdown(get_hero_html(icon_hero), unsafe_allow_html=True)

# Steps
st.markdown('<h2 style="text-align: center; color: #0F172A; margin-bottom: 40px;">Как это работает?</h2>', unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(get_step_html(icon_check, 1, "Введите номер", "Загрузите данные или введите номер телефона для начала анализа."), unsafe_allow_html=True)
with col2:
    st.markdown(get_step_html(icon_check, 2, "Получите анализ", "Мы сравним ваши расходы с актуальными тарифами операторов."), unsafe_allow_html=True)
with col3:
    st.markdown(get_step_html(icon_check, 3, "Экономьте", "Переходите на выгодный тариф и оставайтесь на связи без переплат."), unsafe_allow_html=True)

st.write("")
st.write("")

# Info Cards
col_sec, col_sup = st.columns(2)
with col_sec:
    st.markdown(get_info_card_html(icon_shield, "Ваши данные под защитой", "Мы не сохраняем ваши персональные данные и историю звонков. Вся информация используется только в момент расчета и сразу удаляется."), unsafe_allow_html=True)
with col_sup:
    st.markdown(get_info_card_html(icon_support, "Есть вопросы?", "Это демонстрационная версия, созданная в рамках хакатона INAI. Если у вас есть вопросы, напишите нам."), unsafe_allow_html=True)