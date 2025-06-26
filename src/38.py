from typing import Dict
from collections import defaultdict
from pathlib import Path
from datetime import datetime, timezone


def analysis_update_time(directory: str) -> Dict[str, int]:
    result: Dict[str, int] = defaultdict(int)

    for file in Path(directory).rglob("*"):
        if file.is_file():
            modified = datetime.fromtimestamp(file.stat().st_mtime, tz=timezone.utc)
            result[modified.strftime("%Y-%m-%d")] += 1
    return dict(result)


if __name__ == "__main__":
    print(analysis_update_time("./src"))
