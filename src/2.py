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


users: List[User] = [
    {
        "name": "涼太",
        "age": 28,
        "score": 88,
        "gender": "male",
        "job": {"title": "エンジニア", "department": "開発"},
    },
    {
        "name": "さき",
        "age": 24,
        "score": 92,
        "gender": "female",
        "job": {"title": "デザイナー", "department": "UI/UX"},
    },
    {
        "name": "しょうた",
        "age": 30,
        "score": 76,
        "gender": "male",
        "job": {"title": "マネージャー", "department": "営業"},
    },
    {
        "name": "みき",
        "age": 21,
        "score": 95,
        "gender": "female",
        "job": {"title": "エンジニア", "department": "AI"},
    },
    {
        "name": "あきら",
        "age": 27,
        "score": 64,
        "gender": "male",
        "job": {"title": "マーケター", "department": "広報"},
    },
]


# def female_users(users: List[User]) -> List[User]:
#     return [u for u in users if u["gender"] == "female"]


# def engineer_names(users: List[User]) -> List[str]:
#     return [u["name"] for u in users if u["job"]["title"] == "エンジニア"]


# def ai_department_average_score(users: List[User]) -> float:
#     ai_users = [u for u in users if u["job"]["department"] == "AI"]
#     total = sum(u["score"] for u in ai_users)
#     return total / len(ai_users) if ai_users else 0.0


# def count_by_department(users: List[User]) -> dict[str, int]:
#     counts: dict[str, int] = {}
#     for u in users:
#         dept = u["job"]["department"]
#         counts[dept] = counts.get(dept, 0) + 1
#     return counts


def female_users(users: List[User]) -> List[User]:
    return [u for u in users if u["gender"] == "female"]


def engineer_names(users: List[User]) -> List[User]:
    return [u for u in users if u["job"]["title"] == "エンジニア"]


def ai_department_average_score(users: List[User]) -> float:
    ai_users = [u for u in users if u["job"]["department"] == "AI"]
    total = sum(u["score"] for u in ai_users)
    return total / len(ai_users) if ai_users else 0.0


def count_by_department(users: List[User]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for u in users:
        dept = u["job"]["department"]
        counts[dept] = counts.get(dept, 0) + 1
    return counts


print("--- 女性ユーザー ---")
for u in female_users(users):
    print(f"{u['name']}さん（{u['job']['title']}）")

print("--- エンジニア一覧 ---")
print(engineer_names(users))

print("--- AI部門の平均スコア ---")
print(ai_department_average_score(users))

print("--- 部署ごとの人数 ---")
print(count_by_department(users))
