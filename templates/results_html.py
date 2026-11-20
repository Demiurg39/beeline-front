# templates/results_html.py

def get_metrics_html(current_cost: float, new_cost: float, savings: float, net_savings_3m: float, switch_fee: float) -> str:
    """Возвращает HTML для двух карточек (Текущие/Новые расходы) и блока экономии."""
    return (
        # Карточка 1: Текущие
        '<div style="background: white; border: 1px solid #E2E8F0; border-radius: 12px; padding: 20px;">'
        '<div style="color: #64748B; font-size: 0.8rem; font-weight: 600; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Текущие расходы</div>'
        f'<div style="color: #0F172A; font-size: 1.8rem; font-weight: 700; margin-bottom: 4px;">{current_cost:.0f} сом</div>'
        '<div style="color: #94A3B8; font-size: 0.75rem;">в среднем за месяц</div>'
        '</div>'
        # Карточка 2: Новые
        '<div style="background: white; border: 1px solid #E2E8F0; border-radius: 12px; padding: 20px;">'
        '<div style="color: #64748B; font-size: 0.8rem; font-weight: 600; margin-bottom: 8px; text-transform: uppercase; letter-spacing: 0.5px;">Новые расходы</div>'
        f'<div style="color: #0F172A; font-size: 1.8rem; font-weight: 700; margin-bottom: 4px;">{new_cost:.0f} сом</div>'
        '<div style="color: #94A3B8; font-size: 0.75rem;">в среднем за месяц</div>'
        '</div>'
    )

def get_savings_block_html(savings: float, net_savings_3m: float, switch_fee: float) -> str:
    return (
        '<div style="background: #F0FDF4; border: 1px solid #DCFCE7; border-radius: 12px; padding: 24px;">'
        '<div style="color: #166534; font-weight: 600; font-size: 0.9rem; margin-bottom: 8px;">Потенциальная экономия</div>'
        f'<div style="color: #166534; font-size: 2rem; font-weight: 800; line-height: 1; margin-bottom: 6px;">{savings:.0f} сом <span style="font-size: 1rem; font-weight: 500; opacity: 0.8;">/ месяц</span></div>'
        f'<div style="color: #166534; font-size: 0.8rem; opacity: 0.8;">{net_savings_3m:.0f} сом за три месяца (с учётом {switch_fee:.0f} сом за смену тарифа)</div>'
        '</div>'
    )

def get_llm_block_html(llm_text: str, icon_base64: str = "") -> str:
    img_tag = f'<img src="data:image/png;base64,{icon_base64}" width="32" style="object-fit: contain; opacity: 0.8;">' if icon_base64 else ''
    return (
        '<div style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; padding: 24px;">'
        '<div style="display: flex; align-items: center; gap: 12px; margin-bottom: 16px;">'
        f'{img_tag}'
        '<div style="font-weight: 700; color: #0F172A; font-size: 1.1rem;">Почему мы так решили?</div>'
        '</div>'
        f'<div style="color: #334155; font-size: 0.95rem; line-height: 1.6; background: #F8FAFC; padding: 16px; border-radius: 8px;">{llm_text}</div>'
        '<div style="color: #94A3B8; font-size: 0.75rem; margin-top: 12px; text-align: right;">Сгенерировано ИИ на основе вашей детализации</div>'
        '</div>'
    )


def get_llm_block_html(llm_text: str, icon_base64: str = "") -> str:
    # Если иконка передана, создаем тег img, иначе оставляем пустоту
    img_tag = f'<img src="data:image/png;base64,{icon_base64}" width="32" style="object-fit: contain; opacity: 0.8;">' if icon_base64 else ''

    return (
        '<div style="background: #FFFFFF; border: 1px solid #E2E8F0; border-radius: 12px; padding: 24px;">'
        '<div style="display: flex; align-items: center; gap: 12px; margin-bottom: 16px;">'
        f'{img_tag}'
        '<div style="font-weight: 700; color: #0F172A; font-size: 1.1rem;">Почему мы так решили?</div>'
        '</div>'
        f'<div style="color: #334155; font-size: 0.95rem; line-height: 1.6; background: #F8FAFC; padding: 16px; border-radius: 8px;">{llm_text}</div>'
        '<div style="color: #94A3B8; font-size: 0.75rem; margin-top: 12px; text-align: right;">Сгенерировано ИИ на основе вашей детализации</div>'
        '</div>'
    )