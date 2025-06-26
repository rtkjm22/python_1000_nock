from pathlib import Path
from typing import List, Dict

# def count_lines_by_file(directory: str, extensions: List[str]) -> Dict[str, int]:
#   result: Dict[str, int] = {}
#   for file in Path(directory).rglob('*'):
#     if file.is_file() and file.suffix in extensions:
#       with open(file, encoding="utf-8") as f:
#         line_count = sum(1 for _ in f)
#       result[file.name] = line_count
#   return result


def count_lines_by_file(directory: str, extensions: List[str]) -> Dict[str, int]:
    result: Dict[str, int] = {}
    for file in Path(directory).rglob("*"):
        if file.is_file() and file.suffix in extensions:
            with open(file, encoding="utf-8") as f:
                line_count = sum(1 for _ in f)
            result[file.name] = line_count
    return result


print(count_lines_by_file("./src", [".py"]))
