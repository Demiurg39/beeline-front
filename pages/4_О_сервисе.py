import streamlit as st
from components.styles import inject_css
from components.header import render_header
from components.image_utils import get_image_base64

st.set_page_config(page_title="О сервисе — Tariffly", layout="wide")
inject_css()
render_header("about")

# --- ХЕЛПЕР ДЛЯ ИКОНОК ---
def get_icon(name):
    try:
        return get_image_base64(f"assets/{name}.png")
    except:
        return ""

icon_hero = get_icon("hero_phone")
icon_check = get_icon("icon_check_circle")
icon_shield = get_icon("db_phone") # Используем как щит/защиту
icon_support = get_icon("icon_sms") # Используем для поддержки

# ==========================================
# HERO SECTION (Верхний баннер)
# ==========================================
st.markdown(f'''
<div style="display: flex; align-items: center; justify-content: space-between; background: #FFFFFF; border-radius: 24px; padding: 40px; margin-bottom: 40px; box-shadow: 0 10px 30px -10px rgba(0,0,0,0.05);">
    <div style="flex: 1; padding-right: 40px;">
        <h1 style="color: #0F172A; font-size: 2.5rem; font-weight: 800; margin-bottom: 16px; line-height: 1.2;">О сервисе Tariffly</h1>
        <p style="color: #64748B; font-size: 1.1rem; line-height: 1.6; max-width: 500px;">
            Простой и удобный сервис для анализа мобильных тарифов в Кыргызстане. Помогаем находить лучшие условия и экономить ваши деньги.
        </p>
    </div>
    <div style="flex: 0 0 300px; text-align: right;">
        <img src="data:image/png;base64,{icon_hero}" style="max-width: 100%; height: auto;" alt="Hero Image">
    </div>
</div>
''', unsafe_allow_html=True)


# ==========================================
# КАК ЭТО РАБОТАЕТ (Шаги)
# ==========================================
st.markdown('<h2 style="text-align: center; color: #0F172A; margin-bottom: 40px;">Как это работает?</h2>', unsafe_allow_html=True)

# Используем 3 колонки для шагов
col1, col2, col3 = st.columns(3)

step_style = "text-align: center; padding: 20px;"

with col1:
    st.markdown(f'''
    <div style="{step_style}">
        <div style="background: #F3E8FF; width: 64px; height: 64px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 16px;">
            <img src="data:image/png;base64,{icon_check}" style="width: 32px;">
        </div>
        <h4 style="color: #0F172A; margin-bottom: 8px;">1. Введите номер</h4>
        <p style="color: #64748B; font-size: 0.9rem;">Загрузите данные или введите номер телефона для начала анализа.</p>
    </div>
    ''', unsafe_allow_html=True)

with col2:
    st.markdown(f'''
    <div style="{step_style}">
        <div style="background: #F3E8FF; width: 64px; height: 64px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 16px;">
            <img src="data:image/png;base64,{icon_check}" style="width: 32px;">
        </div>
        <h4 style="color: #0F172A; margin-bottom: 8px;">2. Получите анализ</h4>
        <p style="color: #64748B; font-size: 0.9rem;">Мы сравним ваши расходы с актуальными тарифами операторов.</p>
    </div>
    ''', unsafe_allow_html=True)

with col3:
    st.markdown(f'''
    <div style="{step_style}">
        <div style="background: #F3E8FF; width: 64px; height: 64px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 16px;">
            <img src="data:image/png;base64,{icon_check}" style="width: 32px;">
        </div>
        <h4 style="color: #0F172A; margin-bottom: 8px;">3. Экономьте</h4>
        <p style="color: #64748B; font-size: 0.9rem;">Переходите на выгодный тариф и оставайтесь на связи без переплат.</p>
    </div>
    ''', unsafe_allow_html=True)

st.write("") # Отступ
st.write("")

# ==========================================
# БЛОКИ БЕЗОПАСНОСТЬ И ПОДДЕРЖКА
# ==========================================
col_sec, col_sup = st.columns(2)

with col_sec:
    st.markdown(f'''
    <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 16px; padding: 24px; display: flex; gap: 20px; align-items: flex-start; height: 100%;">
        <div style="background: #FFFFFF; padding: 12px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
            <img src="data:image/png;base64,{icon_shield}" style="width: 32px;">
        </div>
        <div>
            <h4 style="color: #0F172A; margin-bottom: 8px; margin-top: 0;">Ваши данные под защитой</h4>
            <p style="color: #64748B; font-size: 0.9rem; margin: 0; line-height: 1.5;">
                Мы не сохраняем ваши персональные данные и историю звонков. Вся информация используется только в момент расчета и сразу удаляется.
            </p>
        </div>
    </div>
    ''', unsafe_allow_html=True)

with col_sup:
    st.markdown(f'''
    <div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 16px; padding: 24px; display: flex; gap: 20px; align-items: flex-start; height: 100%;">
        <div style="background: #FFFFFF; padding: 12px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">
            <img src="data:image/png;base64,{icon_support}" style="width: 32px;">
        </div>
        <div>
            <h4 style="color: #0F172A; margin-bottom: 8px; margin-top: 0;">Есть вопросы?</h4>
            <p style="color: #64748B; font-size: 0.9rem; margin: 0; line-height: 1.5;">
                Это демонстрационная версия, созданная в рамках хакатона INAI. Если у вас есть вопросы, напишите нам.
            </p>
        </div>
    </div>
    ''', unsafe_allow_html=True)