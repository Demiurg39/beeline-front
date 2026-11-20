import streamlit as st
import plotly.graph_objects as go
from components.styles import inject_css
from components.header import render_header
from components.cards import UICards
from components.image_utils import get_image_base64
from services.backend_mock import get_mock_api_response

st.set_page_config(page_title="Результаты — Tariffly", layout="wide")
inject_css()
render_header("home")

if 'phone' not in st.session_state:
    st.warning("Сначала введите номер телефона.")
    if st.button("Перейти к вводу"): st.switch_page("pages/1_Загрузка.py")
    st.stop()

api_response = get_mock_api_response(st.session_state['phone'])
rec = api_response.recommendation

tariff_name_map = {"comfort_plus": "Комфорт+", "basic": "Базовый"}
tariff_display_name = tariff_name_map.get(rec.tariff_id, "Неизвестный тариф")


# Хелпер для иконок (если используете)
def get_icon(name):
    try:
        return get_image_base64(f"assets/icons/{name}.png")
    except:
        return ""


# ==========================================
# СЦЕНАРИЙ 1: ОСТАТЬСЯ НА ТЕКУЩЕМ ТАРИФЕ (ИДЕАЛЬНЫЙ ТАРИФ)
# ==========================================
if rec.action == "stay":
    # Делаем баннер более компактным и горизонтальным
    st.markdown(f'''
    <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-left: 4px solid #6C38FF; border-radius: 12px; padding: 24px 32px; margin-bottom: 30px;">
        <h2 style="color: #0F172A; font-weight: 700; margin-top: 0; margin-bottom: 8px; font-size: 1.5rem;">У вас оптимальный тариф</h2>
        <p style="color: #64748B; font-size: 1rem; margin-bottom: 0;">
            Мы проанализировали ваши расходы. Текущий тариф <b>«{tariff_display_name}»</b> уже является самым выгодным решением. Переход на другие тарифы приведет к лишним тратам.
        </p>
    </div>
    ''', unsafe_allow_html=True)

    # Разделяем график и текстовую сводку, чтобы график не был гигантским
    st.subheader("Ваше среднее потребление")

    col_chart, col_summary = st.columns([2, 1], gap="large")

    with col_chart:
        c_months = [item.month for item in rec.consumption]
        c_gb = [item.gb for item in rec.consumption]
        c_minutes = [item.minutes for item in rec.consumption]

        fig_cons = go.Figure()
        fig_cons.add_trace(go.Bar(x=c_months, y=c_gb, name='Интернет (ГБ)', marker_color='#6C38FF'))
        fig_cons.add_trace(go.Bar(x=c_months, y=c_minutes, name='Минуты', marker_color='#C4B5FD'))
        fig_cons.update_layout(
            barmode='group', plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
            yaxis=dict(showgrid=True, gridcolor='#F1F5F9'), xaxis=dict(showgrid=False),
            margin=dict(l=10, r=10, t=10, b=10), height=350,
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig_cons, use_container_width=True)

    with col_summary:
        # Добавляем текстовую карточку справа, чтобы заполнить пустоту
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
# СЦЕНАРИЙ 2: РЕКОМЕНДАЦИЯ СМЕНИТЬ ТАРИФ
# ==========================================
else:
    # --- СТАТУСНАЯ ПЛАШКА ---
    st.markdown(
        f'<div style="background: #F8FAFC; border-left: 4px solid #6C38FF; border-radius: 4px; padding: 16px 24px; margin-bottom: 24px;">'
        f'<div style="display: flex; align-items: center; gap: 12px;">'
        f'<div style="font-weight: 700; color: #0F172A; font-size: 1.05rem;">Анализ завершён</div>'
        f'<div style="color: #64748B; font-size: 0.9rem;">Мы нашли для вас более выгодный вариант.</div>'
        f'</div></div>',
        unsafe_allow_html=True)


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
        if st.button("Подключить тариф", use_container_width=True, type="primary"):
            show_tariff_details()

    with col_right:
        m1, m2 = st.columns(2)
        with m1:
            st.markdown(
                f'<div style="background: white; border: 1px solid #E2E8F0; border-radius: 12px; padding: 20px;">'
                f'<div style="color: #64748B; font-size: 0.8rem; font-weight: 600; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Текущие расходы</div>'
                f'<div style="color: #0F172A; font-size: 1.8rem; font-weight: 700; margin-bottom: 4px;">{rec.current_monthly_cost:.0f} сом</div>'
                f'<div style="color: #94A3B8; font-size: 0.75rem;">в среднем за месяц</div>'
                f'</div>',
                unsafe_allow_html=True)
        with m2:
            st.markdown(
                f'<div style="background: white; border: 1px solid #E2E8F0; border-radius: 12px; padding: 20px;">'
                f'<div style="color: #64748B; font-size: 0.8rem; font-weight: 600; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Новые расходы</div>'
                f'<div style="color: #0F172A; font-size: 1.8rem; font-weight: 700; margin-bottom: 4px;">{rec.new_monthly_cost:.0f} сом</div>'
                f'<div style="color: #94A3B8; font-size: 0.75rem;">в среднем за месяц</div>'
                f'</div>',
                unsafe_allow_html=True)

        st.write("")

        st.markdown(
            f'<div style="background: #F0FDF4; border: 1px solid #DCFCE7; border-radius: 12px; padding: 24px;">'
            f'<div style="color: #166534; font-weight: 600; font-size: 0.9rem; margin-bottom: 8px;">Потенциальная экономия</div>'
            f'<div style="color: #166534; font-size: 2rem; font-weight: 800; line-height: 1; margin-bottom: 6px;">{rec.monthly_savings:.0f} сом <span style="font-size: 1rem; font-weight: 500; opacity: 0.8;">/ месяц</span></div>'
            f'<div style="color: #166534; font-size: 0.8rem; opacity: 0.8;">{rec.net_savings_3m:.0f} сом за три месяца (с учётом {rec.switch_fee:.0f} сом за смену тарифа)</div>'
            f'</div>',
            unsafe_allow_html=True)

    st.write("---")

    # --- ГРАФИК РАСХОДОВ ---
    st.subheader("Динамика ваших расходов")

    month_names = {"01": "Янв", "02": "Фев", "03": "Мар", "04": "Апр", "05": "Май", "06": "Июн", "07": "Июл",
                   "08": "Авг", "09": "Сен", "10": "Окт", "11": "Ноя", "12": "Дек"}
    hist_months_raw = list(rec.monthly_costs.keys())
    hist_months = [month_names.get(m.split("-")[1], m) for m in hist_months_raw]
    hist_costs = list(rec.monthly_costs.values())

    future_months = ["Ноя", "Дек", "Янв"]
    future_costs = [rec.new_monthly_cost] * 3

    all_months = hist_months + future_months
    current_line = hist_costs + [None] * 3
    forecast_line = [None] * (len(hist_costs) - 1) + [hist_costs[-1]] + future_costs

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=all_months, y=current_line, mode='lines+markers', name='Текущие расходы',
                             line=dict(color='#94A3B8', width=2), marker=dict(size=6)))
    fig.add_trace(go.Scatter(x=all_months, y=forecast_line, mode='lines+markers', name='Прогноз на новом тарифе',
                             line=dict(color='#6C38FF', width=2, dash='dash'), marker=dict(size=6, symbol='square')))
    fig.update_layout(plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
                      yaxis=dict(showgrid=True, gridcolor='#F1F5F9', title="Расходы (сом)"),
                      xaxis=dict(showgrid=False, type='category'), margin=dict(l=20, r=20, t=20, b=20), height=300,
                      legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
                      hovermode="x unified")
    st.plotly_chart(fig, use_container_width=True)

    # --- ГРАФИК ПОТРЕБЛЕНИЯ ---
    st.write("---")
    st.subheader("Ваше среднее потребление")

    # Убираем col_chart_cons, чтобы график занял всю ширину и не «поплыл»
    c_months = [item.month for item in rec.consumption]
    c_gb = [item.gb for item in rec.consumption]
    c_minutes = [item.minutes for item in rec.consumption]

    fig_cons = go.Figure()
    fig_cons.add_trace(go.Bar(x=c_months, y=c_gb, name='Интернет (ГБ)', marker_color='#6C38FF'))
    fig_cons.add_trace(go.Bar(x=c_months, y=c_minutes, name='Минуты', marker_color='#C4B5FD'))

    fig_cons.update_layout(
        barmode='group',
        plot_bgcolor="rgba(0,0,0,0)",
        paper_bgcolor="rgba(0,0,0,0)",
        yaxis=dict(showgrid=True, gridcolor='#F1F5F9'),
        xaxis=dict(showgrid=False),
        margin=dict(l=20, r=20, t=40, b=20),  # Увеличили верхний отступ для легенды
        height=350,  # Чуть увеличили высоту для пропорциональности
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
        bargap=0.2,  # Расстояние между группами месяцев
        bargroupgap=0.05  # Расстояние между столбцами внутри группы
    )
    st.plotly_chart(fig_cons, use_container_width=True)

st.write("---")

# --- БЛОК ОТ LLM ---
img_ai = get_image_base64("assets/icon_ai.png") if 'get_image_base64' in globals() else ""
st.markdown(
    f'<div style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; padding: 24px;">'
    f'<div style="display: flex; align-items: center; gap: 12px; margin-bottom: 16px;">'
    f'<img src="data:image/png;base64,{img_ai}" width="32" style="object-fit: contain; opacity: 0.8;">'
    f'<div style="font-weight: 700; color: #0F172A; font-size: 1.1rem;">Почему мы так решили?</div>'
    f'</div>'
    f'<div style="color: #334155; font-size: 0.95rem; line-height: 1.6; background: #F8FAFC; padding: 16px; border-radius: 8px;">{api_response.llm_explanation}</div>'
    f'<div style="color: #94A3B8; font-size: 0.75rem; margin-top: 12px; text-align: right;">Сгенерировано ИИ на основе вашей детализации</div>'
    f'</div>',
    unsafe_allow_html=True)