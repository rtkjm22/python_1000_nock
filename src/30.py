from pathlib import Path
from typing import Dict


def count_file_extensions(directory: str) -> Dict[str, int]:
    result: Dict[str, int] = {}
    for file in Path(directory).rglob("*"):
        if file.is_file():
            ext = file.suffix if file.suffix else "no_ext"
            result[ext] = result.get(ext, 0) + 1
    return result


print(count_file_extensions("./src"))
