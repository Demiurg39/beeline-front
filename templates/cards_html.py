# templates/cards_html.py

def get_recommended_tariff_html(name, price, minutes, gb, sms):
    return (
        '<div style="background: linear-gradient(180deg, #FFFFFF 0%, #F7F5FF 100%); border: 2px solid #7452D6; border-radius: 20px; padding: 28px; box-shadow: 0 8px 24px rgba(116,82,214,.15); position: relative;">'
        '<div style="display: flex; justify-content: space-between; align-items: flex-start;">'
        '<span style="background-color: #5B3FD0; color: white; padding: 6px 16px; border-radius: 20px; font-size: 0.8rem; font-weight: 700; text-transform: uppercase;">✓ Рекомендуем</span>'
        '<span style="font-size: 24px; color: #7452D6;">👑</span>'
        '</div>'
        f'<h1 style="color: #252044; margin-top: 16px; margin-bottom: 4px; font-size: 2.2rem; font-weight: 800;">{name}</h1>'
        f'<h2 style="color: #7452D6; margin-top: 0; font-size: 2rem; font-weight: 800;">{price:.0f} сом <span style="font-size: 1rem; color: #6E688F; font-weight: 600;">/ мес.</span></h2>'
        '<p style="color: #6E688F; font-size: 0.9rem; margin-bottom: 24px;">Оптимальный вариант с учётом вашего потребления.</p>'
        '<div style="display: flex; justify-content: space-between; align-items: center; border-top: 1px solid #E8E1FB; padding-top: 20px;">'
        f'<div style="text-align: center; flex: 1;"><div style="font-size: 1.2rem; margin-bottom: 4px;">📞</div><div style="font-weight: 800; color: #252044; font-size: 1.2rem;">{minutes}</div><div style="font-size: 0.7rem; color: #6E688F; text-transform: uppercase;">Минут</div></div>'
        '<div style="width: 1px; height: 40px; background: #E8E1FB;"></div>'
        f'<div style="text-align: center; flex: 1;"><div style="font-size: 1.2rem; margin-bottom: 4px;">🌐</div><div style="font-weight: 800; color: #252044; font-size: 1.2rem;">{gb} ГБ</div><div style="font-size: 0.7rem; color: #6E688F; text-transform: uppercase;">Интернета</div></div>'
        '<div style="width: 1px; height: 40px; background: #E8E1FB;"></div>'
        f'<div style="text-align: center; flex: 1;"><div style="font-size: 1.2rem; margin-bottom: 4px;">✉️</div><div style="font-weight: 800; color: #252044; font-size: 1.2rem;">{sms}</div><div style="font-size: 0.7rem; color: #6E688F; text-transform: uppercase;">SMS</div></div>'
        '</div></div>'
    )

def get_tariff_plan_html(border, badge, name, price, minutes, gb, sms, overage):
    return (
        f'<div style="background: #FFFFFF; border: {border}; border-radius: 18px; padding: 24px; box-shadow: 0 4px 12px rgba(0,0,0,0.03); position: relative; height: 100%; margin-top: 10px;">'
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