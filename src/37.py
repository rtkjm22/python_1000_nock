from typing import List
from pathlib import Path


# def top_recent_files(directory: str, limit: int) -> List[str]:
#     files = sorted(
#         [file for file in Path(directory).rglob("*") if file.is_file()],
#         key=lambda x: x.stat().st_mtime,
#         reverse=True,
#     )

#     return [str(file) for file in files][:limit]

def top_recent_files(directory: str, limit: int) -> List[str]:
    file_stats = [
        (file, file.stat().st_mtime)
        for file in Path(directory).rglob("*")
        if file.is_file()
    ]
    print(file_stats)
    sorted_files = sorted(file_stats, key=lambda x: x[1], reverse=True)
    return [str(file) for file, _ in sorted_files[:limit]]


if __name__ == "__main__":
    print(top_recent_files("./src", 5))
