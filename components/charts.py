import plotly.graph_objects as go
import streamlit as st
from typing import List, Dict


# Импортируем модель, если она у вас есть, или используем обычный список
# from models.analysis_result import ConsumptionDetail

class UICharts:
    @staticmethod
    def render_cost_dynamics(monthly_costs: Dict[str, float], new_cost: float):
        """График динамики расходов (история + прогноз)."""
        month_names = {"01": "Янв", "02": "Фев", "03": "Мар", "04": "Апр", "05": "Май", "06": "Июн", "07": "Июл",
                       "08": "Авг", "09": "Сен", "10": "Окт", "11": "Ноя", "12": "Дек"}

        hist_months_raw = list(monthly_costs.keys())
        hist_months = [month_names.get(m.split("-")[1], m) for m in hist_months_raw]
        hist_costs = list(monthly_costs.values())

        future_months = ["Ноя", "Дек", "Янв"]
        future_costs = [new_cost] * 3

        all_months = hist_months + future_months
        current_line = hist_costs + [None] * 3
        forecast_line = [None] * (len(hist_costs) - 1) + [hist_costs[-1]] + future_costs

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=all_months, y=current_line, mode='lines+markers', name='Текущие расходы',
                                 line=dict(color='#94A3B8', width=2), marker=dict(size=6)))
        fig.add_trace(go.Scatter(x=all_months, y=forecast_line, mode='lines+markers', name='Прогноз на новом тарифе',
                                 line=dict(color='#6C38FF', width=2, dash='dash'),
                                 marker=dict(size=6, symbol='square')))

        fig.update_layout(
            plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
            yaxis=dict(showgrid=True, gridcolor='#F1F5F9', title="Расходы (сом)"),
            xaxis=dict(showgrid=False, type='category'), margin=dict(l=20, r=20, t=20, b=20), height=300,
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            hovermode="x unified"
        )
        st.plotly_chart(fig, use_container_width=True)

    @staticmethod
    def render_consumption(consumption: List):
        """График среднего потребления (Интернет и Минуты)."""
        c_months = [item.month for item in consumption]
        c_gb = [item.gb for item in consumption]
        c_minutes = [item.minutes for item in consumption]

        fig_cons = go.Figure()
        fig_cons.add_trace(go.Bar(x=c_months, y=c_gb, name='Интернет (ГБ)', marker_color='#6C38FF'))
        fig_cons.add_trace(go.Bar(x=c_months, y=c_minutes, name='Минуты', marker_color='#C4B5FD'))

        fig_cons.update_layout(
            barmode='group', plot_bgcolor="rgba(0,0,0,0)", paper_bgcolor="rgba(0,0,0,0)",
            yaxis=dict(showgrid=True, gridcolor='#F1F5F9'), xaxis=dict(showgrid=False),
            margin=dict(l=20, r=20, t=40, b=20), height=350,
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1),
            bargap=0.2, bargroupgap=0.05
        )
        st.plotly_chart(fig_cons, use_container_width=True)