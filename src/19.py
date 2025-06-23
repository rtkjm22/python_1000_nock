from typing import TypedDict, List, Dict
from collections import defaultdict
from enum import Enum
from pprint import pprint

# AgeGroup = Literal["10s", "20s", "30s", "40s", "50s+"]


class AgeGroup(str, Enum):
    AGE_10S = "10s"
    AGE_20S = "20s"
    AGE_30S = "30s"
    AGE_40S = "40s"
    AGE_50S = "50s+"


class Category(str, Enum):
    BOOK = "book"
    ELECTRONICS = "electronics"
    FASHION = "fashion"


class RawPurchase(TypedDict):
    user_id: int
    age_group: str
    category: str
    amount: int


class Purchase(TypedDict):
    user_id: int
    age_group: AgeGroup
    category: Category
    amount: int


purchases: List[RawPurchase] = [
    {"user_id": 1, "age_group": "20s", "category": "book", "amount": 3000},
    {"user_id": 2, "age_group": "30s", "category": "electronics", "amount": 25000},
    {"user_id": 3, "age_group": "20s", "category": "fashion", "amount": 8000},
    {"user_id": 4, "age_group": "30s", "category": "book", "amount": 1200},
    {"user_id": 5, "age_group": "40s", "category": "electronics", "amount": 40000},
    {"user_id": 6, "age_group": "20s", "category": "book", "amount": 1500},
]


def convert(rows: List[RawPurchase]) -> List[Purchase]:
    return [
        {
            **r,
            "age_group": AgeGroup(r["age_group"]),
            "category": Category(r["category"]),
        }
        for r in rows
    ]


def aggregate_by_category_and_age(
    purchase: List[Purchase],
) -> Dict[Category, Dict[AgeGroup, int]]:
    result: Dict[Category, Dict[AgeGroup, int]] = defaultdict(lambda: defaultdict(int))
    for p in purchase:
        result[p["category"]][p["age_group"]] += p["amount"]
    return {k: dict(v) for k, v in result.items()}


pprint(aggregate_by_category_and_age(convert(purchases)))
