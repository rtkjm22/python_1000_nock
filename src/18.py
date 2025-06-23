from typing import TypedDict, Dict, List
from enum import Enum
from collections import defaultdict


class Membership(str, Enum):
    SILVER = "silver"
    GOLD = "gold"
    PLATINUM = "platinum"


class RawCustomer(TypedDict):
    name: str
    membership: str
    total_spent: float


class Customer(TypedDict):
    name: str
    membership: Membership
    total_spent: float


customers: List[RawCustomer] = [
    {"name": "佐藤", "membership": "silver", "total_spent": 12000.0},
    {"name": "田中", "membership": "gold", "total_spent": 25000.0},
    {"name": "鈴木", "membership": "platinum", "total_spent": 52000.0},
    {"name": "高橋", "membership": "silver", "total_spent": 17000.0},
    {"name": "伊藤", "membership": "gold", "total_spent": 34000.0},
]


def convert(raws: List[RawCustomer]) -> List[Customer]:
    return [
        {
            "name": r["name"],
            "membership": Membership(r["membership"]),
            "total_spent": r["total_spent"],
        }
        for r in raws
    ]


def aggregate_spending_by_membership(
    customers: List[Customer],
) -> Dict[Membership, float]:
    result: Dict[Membership, float] = defaultdict(float)

    for c in customers:
        result[c["membership"]] += c["total_spent"]
    return result
  
def sort_spending(aggregated: Dict[Membership, float]) -> List[tuple[Membership, float]]:
  return sorted(aggregated.items(), key=lambda x : x[0], reverse=False)


aggregated = aggregate_spending_by_membership(convert(customers))
print(sort_spending(aggregated))

