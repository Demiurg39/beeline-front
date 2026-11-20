import streamlit as st
from templates.cards_html import get_recommended_tariff_html, get_tariff_plan_html
from templates.banners_html import get_status_banner_html, get_optimal_banner_html
from templates.results_html import get_metrics_html, get_savings_block_html, get_llm_block_html


class UICards:
    # ==========================================
    # МЕТОДЫ ДЛЯ СТРАНИЦЫ "ТАРИФЫ"
    # ==========================================
    @staticmethod
    def render_tariff_plan_card(tariff, is_recommended=False):
        border = "2px solid #7452D6" if is_recommended else "1px solid #E8E1FB"
        badge = '<div style="position: absolute; top: -12px; left: 50%; transform: translateX(-50%); background-color: #7452D6; color: white; padding: 4px 16px; border-radius: 20px; font-size: 0.75rem; font-weight: 700; white-space: nowrap;">✓ Рекомендуем</div>' if is_recommended else ''

        html = get_tariff_plan_html(
            border, badge, tariff.name, tariff.price,
            tariff.minutes, tariff.gb, tariff.sms, tariff.overage_cost
        )
        st.markdown(html, unsafe_allow_html=True)

    # ==========================================
    # МЕТОДЫ ДЛЯ СТРАНИЦЫ "РЕЗУЛЬТАТЫ"
    # ==========================================
    @staticmethod
    def render_recommended_tariff(tariff_name: str, price: float, minutes: int = 1000, gb: int = 20, sms: int = 200):
        html = get_recommended_tariff_html(tariff_name, price, minutes, gb, sms)
        st.markdown(html, unsafe_allow_html=True)

    @staticmethod
    def render_status_banner():
        st.markdown(get_status_banner_html(), unsafe_allow_html=True)

    @staticmethod
    def render_optimal_banner(tariff_name: str):
        st.markdown(get_optimal_banner_html(tariff_name), unsafe_allow_html=True)

    @staticmethod
    def render_metrics(current_cost, new_cost, savings, net_savings_3m, switch_fee):
        m1, m2 = st.columns(2)
        with m1:
            st.markdown(
                f'<div style="background: white; border: 1px solid #E2E8F0; border-radius: 12px; padding: 20px;">'
                f'<div style="color: #64748B; font-size: 0.8rem; font-weight: 600; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Текущие расходы</div>'
                f'<div style="color: #0F172A; font-size: 1.8rem; font-weight: 700; margin-bottom: 4px;">{current_cost:.0f} сом</div>'
                f'<div style="color: #94A3B8; font-size: 0.75rem;">в среднем за месяц</div>'
                f'</div>',
                unsafe_allow_html=True)
        with m2:
            st.markdown(
                f'<div style="background: white; border: 1px solid #E2E8F0; border-radius: 12px; padding: 20px;">'
                f'<div style="color: #64748B; font-size: 0.8rem; font-weight: 600; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Новые расходы</div>'
                f'<div style="color: #0F172A; font-size: 1.8rem; font-weight: 700; margin-bottom: 4px;">{new_cost:.0f} сом</div>'
                f'<div style="color: #94A3B8; font-size: 0.75rem;">в среднем за месяц</div>'
                f'</div>',
                unsafe_allow_html=True)

        st.write("")

        st.markdown(
            f'<div style="background: #F0FDF4; border: 1px solid #DCFCE7; border-radius: 12px; padding: 24px;">'
            f'<div style="color: #166534; font-weight: 600; font-size: 0.9rem; margin-bottom: 8px;">Потенциальная экономия</div>'
            f'<div style="color: #166534; font-size: 2rem; font-weight: 800; line-height: 1; margin-bottom: 6px;">{savings:.0f} сом <span style="font-size: 1rem; font-weight: 500; opacity: 0.8;">/ месяц</span></div>'
            f'<div style="color: #166534; font-size: 0.8rem; opacity: 0.8;">{net_savings_3m:.0f} сом за три месяца (с учётом {switch_fee:.0f} сом за смену тарифа)</div>'
            f'</div>',
            unsafe_allow_html=True)

    @staticmethod
    def render_llm_explanation(llm_text: str, icon_base64: str = ""):
        st.markdown(get_llm_block_html(llm_text, icon_base64), unsafe_allow_html=True)