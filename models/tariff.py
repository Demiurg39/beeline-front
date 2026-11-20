from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class Tariff:
    name: str
    price: float
    minutes: int
    gb: int
    sms: int
    overage_cost: str

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Tariff':
        return cls(
            name=data.get("name", "Без названия"),
            price=float(data.get("price", 0)),
            minutes=int(data.get("minutes", 0)),
            gb=int(data.get("gb", 0)),
            sms=int(data.get("sms", 0)),
            overage_cost=data.get("overage", "Не указана")
        )