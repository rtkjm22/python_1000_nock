from typing import TypedDict, List


class Contact(TypedDict):
    name: str
    email: str


contacts: List[Contact] = [
    {"name": "佐藤", "email": "sato@example.com"},
    {"name": "田中", "email": "tanaka@example.org"},
    {"name": "鈴木", "email": "suzuki@example.com"},
    {"name": "高橋", "email": "takahashi@company.jp"},
    {"name": "伊藤", "email": "ito@example.com"},
]


def filter_by_domain(contacts: List[Contact], domain: str) -> List[Contact]:
    return [c for c in contacts if c["email"].split('@')[1] == domain]


print(filter_by_domain(contacts, "example.com"))
