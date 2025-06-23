from typing import TypedDict, List, Dict
from collections import Counter


class Movie(TypedDict):
    title: str
    year: int
    genre: str


movies: List[Movie] = [
    {"title": "Inception", "year": 2010, "genre": "Sci-Fi"},
    {"title": "The Dark Knight", "year": 2008, "genre": "Action"},
    {"title": "Interstellar", "year": 2014, "genre": "Sci-Fi"},
    {"title": "The Prestige", "year": 2006, "genre": "Drama"},
    {"title": "Dunkirk", "year": 2017, "genre": "War"},
    {"title": "Tenet", "year": 2020, "genre": "Sci-Fi"},
    {"title": "Memento", "year": 2000, "genre": "Thriller"},
]


def analysis_movies(movies: List[Movie]) -> Dict[str, int]:
    # filtered = [m for m in movies if m["year"] >= 2010]
    # result: Dict[str, int] = defaultdict(int)
    # for m in filtered:
    #     result[m["genre"]] += 1
    # return dict(result)
    return dict(Counter(m["genre"] for m in movies if m["year"] >= 2010))


print(analysis_movies(movies))
