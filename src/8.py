import json, os
from typing import List, TypedDict, cast


class Sale(TypedDict):
    id: int
    product: str
    amount: int
    category: str


def load_sales(path: str) -> List[Sale]:
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
        return cast(List[Sale], data)


def save_sales(path: str, sales: List[Sale]) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(sales, f, ensure_ascii=False, indent=2)

    # f = open(path, "w", encoding="utf-8")
    # try:
    #   json.dump(sales, f, ensure_ascii=False, indent=2)
    # finally:
    #   f.close()


def filter_high_value_sales(sales: List[Sale], threshold: int) -> List[Sale]:
    return [s for s in sales if s["amount"] >= threshold]


if __name__ == "__main__":
    src_path = "src/data/sales.json"
    dest_path = "src/data/high_value_sales.json"

    sales = load_sales(src_path)
    filtered = filter_high_value_sales(sales, threshold=10000)
    save_sales(dest_path, filtered)

    for s in filtered:
        print(f"{s["product"]} (売上：¥{s['amount']})")
