# templates/about_html.py

def get_hero_html(icon_hero_base64: str) -> str:
    return (
        '<div style="display: flex; align-items: center; justify-content: space-between; background: #FFFFFF; border-radius: 24px; padding: 40px; margin-bottom: 40px; box-shadow: 0 10px 30px -10px rgba(0,0,0,0.05);">'
        '<div style="flex: 1; padding-right: 40px;">'
        '<h1 style="color: #0F172A; font-size: 2.5rem; font-weight: 800; margin-bottom: 16px; line-height: 1.2;">О сервисе Tariffly</h1>'
        '<p style="color: #64748B; font-size: 1.1rem; line-height: 1.6; max-width: 500px;">'
        'Простой и удобный сервис для анализа мобильных тарифов в Кыргызстане. Помогаем находить лучшие условия и экономить ваши деньги.'
        '</p></div>'
        '<div style="flex: 0 0 300px; text-align: right;">'
        f'<img src="data:image/png;base64,{icon_hero_base64}" style="max-width: 100%; height: auto;" alt="Hero Image">'
        '</div></div>'
    )

def get_step_html(icon_check_base64: str, step_num: int, title: str, description: str) -> str:
    return (
        '<div style="text-align: center; padding: 20px;">'
        '<div style="background: #F3E8FF; width: 64px; height: 64px; border-radius: 50%; display: flex; align-items: center; justify-content: center; margin: 0 auto 16px;">'
        f'<img src="data:image/png;base64,{icon_check_base64}" style="width: 32px;">'
        '</div>'
        f'<h4 style="color: #0F172A; margin-bottom: 8px;">{step_num}. {title}</h4>'
        f'<p style="color: #64748B; font-size: 0.9rem;">{description}</p>'
        '</div>'
    )

def get_info_card_html(icon_base64: str, title: str, text: str) -> str:
    return (
        '<div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-radius: 16px; padding: 24px; display: flex; gap: 20px; align-items: flex-start; height: 100%;">'
        '<div style="background: #FFFFFF; padding: 12px; border-radius: 12px; box-shadow: 0 4px 6px rgba(0,0,0,0.05);">'
        f'<img src="data:image/png;base64,{icon_base64}" style="width: 32px;">'
        '</div>'
        '<div>'
        f'<h4 style="color: #0F172A; margin-bottom: 8px; margin-top: 0;">{title}</h4>'
        f'<p style="color: #64748B; font-size: 0.9rem; margin: 0; line-height: 1.5;">{text}</p>'
        '</div></div>'
    )