import streamlit as st
from components.styles import inject_css
from components.header import render_header
from components.cards import UICards
from components.charts import UICharts # <--- ДОБАВИЛИ ИМПОРТ
from components.image_utils import get_image_base64
from services.backend_mock import get_mock_api_response

st.set_page_config(page_title="Результаты — Tariffly", layout="wide")
inject_css()
render_header("home")

if 'phone' not in st.session_state:
    st.warning("Сначала введите номер телефона.")
    if st.button("Перейти к вводу"): st.switch_page("pages/1_Загрузка.py")
    st.stop()

try:
    api_response = get_mock_api_response(st.session_state['phone'])
    rec = api_response.recommendation
except Exception as e:
    st.error(f"Не удалось загрузить данные: {e}")
    st.stop()

tariff_name_map = {"comfort_plus": "Комфорт+", "basic": "Базовый"}
tariff_display_name = tariff_name_map.get(rec.tariff_id, "Неизвестный тариф")

# ==========================================
# СЦЕНАРИЙ 1: ОСТАТЬСЯ
# ==========================================
if rec.action == "stay":
    UICards.render_optimal_banner(tariff_display_name)

    st.subheader("Ваше среднее потребление")
    col_chart, col_summary = st.columns([2, 1], gap="large")

    with col_chart:
        # Вызов графика из компонента
        UICharts.render_consumption(rec.consumption)

    with col_summary:
        st.markdown(
            f'<div style="background: white; border: 1px solid #E2E8F0; border-radius: 12px; padding: 20px; height: 100%;">'
            f'<div style="font-weight: 700; color: #0F172A; margin-bottom: 16px;">Текущий тариф</div>'
            f'<div style="font-size: 1.5rem; font-weight: 800; color: #6C38FF; margin-bottom: 8px;">{tariff_display_name}</div>'
            f'<div style="color: #64748B; font-size: 0.9rem; margin-bottom: 16px;">Оптимальный выбор для вашего профиля потребления.</div>'
            f'<div style="border-top: 1px solid #F1F5F9; padding-top: 16px;">'
            f'<div style="display: flex; justify-content: space-between; margin-bottom: 8px; font-size: 0.9rem;">'
            f'<span style="color: #64748B;">Интернет</span> <span style="font-weight: 600;">20 ГБ</span>'
            f'</div>'
            f'<div style="display: flex; justify-content: space-between; font-size: 0.9rem;">'
            f'<span style="color: #64748B;">Звонки</span> <span style="font-weight: 600;">1000 мин</span>'
            f'</div>'
            f'</div>'
            f'</div>',
            unsafe_allow_html=True)

# ==========================================
# СЦЕНАРИЙ 2: СМЕНИТЬ
# ==========================================
else:
    UICards.render_status_banner()

    @st.dialog("Детали тарифа")
    def show_tariff_details():
        st.write(f"**{tariff_display_name}** — это оптимальный выбор для вас.")
        st.markdown("- **Абонплата:** 550 сом/мес.\n- **Интернет:** 20 ГБ\n- **Звонки:** 1000 минут\n- **SMS:** 200 сообщений")
        if st.button("Выбрать этот тариф", type="primary", use_container_width=True):
            st.success("Заявка на подключение отправлена!")

    col_left, col_right = st.columns([1, 1.1], gap="large")

    with col_left:
        UICards.render_recommended_tariff(tariff_display_name, rec.new_monthly_cost)
        st.write("")
        if st.button("Подключить тариф", use_container_width=True, type="primary"):
            show_tariff_details()

    with col_right:
        UICards.render_metrics(
            current_cost=rec.current_monthly_cost,
            new_cost=rec.new_monthly_cost,
            savings=rec.monthly_savings,
            net_savings_3m=rec.net_savings_3m,
            switch_fee=rec.switch_fee
        )

    st.write("---")

    # --- ГРАФИК РАСХОДОВ ---
    st.subheader("Динамика ваших расходов")
    # Вызов графика из компонента
    UICharts.render_cost_dynamics(rec.monthly_costs, rec.new_monthly_cost)

    # --- ГРАФИК ПОТРЕБЛЕНИЯ ---
    st.write("---")
    st.subheader("Ваше среднее потребление")
    # Вызов графика из компонента
    UICharts.render_consumption(rec.consumption)

st.write("---")

# --- БЛОК ОТ LLM ---
img_ai = get_image_base64("assets/icon_ai.png") if 'get_image_base64' in globals() else ""
UICards.render_llm_explanation(api_response.llm_explanation, img_ai)