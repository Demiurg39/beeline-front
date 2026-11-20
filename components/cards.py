import streamlit as st
from templates.cards_html import get_recommended_tariff_html, get_tariff_plan_html


class UICards:
    @staticmethod
    def render_recommended_tariff(tariff_name: str, price: float, minutes: int = 1000, gb: int = 20, sms: int = 200):
        html = get_recommended_tariff_html(tariff_name, price, minutes, gb, sms)
        st.markdown(html, unsafe_allow_html=True)

    @staticmethod
    def render_tariff_plan_card(tariff, is_recommended=False):
        border = "2px solid #7452D6" if is_recommended else "1px solid #E8E1FB"
        badge = '<div style="position: absolute; top: -12px; left: 50%; transform: translateX(-50%); background-color: #7452D6; color: white; padding: 4px 16px; border-radius: 20px; font-size: 0.75rem; font-weight: 700; white-space: nowrap;">✓ Рекомендуем</div>' if is_recommended else ''

        html = get_tariff_plan_html(border, badge, tariff.name, tariff.price, tariff.minutes, tariff.gb, tariff.sms,
                                    tariff.overage_cost)
        st.markdown(html, unsafe_allow_html=True)
        st.write("")
        st.button("Подробнее", key=f"btn_{tariff.name}", use_container_width=True,
                  type="primary" if is_recommended else "secondary")