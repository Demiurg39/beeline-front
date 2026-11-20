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

if error:
    st.error(f"Ошибка: {error}")
else:
    cols = st.columns(4, gap="medium")
    for idx, tariff in enumerate(tariffs):
        with cols[idx]:
            # Временно хардкодим, что Комфорт+ рекомендуемый (потом будем брать из результата)
            is_rec = (tariff.name == "Комфорт+")
            UICards.render_tariff_plan_card(tariff, is_recommended=is_rec)