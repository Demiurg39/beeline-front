# models/tariff.py
from dataclasses import dataclass
from typing import Dict, Any

@dataclass
class OverageRates:
    call: float
    data: float
    sms: float

@dataclass
class Tariff:
    id: str
    name: str
    fee: float
    minutes: int
    gb: int
    sms: int
    overage: OverageRates
    night_unlimited: bool

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Tariff':
        overage_data = data.get("overage", {})
        overage = OverageRates(
            call=float(overage_data.get("call", 0)),
            data=float(overage_data.get("data", 0)),
            sms=float(overage_data.get("sms", 0))
        )
        return cls(
            id=data["id"],
            name=data["name"],
            fee=float(data["fee"]),
            minutes=int(data["minutes"]),
            gb=int(data["gb"]),
            sms=int(data["sms"]),
            overage=overage,
            night_unlimited=bool(data["night_unlimited"])
        )

@dataclass
class Addon:
    id: str
    name: str
    fee: float
    minutes: int
    gb: int
    sms: int

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Addon':
        return cls(
            id=data["id"],
            name=data["name"],
            fee=float(data["fee"]),
            minutes=int(data["minutes"]),
            gb=int(data["gb"]),
            sms=int(data["sms"])
        )