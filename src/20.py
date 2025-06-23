from typing import Dict, List
from collections import Counter

test_data: List[str] = [
    "apple",
    "banana",
    "apple",
    "orange",
    "banana",
    "apple",
    "orange",
    "banana",
    "banana",
]


def count_occurrences(items: List[str]) -> Dict[str, int]:
    return Counter(items)


print(count_occurrences(test_data))
