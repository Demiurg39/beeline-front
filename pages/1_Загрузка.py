import streamlit as st
import time
from components.styles import inject_css
from components.header import render_header
from services.backend_mock import get_subscriber_id_by_phone

st.set_page_config(page_title="Вход — Tariffly", layout="wide")
inject_css()
render_header("home")

col_left, col_right = st.columns([1, 1.1], gap="large")

with col_left:
    st.markdown(
        '<h2 style="color: #0F172A; font-weight: 800; margin-top: 30px;">Узнайте, сколько вы можете сэкономить</h2>',
        unsafe_allow_html=True)
    st.markdown(
        '<p style="color: #64748B; font-size: 1.1rem; margin-bottom: 40px;">Введите ваш номер телефона. Мы сами запросим детализацию из базы оператора.</p>',
        unsafe_allow_html=True)

    phone = st.text_input("Номер телефона", placeholder="+996 555 000 001", label_visibility="collapsed")
    st.write("")

    if st.button("Проанализировать тарифы", type="primary", use_container_width=True):
        if not phone or len(phone) < 9:
            st.error("Пожалуйста, введите корректный номер телефона.")
        else:
            # Ищем абонента по номеру ДО запуска анимации (чтобы не крутить спиннер зря)
            subscriber_id = get_subscriber_id_by_phone(phone)

            if not subscriber_id:
                # Если номера нет в базе - показываем ошибку сразу
                st.error(
                    "Абонент с таким номером не найден в базе. Попробуйте один из тестовых номеров: +996555000001 ... +996555000010")
            else:
                # Если абонент найден - запускаем красивую анимацию
                with st.status("Анализируем ваш номер...", expanded=True) as status:
                    st.write("🔌 Подключаемся к базе оператора...")
                    time.sleep(1)
                    st.write("📊 Загружаем детализацию за 3 месяца...")
                    time.sleep(1)
                    st.write("🧠 Нейросеть подбирает лучший вариант...")

                    status.update(label="Анализ завершен!", state="complete", expanded=False)

                # Сохраняем данные и переходим
                st.session_state['phone'] = phone
                st.session_state['subscriber_id'] = subscriber_id
                st.switch_page("pages/2_Результаты.py")

    st.markdown(
        '<div style="color: #64748B; font-size: 0.8rem; margin-top: 20px;">🔒 Мы не сохраняем ваши данные. Это демо-версия для хакатона.</div>',
        unsafe_allow_html=True)

with col_right:
    st.image("assets/db_phone.png", use_container_width=True)