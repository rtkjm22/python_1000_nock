import csv
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


def load_users_from_csv(path: str) -> List[User]:
    with open(path, encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return [
            {
                "name": row["name"],
                "age": int(row["age"]),
                "score": int(row["score"]),
                "gender": row["gender"],  # type: ignore
                "job": {
                    "title": row["title"],
                    "department": row["department"],
                },
            }
            for row in reader
        ]


def top_scorer(users: List[User]) -> User:
    return max(users, key=lambda u: u["score"])

if __name__ == '__main__':
  users = load_users_from_csv('src/data/users.csv')
  print("--- 読み込み結果 ---")
  for user in users:
    print(user)
  
  print("--- トップスコア ---")
  print(top_scorer(users))














