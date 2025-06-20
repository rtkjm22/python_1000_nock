from typing import TypedDict, List


class User(TypedDict):
    name: str
    age: int
    score: int


users: List[User] = [
    {"name": "涼太", "age": 28, "score": 88},
    {"name": "さき", "age": 24, "score": 92},
    {"name": "しょうた", "age": 30, "score": 76},
    {"name": "みき", "age": 21, "score": 95},
    {"name": "あきら", "age": 27, "score": 64},
]


def high_scores(users: List[User]) -> List[str]:
  return [user['name'] for user in users if user["score"] >= 80]