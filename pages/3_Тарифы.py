import streamlit as st
from components.styles import inject_css
from components.header import render_header
from components.cards import UICards
from services.data_service import DataService

st.set_page_config(page_title="Все тарифы — Tariffly", layout="wide")
inject_css()
render_header("tariffs")

st.markdown('<h2 style="color: #252044; font-weight: 800; margin-bottom: 4px;">Все доступные тарифы</h2>', unsafe_allow_html=True)
st.markdown('<p style="color: #6E688F; font-size: 1rem; margin-bottom: 24px;">Сравните условия и найдите подходящий вариант.</p>', unsafe_allow_html=True)

tariffs, error = DataService.load_mock_tariffs()

@st.dialog("Детали тарифа")
def show_tariff_modal(tariff, is_rec):
    st.markdown(f"### {tariff.name}")
    st.markdown(f"**Цена:** {tariff.price} сом / мес.")
    if is_rec:
        st.success("Этот тариф рекомендован специально для вас!")
    st.markdown("---")
    st.markdown(f"**Интернет:** {tariff.gb} ГБ")
    st.markdown(f"**Звонки:** {tariff.minutes} минут")
    st.markdown(f"**SMS:** {tariff.sms} шт.")
    st.markdown(f"**Перерасход:** {tariff.overage_cost}")
    st.write("")
    if st.button("Подключить этот тариф", use_container_width=True, type="primary"):
        st.success(f"Заявка на подключение тарифа «{tariff.name}» отправлена!")

if error:
    st.error(f"Ошибка: {error}")
else:
    cols = st.columns(4, gap="medium")
    for idx, tariff in enumerate(tariffs):
        with cols[idx]:
            is_rec = (tariff.name == "Комфорт+")
            UICards.render_tariff_plan_card(tariff, is_recommended=is_rec)
            st.write("")
            btn_type = "primary" if is_rec else "secondary"
            # Используем idx для уникальности ключа
            if st.button("Подробнее", key=f"btn_{idx}", use_container_width=True, type=btn_type):
                show_tariff_modal(tariff, is_rec)