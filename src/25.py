from typing import TypedDict, List, Dict
from datetime import datetime
from collections import defaultdict
from pprint import pprint


class Post(TypedDict):
    user_id: int
    content: str
    created_at: str


posts: List[Post] = [
    {"user_id": 1, "content": "はじめての投稿！", "created_at": "2024-05-01T10:00:00"},
    {
        "user_id": 2,
        "content": "おはようございます",
        "created_at": "2024-05-03T08:15:00",
    },
    {"user_id": 1, "content": "今日のランチ", "created_at": "2024-05-15T12:45:00"},
    {"user_id": 3, "content": "旅行に行きました", "created_at": "2024-06-01T18:20:00"},
    {"user_id": 2, "content": "仕事が終わった〜", "created_at": "2024-06-02T21:00:00"},
    {"user_id": 1, "content": "Pythonたのしい", "created_at": "2024-06-03T09:05:00"},
]


def analysisPosts(posts: List[Post]) -> Dict[int, Dict[str, int]]:
    result: Dict[int, Dict[str, int]] = defaultdict(lambda: defaultdict(int))
    for p in posts:
        result[p["user_id"]][
            datetime.fromisoformat(p["created_at"]).strftime("%Y-%m")
        ] += 1
    return {k: dict(v) for k, v in result.items()}


pprint(analysisPosts(posts))
