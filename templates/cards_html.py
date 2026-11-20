# templates/cards_html.py

def get_recommended_tariff_html(name, price, minutes, gb, sms):
    # ... (оставляем без изменений, если не нужна анимация на главной)
    pass

def get_tariff_plan_html(border, badge, name, price, minutes, gb, sms, overage):
    return (
        # ДОБАВЛЕН class="tariff-card"
        f'<div class="tariff-card" style="background: #FFFFFF; border: {border}; border-radius: 18px; padding: 24px; box-shadow: 0 4px 12px rgba(0,0,0,0.03); position: relative; height: 100%; margin-top: 10px; transition: all 0.2s ease-in-out;">'
        f'{badge}'
        f'<h3 style="color: #252044; margin-top: 0; margin-bottom: 8px; font-size: 1.3rem; font-weight: 700;">{name}</h3>'
        f'<div style="font-size: 1.8rem; font-weight: 800; color: #5B3FD0; margin-bottom: 16px;">{price:.0f} сом <span style="font-size: 0.9rem; color: #6E688F;">/ мес.</span></div>'
        f'<div style="color: #444; font-size: 0.95rem; line-height: 2;">'
        f'<span style="color: #7452D6;">✓</span> <b>{minutes}</b> минут<br>'
        f'<span style="color: #7452D6;">✓</span> <b>{gb}</b> ГБ<br>'
        f'<span style="color: #7452D6;">✓</span> <b>{sms}</b> SMS'
        f'</div>'
        f'<div style="margin-top: 20px; color: #6E688F; font-size: 0.8rem; border-top: 1px solid #F0F0F0; padding-top: 16px;">Перерасход: {overage}</div>'
        f'</div>'
    )