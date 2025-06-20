from typing import TypedDict, List, Literal


class Job(TypedDict):
    title: str
    department: str


class User(TypedDict):
    name: str
    age: int
    score: int
    job: Job
    gender: Literal["male", "female"]


def top_scorer(users: List[User]) -> User:
    return max(users, key=lambda u: u["score"])


def filter_by_department(users: List[User], department: str) -> List[User]:
    return [u for u in users if u["job"]["department"] == department]


def get_names(users: List[User]) -> List[str]:
    return [u["name"] for u in users]


def is_young(user: User) -> bool:
    return user["age"] <= 25
