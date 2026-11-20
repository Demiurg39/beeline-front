import streamlit as st
import plotly.graph_objects as go
from typing import Dict


class UICharts:
    @staticmethod
    def render_comparison_chart(data: Dict[str, float], recommended_name: str):
        tariffs = list(data.keys())
        costs = list(data.values())

        # Создаем список цветов для каждого столбца вручную, без сложных условий
        colors = []
        for name in tariffs:
            if name == recommended_name:
                colors.append('#7452D6')  # Темно-фиолетовый для рекомендуемого
            else:
                colors.append('#D1C4F5')  # Светло-фиолетовый для остальных

        fig = go.Figure(data=[go.Bar(
            x=tariffs,
            y=costs,
            marker_color=colors,
            text=[f"{c:.0f}" for c in costs],
            textposition='auto'
        )])

        fig.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=20, r=20, t=40, b=20),
            yaxis=dict(showgrid=False, showticklabels=False, zeroline=False),
            xaxis=dict(showgrid=False, tickfont=dict(color="#6E688F", size=14)),
            showlegend=False,
            height=350
        )

        # Делаем текст белым и скругляем углы
        fig.update_traces(
            textfont=dict(color='#FFFFFF'),
            marker_cornerradius=8
        )

        st.plotly_chart(fig, use_container_width=True)