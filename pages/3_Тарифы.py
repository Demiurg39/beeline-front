import streamlit as st
from components.styles import inject_css
from components.header import render_header
from components.cards import UICards
from services.data_service import DataService

st.set_page_config(page_title="Все тарифы — Tariffly", layout="wide")
inject_css()
render_header("tariffs")

st.markdown('<h2 style="color: #252044; font-weight: 800; margin-bottom: 4px;">Все доступные тарифы</h2>',
            unsafe_allow_html=True)
st.markdown(
    '<p style="color: #6E688F; font-size: 1rem; margin-bottom: 24px;">Сравните условия и найдите подходящий вариант.</p>',
    unsafe_allow_html=True)

# Загружаем тарифы
tariffs, error_tariffs = DataService.load_tariffs()
# Загружаем доппакеты
addons, error_addons = DataService.load_addons()


# --- МОДАЛЬНОЕ ОКНО ---
@st.dialog("Детали тарифа")
def show_tariff_modal(tariff, is_rec):
    st.markdown(f"### {tariff.name}")
    st.markdown(f"**Абонплата:** {tariff.fee} сом / мес.")
    if is_rec:
        st.success("Этот тариф рекомендован специально для вас!")
    st.markdown("---")
    st.markdown(f"**Интернет:** {tariff.gb} ГБ")
    st.markdown(f"**Звонки:** {tariff.minutes} минут")
    st.markdown(f"**SMS:** {tariff.sms} шт.")
    st.markdown(f"**Ночной безлимит:** {'Да' if tariff.night_unlimited else 'Нет'}")
    st.markdown(
        f"**Перерасход:** Звонок: {tariff.overage.call} сом, Интернет: {tariff.overage.data} сом, SMS: {tariff.overage.sms} сом")
    st.write("")
    if st.button("Подключить этот тариф", use_container_width=True, type="primary", key=f"connect_{tariff.id}"):
        st.success(f"Заявка на подключение тарифа «{tariff.name}» отправлена!")


# ==========================================
# БЛОК ТАРИФОВ
# ==========================================
if error_tariffs:
    st.error(f"Ошибка загрузки тарифов: {error_tariffs}")
else:
    cols = st.columns(4, gap="medium")
    for idx, tariff in enumerate(tariffs):
        with cols[idx % 4]:  # Распределяем по 4 колонки
            # Временно хардкодим, что "Максимум" рекомендуемый
            is_rec = (tariff.id == "T05")

            # Передаем в метод рендеринга объект tariff и флаг
            UICards.render_tariff_plan_card(tariff, is_recommended=is_rec)

            st.write("")

            btn_type = "primary" if is_rec else "secondary"
            if st.button("Подробнее", key=f"btn_tariff_{tariff.id}", use_container_width=True, type=btn_type):
                show_tariff_modal(tariff, is_rec)

st.write("---")

# ==========================================
# БЛОК ДОП-УСЛУГ
# ==========================================
st.markdown('<h3 style="color: #252044; font-weight: 800; margin-bottom: 16px;">Дополнительные пакеты</h3>',
            unsafe_allow_html=True)

if error_addons:
    st.error(f"Ошибка загрузки доппакетов: {error_addons}")
else:
    # Для доп-услуг используем 3 колонки, так как их всего 3
    cols_addons = st.columns(3, gap="medium")
    for idx, addon in enumerate(addons):
        with cols_addons[idx]:
            UICards.render_addon_card(addon)
            st.write("")
            if st.button("Добавить к тарифу", key=f"btn_addon_{addon.id}", use_container_width=True):
                st.toast(f"Пакет «{addon.name}» добавлен в корзину!")