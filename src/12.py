from typing import TypedDict, List, Dict
from collections import defaultdict


class Client(TypedDict):
    id: int
    name: str
    industry: str


class Transaction(TypedDict):
    client_id: int
    department: str
    amount: int
    is_priority: bool


def analyze_sales(transactions: List[Transaction], clients: List[Client]) -> None:
    client_map: Dict[int, Client] = {client["id"]: client for client in clients}

    client_sales: Dict[int, int] = defaultdict(int)

    department_industry_sales: Dict[str, Dict[str, int]] = defaultdict(
        lambda: defaultdict(int)
    )

    for tx in transactions:
        client = client_map.get(tx["client_id"])
        if not client:
            continue

        client_sales[tx["client_id"]] += tx["amount"]
        department_industry_sales[tx["department"]][client["industry"]] += tx["amount"]

    print("重要取引先 TOP 3（売上高順）")
    sorted_clients = sorted(client_sales.items(), key=lambda x: x[1], reverse=True)[:3]
    for i, (client_id, total) in enumerate(sorted_clients, 1):
        print(f"{i}. {client_map[client_id]['name']} (¥{total:,})")


if __name__ == "__main__":
    clients: List[Client] = [
        {"id": 1, "name": "テック株式会社", "industry": "IT"},
        {"id": 2, "name": "ヘルスケア合同", "industry": "医療"},
        {"id": 3, "name": "大和商事", "industry": "小売"},
        {"id": 4, "name": "トラベルズ", "industry": "観光"},
    ]

    transactions: List[Transaction] = [
        {"client_id": 1, "department": "営業", "amount": 500000, "is_priority": True},
        {
            "client_id": 2,
            "department": "マーケティング",
            "amount": 230000,
            "is_priority": False,
        },
        {"client_id": 1, "department": "営業", "amount": 800000, "is_priority": True},
        {"client_id": 3, "department": "営業", "amount": 300000, "is_priority": False},
        {"client_id": 2, "department": "営業", "amount": 450000, "is_priority": True},
        {
            "client_id": 4,
            "department": "マーケティング",
            "amount": 150000,
            "is_priority": False,
        },
        {"client_id": 3, "department": "営業", "amount": 120000, "is_priority": False},
    ]

    analyze_sales(transactions, clients)
