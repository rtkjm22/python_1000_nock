import unittest
from src.three import User, top_scorer
# from three import User, top_scorer, filter_by_department, get_young_user_names/
from typing import List 


class TestThree(unittest.TestCase):
    def setUp(self):
        self.users: List[User] = [
            {
                "name": "なお",
                "age": 23,
                "score": 81,
                "gender": "female",
                "job": {"title": "デザイナー", "department": "UI/UX"},
            },
            {
                "name": "たける",
                "age": 35,
                "score": 91,
                "gender": "male",
                "job": {"title": "エンジニア", "department": "AI"},
            },
            {
                "name": "みき",
                "age": 22,
                "score": 97,
                "gender": "female",
                "job": {"title": "エンジニア", "department": "AI"},
            },
        ]

    def test_top_scorer(self):
        result = top_scorer(self.users)
        self.assertEqual(result["name"], "みき")

