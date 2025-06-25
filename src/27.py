from typing import TypedDict, List
from enum import Enum
from pprint import pprint


class Rank(str, Enum):
    BRONZE = "bronze"
    SILVER = "silver"
    GOLD = "gold"
    PLATINUM = "platinum"


class RawUser(TypedDict):
    id: int
    name: str
    rank: str


class User(TypedDict):
    id: int
    name: str
    rank: Rank


class UserWithBenefit(TypedDict):
    id: int
    name: str
    benefit: str


users: List[RawUser] = [
    {"id": 1, "name": "佐藤", "rank": "gold"},
    {"id": 2, "name": "田中", "rank": "silver"},
    {"id": 3, "name": "鈴木", "rank": "bronze"},
    {"id": 4, "name": "高橋", "rank": "platinum"},
    {"id": 5, "name": "伊藤", "rank": "silver"},
]


def convertUser(users: List[RawUser]) -> List[User]:
    return [{**u, "rank": Rank(u["rank"])} for u in users]


def assign_benefits(users: List[User]) -> List[UserWithBenefit]:
    result: List[UserWithBenefit] = []
    for u in users:
        rank = u["rank"]
        match rank:
            case Rank.BRONZE:
                benefit = "500円割引"
            case Rank.SILVER:
                benefit = "送料無料"
            case Rank.GOLD:
                benefit = "10%オフクーポン"
            case Rank.PLATINUM:
                benefit = "専属コンシェルジュ + 10%オフクーポン"
        result.append({"id": u["id"], "name": u["name"], "benefit": benefit})
    return result


converted = convertUser(users)


pprint(converted)
pprint(assign_benefits(converted))
