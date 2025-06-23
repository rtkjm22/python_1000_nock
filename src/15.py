from typing import TypedDict, List, Dict
from collections import defaultdict
from enum import Enum


class Status(str, Enum):
    PAID = "paid"
    PENDING = "pending"
    FAILED = "failed"


class RawPayment(TypedDict):
    user_id: int
    amount: float
    status: str


class Payment(TypedDict):
    user_id: int
    amount: float
    status: Status


payments: List[RawPayment] = [
    {"user_id": 1, "amount": 1200.0, "status": "paid"},
    {"user_id": 2, "amount": 500.0, "status": "failed"},
    {"user_id": 1, "amount": 800.0, "status": "paid"},
    {"user_id": 3, "amount": 300.0, "status": "paid"},
]


def convert(payments: List[RawPayment]) -> List[Payment]:
    return [
        {"user_id": p["user_id"], "amount": p["amount"], "status": Status(p["status"])}
        for p in payments
    ]


def analysis_payments(payments: List[Payment]) -> Dict[int, float]:
    result: Dict[int, float] = defaultdict(int)
    paid_payments = [p for p in payments if p["status"] == Status.PAID]
    for p in paid_payments:
        result[p["user_id"]] += p["amount"]
    return result


print(analysis_payments(convert(payments)))
