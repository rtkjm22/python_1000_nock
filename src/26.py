from typing import TypedDict, List, Dict
from collections import defaultdict


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


def count_movies_by_genre(
    movies: List[Movie], year_from: int, genres: List[str]
) -> Dict[str, int]:
    # filtered = [m for m in movies if m["year"] >= year_from and m["genre"] in genres]
    # result: Dict[str, int] = defaultdict(int)
    # for m in filtered:
    #     result[m["genre"]] += 1
    # return dict(result)
    return {
        genre: sum(1 for m in movies if m["year"] >= year_from and m["genre"] == genre)
        for genre in genres
    }


print(count_movies_by_genre(movies, 2010, ["Sci-Fi", "War"]))
