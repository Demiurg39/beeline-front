import streamlit as st
import plotly.graph_objects as go
from typing import Dict

class UICharts:
    @staticmethod
    def render_comparison_chart(data: Dict[str, float], recommended_name: str):
        tariffs = list(data.keys())
        costs = list(data.values())
        colors = ['#7452D6' if t == recommended_name else '#D1C4F5' for t in tariffs]

        fig = go.Figure(data=[go.Bar(
            x=tariffs, y=costs, marker_color=colors,
            text=[f"{c:.0f}" for c in costs], textposition='auto'
        )])
        fig.update_layout(
            plot_bgcolor="rgba(0,0,0,0)",
            paper_bgcolor="rgba(0,0,0,0)",
            margin=dict(l=20, r=20, t=20, b=20),
            yaxis_title=None,  # Убираем подпись оси Y
            xaxis_title=None,  # Убираем подпись оси X
            yaxis=dict(showgrid=False, showticklabels=False),  # Убираем сетку и цифры по Y
            height=300
        )
        # Делаем столбцы скругленными
        fig.update_traces(marker_line_width=0, marker_cornerradius=8)