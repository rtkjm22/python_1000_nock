from typing import TypedDict, List


class Post(TypedDict):
    user_id: int
    content: str
    created_at: str  # ISO形式: "YYYY-MM-DDTHH:MM:SS"


posts: List[Post] = [
    {"user_id": 1, "content": "おはよう！", "created_at": "2024-05-01T08:00:00"},
    {"user_id": 1, "content": "今日もがんばろう", "created_at": "2024-05-02T09:00:00"},
    {"user_id": 1, "content": "疲れた〜", "created_at": "2024-06-01T18:00:00"},
    {"user_id": 2, "content": "ランチ最高", "created_at": "2024-05-10T12:00:00"},
    {"user_id": 3, "content": "こんにちは", "created_at": "2024-05-05T10:00:00"},
    {"user_id": 3, "content": "やったー！", "created_at": "2024-05-06T11:00:00"},
    {"user_id": 3, "content": "週末だ！", "created_at": "2024-06-07T10:30:00"},
    {"user_id": 3, "content": "おやすみ", "created_at": "2024-06-07T22:30:00"},
]
