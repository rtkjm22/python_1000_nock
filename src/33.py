from pathlib import Path
from typing import Dict, TypedDict


def get_subdir_sizes(root_dir: str) -> Dict[str, int]:
    result: Dict[str, int] = {}
    root = Path(root_dir)

    for subdir in root.iterdir():
        if subdir.is_dir() and not subdir.name.startswith("."):
            total = 0
            for file in subdir.rglob("*"):
                if file.is_file() and not file.name.startswith("."):
                    total += file.stat().st_size
            result[subdir.name] = total
    return result


print(get_subdir_sizes("./src"))
