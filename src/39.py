from pathlib import Path
from typing import Dict, List, Tuple
from collections import defaultdict

from pprint import pprint


# def latest_file_by_extension(directory: str) -> Dict[str, str]:
#     result: Dict[str, str] = defaultdict(str)
#     filtered: Dict[str, List[Tuple[str, float]]] = defaultdict(list)

#     for file in Path(directory).rglob("*"):
#         if file.is_file() and not file.name.startswith("."):
#             suffix = file.suffix if file.suffix else "no_ext"
#             filtered[suffix].append((str(file), file.stat().st_mtime))
#     for ext in filtered.keys():
#         result[ext] = max((item for item in filtered[ext]), key=lambda item: item[1])[0]
#     return dict(result)


def latest_file_by_extension(directory: str) -> Dict[str, str]:
    files_by_ext: Dict[str, Tuple[str, float]] = {}

    for file in Path(directory).rglob("*"):
        if file.is_file() and not file.name.startswith("."):
            ext = file.suffix or "no_ext"
            mtime = file.stat().st_mtime
            if ext not in files_by_ext or mtime > files_by_ext[ext][1]:
                files_by_ext[ext] = (str(file), mtime)

    return {ext: path for ext, (path, _) in files_by_ext.items()}


if __name__ == "__main__":
    pprint(latest_file_by_extension("./src"))
