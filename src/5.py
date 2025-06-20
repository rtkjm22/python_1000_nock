import json
from typing import TypedDict, Literal, List
import os


class Job(TypedDict):
    title: str
    department: str


class User(TypedDict):
    name: str
    age: int
    score: int
    gender: Literal["male", "female"]
    job: Job


def load_users_from_json(path: str) -> List[User]:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def save_users_to_json(users: List[User], path: str) -> None:
    print(os.path.dirname(path), path)
    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        json.dump(users, f, ensure_ascii=False, indent=2)


def get_ai_engineers(users: List[User]) -> List[str]:
    return [
        user["name"]
        for user in users
        if user["job"]["department"] == "AI" and user["job"]["title"] == "エンジニア"
    ]


if __name__ == "__main__":
    users = load_users_from_json("src/data/users.json")

    print("--- AI部門のエンジニアたち ---")
    print(get_ai_engineers(users))

    print("--- ファイルに書き出すテスト ---")
    save_users_to_json(users, "src/data/output_users.json")
