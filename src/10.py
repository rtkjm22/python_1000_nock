from typing import TypedDict, List


class Student(TypedDict):
    name: str
    subject: str
    score: int


def get_high_scores(students: List[Student], threshold: int) -> List[Student]:
    return sorted(
        [s for s in students if s["score"] >= threshold],
        key=lambda s: s["score"],
        reverse=True,
    )


if __name__ == "__main__":
    students: List[Student] = [
        {"name": "さくら", "subject": "数学", "score": 92},
        {"name": "たくみ", "subject": "英語", "score": 78},
        {"name": "あかね", "subject": "数学", "score": 85},
        {"name": "しょう", "subject": "英語", "score": 96},
        {"name": "まい", "subject": "理科", "score": 63},
    ]

    top_students = get_high_scores(students, threshold=80)
    for s in top_students:
        print(f"{s['name']} ({s['subject']} : {s['score']}点)")
