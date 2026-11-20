import streamlit as st

def render_header(active_page="home"):
    home_color = "#6C38FF" if active_page == "home" else "#64748B"
    tariffs_color = "#6C38FF" if active_page == "tariffs" else "#64748B"
    about_color = "#6C38FF" if active_page == "about" else "#64748B"

    html = f'<div style="background: white; padding: 12px 24px; border-bottom: 1px solid #E5E7EB; display: flex; justify-content: space-between; align-items: center; margin-bottom: 30px; border-radius: 0 0 12px 12px;"><div style="display: flex; align-items: center; gap: 10px;"><div style="display: flex; gap: 3px; align-items: flex-end; height: 20px;"><div style="width: 6px; height: 10px; background: #6C38FF; border-radius: 2px;"></div><div style="width: 6px; height: 15px; background: #8B5CF6; border-radius: 2px;"></div><div style="width: 6px; height: 20px; background: #4A20C8; border-radius: 2px;"></div></div><span style="font-size: 20px; font-weight: 800; color: #0F172A;">Tariffly</span></div><div style="display: flex; gap: 24px; font-size: 14px; font-weight: 500;"><a href="/" target="_self" style="color: {home_color}; text-decoration: none;">Главная</a><a href="Тарифы" target="_self" style="color: {tariffs_color}; text-decoration: none;">Тарифы</a><a href="О_сервисе" target="_self" style="color: {about_color}; text-decoration: none;">О сервисе</a></div></div>'

    st.markdown(html, unsafe_allow_html=True)