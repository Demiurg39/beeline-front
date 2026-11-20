import streamlit as st
from components.styles import inject_css
from components.header import render_header
from components.cards import UICards
from components.charts import UICharts

st.set_page_config(page_title="Результаты — Tariffly", layout="wide")
inject_css()
render_header("home")

# Проверка, есть ли данные
if 'result' not in st.session_state:
    st.warning("Сначала введите номер телефона.")
    if st.button("Перейти к вводу"): st.switch_page("pages/1_Загрузка.py")
    st.stop()

result = st.session_state['result']

# Зеленая плашка сверху
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


# Модальное окно для кнопки "Подробнее"
@st.dialog("Детали тарифа")
def show_tariff_details():
    st.write(f"**{result.recommended_tariff}** — это оптимальный выбор для вас.")
    st.markdown("""
    - **Абонплата:** 550 сом/мес.
    - **Интернет:** 20 ГБ
    - **Звонки:** 1000 минут
    - **SMS:** 200 сообщений
    - **Особенности:** Ночной безлимит (01:00 - 07:00)
    """)
    if st.button("Выбрать этот тариф", type="primary", use_container_width=True):
        st.success("Заявка на подключение отправлена!")


# --- ОСНОВНАЯ СЕТКА (2 КОЛОНКИ) ---
col_left, col_right = st.columns([1, 1.1], gap="large")

with col_left:
    # Рисуем ОДНУ рекомендуемую карточку
    UICards.render_recommended_tariff(result.recommended_tariff, result.new_cost)
    st.write("")
    if st.button("Подробнее о тарифе →", use_container_width=True, type="primary"):
        show_tariff_details()

with col_right:
    # Если экономии нет, показываем инфо-блок
    if result.savings <= 0:
        st.info("💡 Ваш текущий тариф уже оптимален. Переход на другие тарифы не окупится.")
        current_color = "#1E8E4E"
    else:
        current_color = "#252044"

    m1, m2 = st.columns(2)
    with m1:
        st.markdown(f'''
        <div style="background: white; border: 1px solid #E8E1FB; border-radius: 16px; padding: 20px;">
            <div style="color: #6E688F; font-size: 0.85rem; font-weight: 600; margin-bottom: 8px;">Текущие расходы</div>
            <div style="color: {current_color}; font-size: 1.8rem; font-weight: 800; margin-bottom: 4px;">{result.current_cost:.0f} сом</div>
            <div style="color: #6E688F; font-size: 0.75rem;">в среднем за месяц</div>
        </div>
        ''', unsafe_allow_html=True)
    with m2:
        new_color = "#1E8E4E" if result.savings > 0 else "#252044"
        st.markdown(f'''
        <div style="background: {'#F4FCF7' if result.savings > 0 else 'white'}; border: 1px solid {'#BFE6CD' if result.savings > 0 else '#E8E1FB'}; border-radius: 16px; padding: 20px;">
            <div style="color: {new_color}; font-size: 0.85rem; font-weight: 600; margin-bottom: 8px;">Новые расходы</div>
            <div style="color: {new_color}; font-size: 1.8rem; font-weight: 800; margin-bottom: 4px;">{result.new_cost:.0f} сом</div>
            <div style="color: {new_color}; font-size: 0.75rem; opacity: 0.7;">в среднем за месяц</div>
        </div>
        ''', unsafe_allow_html=True)

    st.write("")

    # Блок экономии
    if result.savings > 0:
        st.markdown(f'''
        <div style="background: #E8F7EE; border: 1px solid #BFE6CD; border-radius: 16px; padding: 24px;">
            <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 12px;">
                <div style="font-size: 1.5rem;">📉</div>
                <div style="color: #1E8E4E; font-weight: 700; font-size: 1.1rem;">Ваша потенциальная экономия</div>
            </div>
            <div style="color: #1E8E4E; font-size: 2.5rem; font-weight: 800; line-height: 1; margin-bottom: 8px;">{result.savings:.0f} сом <span style="font-size: 1rem;">/ месяц</span></div>
            <div style="color: #1E8E4E; font-size: 0.8rem; opacity: 0.8;">{result.savings * 3:.0f} сом за три месяца (с учётом 50 сом за смену тарифа)</div>
        </div>
        ''', unsafe_allow_html=True)

st.write("---")

# --- БЛОК С ГРАФИКОМ ---
st.subheader("Сравнение стоимости тарифов")
UICharts.render_comparison_chart(result.tariffs_comparison, result.recommended_tariff)

st.write("---")

# --- БЛОК ОТ LLM ---
img_ai = ""
try:
    from components.image_utils import get_image_base64

    img_ai = get_image_base64("assets/icon_ai.png")
except:
    pass

st.markdown(f'''
<div style="background: #FFFFFF; border: 1px solid #E8E1FB; border-radius: 18px; padding: 24px; box-shadow: 0 4px 12px rgba(0,0,0,0.03);">
    <div style="display: flex; align-items: center; gap: 16px; margin-bottom: 16px;">
        <img src="data:image/png;base64,{img_ai}" width="50" style="object-fit: contain;">
        <div style="font-weight: 800; color: #252044; font-size: 1.2rem;">Почему мы выбрали этот тариф?</div>
    </div>
    <div style="color: #444; font-size: 0.95rem; line-height: 1.6; background: #F7F5FF; padding: 16px; border-radius: 12px; border-left: 4px solid #7452D6;">
        {result.llm_explanation}
    </div>
    <div style="color: #A9A3D1; font-size: 0.7rem; margin-top: 12px; text-align: right;">Сгенерировано ИИ на основе вашей детализации</div>
</div>
''', unsafe_allow_html=True)