from typing import TypedDict, List, Dict
from collections import defaultdict


class Article(TypedDict):
    id: int
    title: str
    tags: List[str]
    views: int


articles: List[Article] = [
    {"id": 1, "title": "Python入門", "tags": ["python", "beginner"], "views": 180},
    {"id": 2, "title": "DjangoでWeb開発", "tags": ["python", "django"], "views": 260},
    {"id": 3, "title": "Reactの基本", "tags": ["react", "frontend"], "views": 300},
    {
        "id": 4,
        "title": "TypeScript入門",
        "tags": ["typescript", "frontend"],
        "views": 240,
    },
    {"id": 5, "title": "VueでSPA", "tags": ["vue", "frontend"], "views": 150},
]


# def aggregate_views_by_tag(articles: List[Article]) -> Dict[str, int]:
#     tag_views: Dict[str, int] = defaultdict(int)
#     for a in articles:
#         for tag in a["tags"]:
#             tag_views[tag] += a["views"]
#     return tag_views
def aggregate_views_by_tag(articles: List[Article]) -> Dict[str, int]:
    tag_views: Dict[str, int] = defaultdict(int)
    for tag, views in ((tag, a["views"]) for a in articles for tag in a["tags"]):
        tag_views[tag] += views
    return tag_views


print(aggregate_views_by_tag(articles))
