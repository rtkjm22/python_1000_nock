from typing import TypedDict, List, Dict
from collections import defaultdict
from pprint import pprint


class Article(TypedDict):
    id: int
    title: str
    category: str


articles: List[Article] = [
    {"id": 1, "title": "Python入門", "category": "tech/programming"},
    {"id": 2, "title": "Djangoチュートリアル", "category": "tech/programming"},
    {"id": 3, "title": "健康的な生活習慣", "category": "life/health"},
    {"id": 4, "title": "キャリア設計のコツ", "category": "life/career"},
    {"id": 5, "title": "JavaScriptの基礎", "category": "tech/programming"},
    {"id": 6, "title": "家事の自動化", "category": "life/home"},
    {"id": 7, "title": "React入門", "category": "tech/frontend"},
    {"id": 8, "title": "筋トレのすすめ", "category": "life/health"},
]


def aggregate_by_root_category(articles: List[Article]) -> Dict[str, int]:
    result: Dict[str, int] = defaultdict(int)
    for a in articles:
        result[a["category"].split("/")[0]] += 1
    return result


pprint(aggregate_by_root_category(articles))
