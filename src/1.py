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


# def high_scores(users: List[User]) -> List[str]:
#     return [user["name"] for user in users if user["score"] >= 80]


# def average_age(users: List[User]) -> float:
#     total_age: int = sum(user["age"] for user in users)
#     return total_age / len(users)


# def youngest_user(users: List[User]) -> User:
#     return min(users, key=lambda u: u["age"])


# def sorted_by_score(users: List[User]) -> List[User]:
#     return sorted(users, key=lambda u: u["score"], reverse=True)


def high_scores(users: List[User]) -> List[str]:
    return [user["name"] for user in users if user["score"] >= 80]


def average_age(users: List[User]) -> float:
    total_age: int = sum(user["age"] for user in users)
    return total_age / len(users)


def youngest_user(users: List[User]) -> User:
    return min(users, key=lambda u: u["age"])


def sorted_by_score(users: List[User]) -> List[User]:
    return sorted(users, key=lambda u: u["score"], reverse=True)


print(high_scores(users))
print("---")
print(average_age(users))
print("---")
print(youngest_user(users))
print("---")
print(sorted_by_score(users))
