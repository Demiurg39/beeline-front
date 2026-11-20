# templates/banners_html.py

def get_status_banner_html() -> str:
    """Плашка 'Анализ завершен' для сценария смены тарифа."""
    return (
        '<div style="background: #F8FAFC; border-left: 4px solid #6C38FF; border-radius: 4px; padding: 16px 24px; margin-bottom: 24px;">'
        '<div style="display: flex; align-items: center; gap: 12px;">'
        '<div style="font-weight: 700; color: #0F172A; font-size: 1.05rem;">Анализ завершён</div>'
        '<div style="color: #64748B; font-size: 0.9rem;">Мы нашли для вас более выгодный вариант.</div>'
        '</div></div>'
    )

def get_optimal_banner_html(tariff_name: str) -> str:
    """Плашка 'У вас оптимальный тариф' для сценария 'stay'."""
    return (
        '<div style="background: #F8FAFC; border: 1px solid #E2E8F0; border-left: 4px solid #6C38FF; border-radius: 12px; padding: 24px 32px; margin-bottom: 30px;">'
        '<h2 style="color: #0F172A; font-weight: 700; margin-top: 0; margin-bottom: 8px; font-size: 1.5rem;">У вас оптимальный тариф</h2>'
        f'<p style="color: #64748B; font-size: 1rem; margin-bottom: 0;">'
        f'Мы проанализировали ваши расходы. Текущий тариф <b>«{tariff_name}»</b> уже является самым выгодным решением. Переход на другие тарифы приведет к лишним тратам.'
        '</p></div>'
    )