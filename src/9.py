from typing import List


class Item:
    def __init__(self, name: str, stock: int, price: int):
        self.name = name
        self.stock = stock
        self.price = price

    def is_in_stock(self) -> bool:
        return self.stock > 0

    def __str__(self) -> str:
        return f"{self.name} (在庫：{self.stock}台 / 価格：¥{self.price})"


class Inventory:
    def __init__(self):
        self.items: List[Item] = []

    def add_item(self, item: Item) -> None:
        self.items.append(item)
        # or self.items += [item]

    def show_items(self) -> None:
        for item in self.items:
            print(item)

    def total_value(self) -> int:
        return sum(item.price * item.stock for item in self.items if item.is_in_stock())


if __name__ == "__main__":
    inventory = Inventory()
    inventory.add_item(Item("ノートPC", stock=5, price=120000))
    inventory.add_item(Item("マウス", stock=0, price=1500))
    inventory.add_item(Item("キーボード", stock=12, price=3000))

    inventory.show_items()

    print("\n--- 在庫総額 ---")
    print(f"¥{inventory.total_value()}")
