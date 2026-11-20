import streamlit as st
import plotly.graph_objects as go
from typing import Dict


class UICharts:
    @staticmethod
    def render_comparison_chart(data: Dict[str, float], recommended_name: str):
        tariffs = list(data.keys())
        costs = list(data.values())

        # Цвета: фиолетовый для рекомендуемого, светло-фиолетовый для остальных
        colors = []
        for name in tariffs:
            if name == recommended_name:
                colors.append('#6C38FF')  # Новый Primary
            else:
                colors.append('#D1C4F5')

        fig = go.Figure(data=[go.Bar(
            x=tariffs,
            y=costs,
            marker_color=colors,
            text=[f"{c:.0f} сом" for c in costs],
            textposition='auto',
            hovertemplate="<b>%{x}</b><br>Стоимость: %{y:.0f} сом/мес<extra></extra>"
        )])

        fig.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=20, r=20, t=40, b=20),
            yaxis=dict(showgrid=True, gridcolor='#F0F0F0', title="Стоимость за месяц (сом)"),
            xaxis=dict(showgrid=False, title="Название тарифа"),
            showlegend=False,
            height=350,
            bargap=0.4
        )

        # Белый текст для всех столбцов
        fig.update_traces(
            textfont=dict(color='#FFFFFF', size=12),
            marker_cornerradius=8
        )

        st.plotly_chart(fig, use_container_width=True)