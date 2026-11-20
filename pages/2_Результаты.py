import streamlit as st
from components.styles import inject_css
from components.header import render_header
from components.cards import UICards
from components.charts import UICharts
from components.image_utils import get_image_base64
from services.backend_mock import get_mock_api_response  # <-- Импортируем наш новый мок

st.set_page_config(page_title="Результаты — Tariffly", layout="wide")
inject_css()
render_header("home")

if 'phone' not in st.session_state:
    st.warning("Сначала введите номер телефона.")
    if st.button("Перейти к вводу"): st.switch_page("pages/1_Загрузка.py")
    st.stop()

# Получаем данные от "бэкенда"
api_response = get_mock_api_response(st.session_state['phone'])
rec = api_response.recommendation
comp = api_response.comparison

# Красивое название тарифа для отображения
tariff_display_name = "Комфорт+" if rec.tariff_id == "comfort_plus" else "Базовый"

# --- ЗЕЛЕНАЯ ПЛАШКА ---
st.markdown(f"""
<div style="background: #E8F7EE; border: 1px solid #BFE6CD; border-radius: 14px; padding: 16px 24px; display: flex; justify-content: space-between; align-items: center; margin-bottom: 24px;">
    <div style="display: flex; align-items: center; gap: 16px;">
        <div style="background: #1E8E4E; color: white; border-radius: 50%; width: 24px; height: 24px; display: flex; align-items: center; justify-content: center; font-size: 14px;">✓</div>
        <div>
            <div style="font-weight: 800; color: #1E8E4E; font-size: 1.1rem;">Анализ для номера {st.session_state['phone']} готов!</div>
            <div style="color: #1E8E4E; font-size: 0.85rem; opacity: 0.8;">Мы проанализировали ваше потребление за последние три месяца.</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)


@st.dialog("Детали тарифа")
def show_tariff_details():
    st.write(f"**{tariff_display_name}** — это оптимальный выбор для вас.")
    st.markdown(
        "- **Абонплата:** 550 сом/мес.\n- **Интернет:** 20 ГБ\n- **Звонки:** 1000 минут\n- **SMS:** 200 сообщений")
    if st.button("Выбрать этот тариф", type="primary", use_container_width=True):
        st.success("Заявка на подключение отправлена!")


col_left, col_right = st.columns([1, 1.1], gap="large")

with col_left:
    UICards.render_recommended_tariff(tariff_display_name, rec.new_monthly_cost)
    st.write("")
    if st.button("Подробнее о тарифе →", use_container_width=True, type="primary"):
        show_tariff_details()

with col_right:
    if rec.action == "stay":
        st.info("💡 Ваш текущий тариф уже оптимален. Переход на другие тарифы не окупится.")
        current_color = "#1E8E4E"
    else:
        current_color = "#252044"

    m1, m2 = st.columns(2)
    with m1:
        st.markdown(
            f'<div style="background: white; border: 1px solid #E8E1FB; border-radius: 16px; padding: 20px;"><div style="color: #6E688F; font-size: 0.85rem; font-weight: 600; margin-bottom: 8px;">Текущие расходы</div><div style="color: {current_color}; font-size: 1.8rem; font-weight: 800; margin-bottom: 4px;">{rec.current_monthly_cost:.0f} сом</div><div style="color: #6E688F; font-size: 0.75rem;">в среднем за месяц</div></div>',
            unsafe_allow_html=True)
    with m2:
        new_color = "#1E8E4E" if rec.monthly_savings > 0 else "#252044"
        st.markdown(
            f'<div style="background: {"#F4FCF7" if rec.monthly_savings > 0 else "white"}; border: 1px solid {"#BFE6CD" if rec.monthly_savings > 0 else "#E8E1FB"}; border-radius: 16px; padding: 20px;"><div style="color: {new_color}; font-size: 0.85rem; font-weight: 600; margin-bottom: 8px;">Новые расходы</div><div style="color: {new_color}; font-size: 1.8rem; font-weight: 800; margin-bottom: 4px;">{rec.new_monthly_cost:.0f} сом</div><div style="color: {new_color}; font-size: 0.75rem; opacity: 0.7;">в среднем за месяц</div></div>',
            unsafe_allow_html=True)

    st.write("")

    if rec.monthly_savings > 0:
        st.markdown(
            f'<div style="background: #E8F7EE; border: 1px solid #BFE6CD; border-radius: 16px; padding: 24px;"><div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px;"><div style="font-size: 1.5rem;">📉</div><div style="color: #1E8E4E; font-weight: 700; font-size: 1.1rem;">Ваша потенциальная экономия</div></div><div style="color: #1E8E4E; font-size: 2.5rem; font-weight: 800; line-height: 1; margin-bottom: 8px;">{rec.monthly_savings:.0f} сом <span style="font-size: 1rem;">/ месяц</span></div><div style="color: #1E8E4E; font-size: 0.8rem; opacity: 0.8;">{rec.net_savings_3m:.0f} сом за три месяца (с учётом {rec.switch_fee:.0f} сом за смену тарифа)</div></div>',
            unsafe_allow_html=True)

st.write("---")
st.subheader("Сравнение стоимости тарифов")

# Адаптируем данные для нашего графика
chart_data = {item.tariff_name: item.avg_monthly_cost for item in comp}
UICharts.render_comparison_chart(chart_data, tariff_display_name)

st.write("---")

# --- БЛОК ОТ LLM ---
img_ai = get_image_base64("assets/icon_ai.png") if 'get_image_base64' in globals() else ""

st.markdown(
    f'<div style="background: #FFFFFF; border: 1px solid #E8E1FB; border-radius: 18px; padding: 24px; box-shadow: 0 4px 12px rgba(0,0,0,0.03);"><div style="display: flex; align-items: center; gap: 16px; margin-bottom: 16px;"><img src="data:image/png;base64,{img_ai}" width="50" style="object-fit: contain;"><div style="font-weight: 800; color: #252044; font-size: 1.2rem;">Почему мы выбрали этот тариф?</div></div><div style="color: #444; font-size: 0.95rem; line-height: 1.6; background: #F7F5FF; padding: 16px; border-radius: 12px; border-left: 4px solid #7452D6;">{api_response.llm_explanation}</div><div style="color: #A9A3D1; font-size: 0.7rem; margin-top: 12px; text-align: right;">Сгенерировано ИИ на основе вашей детализации</div></div>',
    unsafe_allow_html=True)