import os
from typing import Dict


# def count_file_extensions(directory: str) -> Dict[str, int]:
#     result: Dict[str, int] = {}
#     for _, __, files in os.walk(directory):
#         for file in files:
#             __, ext = os.path.splitext(file)
#             ext = ext if ext else "no_ext"
#             result[ext] = result.get(ext, 0) + 1
#     return result
def count_file_extensions(directory: str) -> Dict[str, int]:
    result: Dict[str, int] = {}
    for _, __, files in os.walk(directory):
        for file in files:
            _, ext = os.path.splitext(file)
            ext = ext if ext else "no_ext"
            result[ext] = result.get(ext, 0) + 1
    return result


print(count_file_extensions("./src"))
