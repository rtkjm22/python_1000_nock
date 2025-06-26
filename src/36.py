from datetime import datetime
from pathlib import Path
from typing import List


def recent_files(directory: str) -> List[str]:
    return [
        str(file)
        for file in Path(directory).rglob("*")
        if file.is_file()
        and (file.stat().st_mtime) >= datetime.now().timestamp() - 24 * 60 * 60
    ]


print(recent_files("./src"))
