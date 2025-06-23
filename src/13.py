from typing import TypedDict, List, Dict
from collections import defaultdict


class Sale(TypedDict):
    department: str
    amount: int


sales_data: List[Sale] = [
    {"department": "営業", "amount": 500000},
    {"department": "マーケティング", "amount": 230000},
    {"department": "営業", "amount": 800000},
    {"department": "開発", "amount": 400000},
    {"department": "営業", "amount": 300000},
    {"department": "開発", "amount": 600000},
]


def analyze_sales(sales: List[Sale]) -> Dict[str, int]:
    totals: Dict[str, int] = defaultdict(int)

    for sale in sales:
        totals[sale["department"]] += sale["amount"]
    return totals


def sorted_totals(totals: Dict[str, int]) -> List[tuple[str, int]]:
    return sorted(totals.items(), key=lambda x: x[0], reverse=False)


hoge = analyze_sales(sales_data)
fuga = sorted_totals(hoge)
for i, (dept, amount) in enumerate(fuga):
    print(f"{i + 1}. {dept} / {amount}")
