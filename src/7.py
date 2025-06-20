from typing import TypedDict, List
import os, json, logging


class Product(TypedDict):
    id: int
    name: str
    price: float
    stock: int


logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")


def load_products(path: str) -> List[Product]:
    if not os.path.exists(path):
        logging.warning(f"ファイルが存在しません: {path}")
        return []

    with open(path, encoding="utf-8") as f:
        try:
            products = json.load(f)
            logging.info(f"{len(products)} 件の製品を読み込みました。")
            return products
        except json.JSONDecodeError:
            logging.error("JSONの読み込みに失敗しました。")
            return []


def save_products(path: str, products: List[Product]) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(products, f, ensure_ascii=False, indent=2)
        logging.info(f"{len(products)} 件の製品を保存しました。")


def logging_products(products: List[Product]) -> None:
    for p in products:
        print(f"{p['name']} (在庫： {p['stock']}台, 価格： {p['price']: .0f})")


def get_or_create_products(path: str) -> List[Product]:
    products = load_products(path)
    if products:
        return products

    initial: List[Product] = [
        {"id": 1, "name": "ノートPC", "price": 125000, "stock": 4},
        {"id": 2, "name": "ワイヤレスマウス", "price": 2800, "stock": 25},
        {"id": 3, "name": "モニター", "price": 32000, "stock": 8},
    ]
    save_products(path, initial)
    return initial


if __name__ == "__main__":
    path = "src/data/inventory.json"
    products = get_or_create_products(path)
    logging_products(products)
