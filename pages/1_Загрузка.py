import streamlit as st
import time
from components.styles import inject_css
from components.header import render_header
from services.mock_api import MockAPI

st.set_page_config(page_title="Вход — Tariffly", layout="wide")
inject_css()
render_header("home")

# Делаем две колонки: слева текст и ввод, справа картинка
col_left, col_right = st.columns([1, 1], gap="large")

with col_left:
    st.markdown(
        '<h2 style="color: #252044; font-weight: 800; margin-top: 50px;">Узнайте, сколько вы можете сэкономить</h2>',
        unsafe_allow_html=True)
    st.markdown(
        '<p style="color: #6E688F; font-size: 1.1rem; margin-bottom: 40px;">Введите ваш номер телефона. Мы сами запросим детализацию из базы оператора.</p>',
        unsafe_allow_html=True)

    # Поле ввода
    phone = st.text_input("Номер телефона", placeholder="+996 555 123 456", label_visibility="collapsed")
    st.write("")

    if st.button("Проанализировать тарифы", type="primary", use_container_width=True):
        if not phone or len(phone) < 9:
            st.error("Пожалуйста, введите корректный номер телефона.")
        else:
            with st.status("Анализируем ваш номер...", expanded=True) as status:
                st.write("🔌 Подключаемся к базе оператора...")
                time.sleep(1)
                st.write("📊 Загружаем детализацию за 3 месяца...")
                time.sleep(1)
                st.write("🧠 Нейросеть подбирает лучший вариант...")
                result = MockAPI.fetch_user_data_by_phone(phone)
                status.update(label="Анализ завершен!", state="complete", expanded=False)

            st.session_state['result'] = result
            st.session_state['phone'] = phone
            st.switch_page("pages/2_Результаты.py")

    st.markdown(
        '<div style="color: #6E688F; font-size: 0.8rem; margin-top: 20px;">🔒 Мы не сохраняем ваши данные. Это демо-версия для хакатона.</div>',
        unsafe_allow_html=True)

with col_right:
    # Картинка базы данных
    st.image("assets/db_phone.png", use_container_width=True)