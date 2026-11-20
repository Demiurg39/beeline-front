import streamlit as st


def render_header(active_page="home"):
    home_color = "#7452D6" if active_page == "home" else "#252044"
    tariffs_color = "#7452D6" if active_page == "tariffs" else "#252044"
    about_color = "#7452D6" if active_page == "about" else "#252044"

    col1, col2, col3 = st.columns([2, 3, 1])

    with col1:
        st.markdown(
            '<div style="display: flex; align-items: center; gap: 10px;"><div style="display: flex; gap: 3px; align-items: flex-end; height: 24px;"><div style="width: 8px; height: 12px; background: #C9B8F5; border-radius: 2px;"></div><div style="width: 8px; height: 18px; background: #8C6CF0; border-radius: 2px;"></div><div style="width: 8px; height: 24px; background: #5B3FD0; border-radius: 2px;"></div></div><span style="font-size: 24px; font-weight: 800; color: #252044;">Tariffly</span></div>',
            unsafe_allow_html=True)

    with col2:
        # Используем st.page_link для надежности
        c1, c2, c3 = st.columns(3)
        with c1:
            st.page_link("app.py", label="Главная", icon=None)
        with c2:
            st.page_link("pages/3_Тарифы.py", label="Все тарифы", icon=None)
        with c3:
            st.page_link("pages/4_О_сервисе.py", label="О сервисе", icon=None)

    with col3:
        st.markdown(
            '<div style="text-align: right;"><button style="background: white; border: none; border-radius: 50%; width: 40px; height: 40px; box-shadow: 0 4px 12px rgba(0,0,0,0.05); cursor: pointer; color: #7452D6; font-size: 18px;">🌙</button></div>',
            unsafe_allow_html=True)