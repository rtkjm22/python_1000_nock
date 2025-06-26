from typing import List
from pathlib import Path


def list_filenames(directory: str) -> List[str]:
    # result: List[str] = []
    # for file in Path(directory).rglob("*"):
    #     if file.is_file():
    #         result.append(file.name)
    # return sorted(result, key=lambda x: x, reverse=False)
    return sorted([file.name for file in Path(directory).iterdir() if file.is_file()])


print(list_filenames("./src"))
