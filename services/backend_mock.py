import time
from typing import Optional


class TariffComparisonItem:
    def __init__(self, tariff_name, avg_monthly_cost, is_profitable):
        self.tariff_name = tariff_name
        self.avg_monthly_cost = avg_monthly_cost
        self.is_profitable = is_profitable


class RecommendationResult:
    def __init__(self, id, action, tariff_id, current_monthly_cost, new_monthly_cost, monthly_savings, switch_fee,
                 net_savings_3m):
        self.id = id
        self.action = action
        self.tariff_id = tariff_id
        self.current_monthly_cost = current_monthly_cost
        self.new_monthly_cost = new_monthly_cost
        self.monthly_savings = monthly_savings
        self.switch_fee = switch_fee
        self.net_savings_3m = net_savings_3m


class ApiRecommendationResponse:
    def __init__(self, recommendation: RecommendationResult, comparison: list[TariffComparisonItem],
                 llm_explanation: Optional[str] = None):
        self.recommendation = recommendation
        self.comparison = comparison
        self.llm_explanation = llm_explanation


# --- ФУНКЦИЯ-ЗАГЛУШКА (как будто мы дернули бэкенд) ---
def get_mock_api_response(phone: str) -> ApiRecommendationResponse:
    time.sleep(2)  # Имитация задержки сети

    # Сценарий 1: Выгодно сменить тариф
    if "555" in phone:
        rec = RecommendationResult(
            id=phone, action="change", tariff_id="comfort_plus",
            current_monthly_cost=850.0, new_monthly_cost=550.0,
            monthly_savings=300.0, switch_fee=50.0, net_savings_3m=850.0
        )
        comp = [
            TariffComparisonItem("Базовый", 1200.0, False),
            TariffComparisonItem("Комфорт", 750.0, True),
            TariffComparisonItem("Комфорт+", 550.0, True),
            TariffComparisonItem("Премиум", 950.0, False),
            TariffComparisonItem("Максимум", 1500.0, False),
        ]
        llm_text = "Ваше среднее потребление интернета составляет 12 ГБ в месяц, а звонков — 450 минут. Тариф «Комфорт+» предоставляет достаточный пакет (20 ГБ и 1000 минут) с запасом. Текущий тариф невыгоден, так как у вас часто происходит перерасход минут, что съедает лишние 300 сомов в месяц."
        return ApiRecommendationResponse(rec, comp, llm_text)

    # Сценарий 2: Лучше остаться (как на твоем скриншоте)
    else:
        rec = RecommendationResult(
            id=phone, action="stay", tariff_id="basic",
            current_monthly_cost=400.0, new_monthly_cost=450.0,
            monthly_savings=-50.0, switch_fee=0.0, net_savings_3m=-150.0
        )
        comp = [
            TariffComparisonItem("Базовый", 400.0, True),
            TariffComparisonItem("Комфорт", 650.0, False),
            TariffComparisonItem("Комфорт+", 850.0, False),
            TariffComparisonItem("Премиум", 1200.0, False),
            TariffComparisonItem("Максимум", 1800.0, False),
        ]
        llm_text = "Ваше потребление очень низкое (менее 2 ГБ и 100 минут в месяц). Переход на другие тарифы потребует переплаты за неиспользуемые пакеты. Рекомендуем остаться на текущем тарифе."
        return ApiRecommendationResponse(rec, comp, llm_text)