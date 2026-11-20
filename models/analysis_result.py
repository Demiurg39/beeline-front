from dataclasses import dataclass
from typing import Dict, Optional


@dataclass
class AnalysisResult:
    current_cost: float
    new_cost: float
    savings: float
    recommended_tariff: str
    tariffs_comparison: Dict[str, float]
    llm_explanation: Optional[str] = None  # Новое поле

    # Старый get_mock_data можно оставить или удалить, он нам больше не нужен