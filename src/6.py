import os
import json
import logging
from typing import TypedDict, Literal, List


class Job(TypedDict):
    title: str
    department: str


class User(TypedDict):
    name: str
    age: int
    score: int
    gender: Literal["male", "female"]
    job: Job


logging.basicConfig(level=logging.INFO, format="%(levelname)s:  %(message)s")


def load_users_safely(path: str) -> List[User]:
    if not os.path.exists(path):
        logging.warning(f"ファイルが見つかりませんでした: {path}")
        return []

    with open(path, encoding="utf-8") as f:
        try:
            users = json.load(f)
            if not users:
                logging.warning("ユーザーリストが空です")
            return users
        except json.JSONDecodeError:
            logging.error("JSONの読み込みに失敗しました")
            return []


if __name__ == "__main__":
    path = "src/data/users.json"
    users = load_users_safely(path)

    if users:
        logging.info(f"ユーザーの数: {len(users)}")
        for u in users:
            print(f"- {u['name']} ({u['job']['department']})")
    else:
        logging.info("ユーザーがいませんでした")
