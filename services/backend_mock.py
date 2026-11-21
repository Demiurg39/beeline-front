import time
from typing import Optional, List, Dict
from services.api_client import ApiClient

# ==========================================
# МАППИНГ НОМЕРОВ
# ==========================================
PHONE_TO_SUBSCRIBER_MAP = {
    "+996555000001": "P01", "+996555000002": "P02", "+996555000003": "P03",
    "+996555000004": "P04", "+996555000005": "P05", "+996555000006": "P06",
    "+996555000007": "P07", "+996555000008": "P08", "+996555000009": "P09",
    "+996555000010": "P10",
}


def get_subscriber_id_by_phone(phone: str) -> Optional[str]:
    clean_phone = phone.replace(" ", "")
    return PHONE_TO_SUBSCRIBER_MAP.get(clean_phone)


# ==========================================
# КЛАССЫ ДЛЯ МОК-ДАННЫХ
# ==========================================
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


# ==========================================
# ГЛАВНАЯ ЛОГИКА (API или МОК)
# ==========================================
USE_REAL_API = True  # Флаг: True = пробуем API, False = только моки


def get_mock_api_response(phone: str) -> ApiRecommendationResponse:
    """Пытается получить данные с реального API. Если не выходит — отдает мок."""
    subscriber_id = get_subscriber_id_by_phone(phone)

    if USE_REAL_API and subscriber_id:
        try:
            api_data = ApiClient.recommend_by_subscriber(subscriber_id)
            return _parse_api_response(api_data)
        except (ConnectionError, ValueError, TimeoutError) as e:
            print(f"[WARNING] API недоступен ({e}). Используем мок-данные.")
            return _get_fallback_mock(phone)

    return _get_fallback_mock(phone)


def _parse_api_response(api_data: dict) -> ApiRecommendationResponse:
    """Преобразует JSON от API в наши внутренние классы."""
    rec_data = api_data["recommendation"]

    consumption = []
    for item in rec_data.get("consumption_on_recommended_tariff", []):
        usage = item["billable_usage"]

        # Временная заглушка: если бэкенд вернул нули, подставляем моковые данные
        minutes = usage["call"] if usage["call"] > 0 else 150
        gb = usage["data"] if usage["data"] > 0 else 5.0
        sms = usage["sms"] if usage["sms"] > 0 else 10

        consumption.append(ConsumptionDetail(
            item["month"], int(minutes), gb, int(sms)
        ))

    rec = RecommendationResult(
        id=rec_data["id"], action=rec_data["action"], tariff_id=rec_data["tariff_id"],
        addon_ids=rec_data["addon_ids"], current_monthly_cost=rec_data["current_monthly_cost"],
        new_monthly_cost=rec_data["new_monthly_cost"], monthly_savings=rec_data["monthly_savings"],
        switch_fee=rec_data["switch_fee"], net_savings_3m=rec_data["net_savings_3m"],
        monthly_costs=rec_data["monthly_costs"], consumption=consumption
    )

    comp = [
        TariffComparisonItem(
            item["tariff_name"], item["avg_monthly_cost"], item["net_savings_3m"], item["is_profitable"]
        ) for item in api_data["comparison"]
    ]

    print("=== ОТВЕТ ОТ API ===")
    print(api_data)
    print("====================")

    return ApiRecommendationResponse(rec, comp, api_data.get("llm_explanation"))


def _get_fallback_mock(phone: str) -> ApiRecommendationResponse:
    """Ваши старые моки (работают, если API выключен)."""
    time.sleep(1.5)
    if "555" in phone:
        rec = RecommendationResult(
            id=phone, action="change", tariff_id="T03", addon_ids=["A01"],
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
            TariffComparisonItem("Старт", 1200.0, -1000.0, False),
            TariffComparisonItem("Комфорт", 750.0, 250.0, True),
            TariffComparisonItem("Онлайн", 550.0, 850.0, True),
        ]
        llm_text = "Ваше среднее потребление интернета составляет 12 ГБ в месяц, а звонков — 450 минут. Тариф «Онлайн» предоставляет достаточный пакет (20 ГБ и 100 минут) с запасом."
        return ApiRecommendationResponse(rec, comp, llm_text)
    else:
        rec = RecommendationResult(
            id=phone, action="stay", tariff_id="T01", addon_ids=[],
            current_monthly_cost=400.0, new_monthly_cost=400.0,
            monthly_savings=0.0, switch_fee=0.0, net_savings_3m=0.0,
            monthly_costs={"2026-08": 400.0, "2026-09": 410.0, "2026-10": 390.0},
            consumption=[
                ConsumptionDetail("Август", 100, 2.0, 5),
                ConsumptionDetail("Сентябрь", 120, 2.5, 8),
                ConsumptionDetail("Октябрь", 90, 1.8, 4),
            ]
        )
        comp = [
            TariffComparisonItem("Старт", 400.0, 0.0, True),
            TariffComparisonItem("Комфорт", 650.0, -750.0, False),
        ]
        llm_text = "Ваше потребление очень низкое. Переход на другие тарифы потребует переплаты. Рекомендуем остаться на текущем тарифе."
        return ApiRecommendationResponse(rec, comp, llm_text)