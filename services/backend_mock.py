import time
from typing import Optional, List, Dict


class TariffComparisonItem:
    def __init__(self, tariff_name, avg_monthly_cost, net_savings_3m, is_profitable):
        self.tariff_name = tariff_name
        self.avg_monthly_cost = avg_monthly_cost
        self.net_savings_3m = net_savings_3m
        self.is_profitable = is_profitable


class ConsumptionDetail:
    def __init__(self, month, minutes, gb, sms):
        self.month = month
        self.minutes = minutes
        self.gb = gb
        self.sms = sms


class RecommendationResult:
    def __init__(self, id, action, tariff_id, addon_ids, current_monthly_cost, new_monthly_cost, monthly_savings,
                 switch_fee, net_savings_3m, monthly_costs, consumption):
        self.id = id
        self.action = action
        self.tariff_id = tariff_id
        self.addon_ids = addon_ids
        self.current_monthly_cost = current_monthly_cost
        self.new_monthly_cost = new_monthly_cost
        self.monthly_savings = monthly_savings
        self.switch_fee = switch_fee
        self.net_savings_3m = net_savings_3m
        self.monthly_costs = monthly_costs
        self.consumption = consumption


class ApiRecommendationResponse:
    def __init__(self, recommendation: RecommendationResult, comparison: List[TariffComparisonItem],
                 llm_explanation: Optional[str] = None):
        self.recommendation = recommendation
        self.comparison = comparison
        self.llm_explanation = llm_explanation


# --- ФУНКЦИЯ-ЗАГЛУШКА ---
def get_mock_api_response(phone: str) -> ApiRecommendationResponse:
    time.sleep(1.5)

    # Сценарий 1: Выгодно сменить тариф (если в номере есть 555)
    if "555" in phone:
        rec = RecommendationResult(
            id=phone, action="change", tariff_id="comfort_plus",
            addon_ids=["addon_5gb"],
            current_monthly_cost=850.0, new_monthly_cost=550.0,
            monthly_savings=300.0, switch_fee=50.0, net_savings_3m=850.0,
            monthly_costs={"2026-08": 900.0, "2026-09": 850.0, "2026-10": 800.0},
            consumption=[
                ConsumptionDetail("Август", 450, 12.5, 20),
                ConsumptionDetail("Сентябрь", 400, 11.0, 15),
                ConsumptionDetail("Октябрь", 480, 13.0, 25),
            ]
        )
        comp = [
            TariffComparisonItem("Базовый", 1200.0, -1000.0, False),
            TariffComparisonItem("Комфорт", 750.0, 250.0, True),
            TariffComparisonItem("Комфорт+", 550.0, 850.0, True),
            TariffComparisonItem("Премиум", 950.0, -300.0, False),
            TariffComparisonItem("Максимум", 1500.0, -1500.0, False),
        ]
        llm_text = "Ваше среднее потребление интернета составляет 12 ГБ в месяц, а звонков — 450 минут. Тариф «Комфорт+» предоставляет достаточный пакет (20 ГБ и 1000 минут) с запасом. Текущий тариф невыгоден, так как у вас часто происходит перерасход минут."
        return ApiRecommendationResponse(rec, comp, llm_text)

    # Сценарий 2: Лучше остаться (Идеальный тариф)
    else:
        rec = RecommendationResult(
            id=phone, action="stay", tariff_id="basic",
            addon_ids=[],
            current_monthly_cost=400.0,
            new_monthly_cost=400.0,
            monthly_savings=0.0,
            switch_fee=0.0,
            net_savings_3m=0.0,
            monthly_costs={"2026-08": 400.0, "2026-09": 410.0, "2026-10": 390.0},  # <-- Вот эту строку мы пропустили!
            consumption=[
                ConsumptionDetail("Август", 100, 2.0, 5),
                ConsumptionDetail("Сентябрь", 120, 2.5, 8),
                ConsumptionDetail("Октябрь", 90, 1.8, 4),
            ]
        )
        comp = [
            TariffComparisonItem("Базовый", 400.0, 0.0, True),
            TariffComparisonItem("Комфорт", 650.0, -750.0, False),
            TariffComparisonItem("Комфорт+", 850.0, -1350.0, False),
            TariffComparisonItem("Премиум", 1200.0, -2400.0, False),
            TariffComparisonItem("Максимум", 1800.0, -4200.0, False),
        ]
        llm_text = "Ваше потребление очень низкое (менее 2 ГБ и 100 минут в месяц). Переход на другие тарифы потребует переплаты за неиспользуемые пакеты. Рекомендуем остаться на текущем тарифе."
        return ApiRecommendationResponse(rec, comp, llm_text)