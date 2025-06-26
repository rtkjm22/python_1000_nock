
from pathlib import Path
from collections import Counter
from typing import Dict


def count_file_extensions(directory: str) -> Dict[str, int]:
  files = Path(directory).rglob('*')
  ext_list = [
    f.suffix if f.suffix else "no_ext"
    for f in files if f.is_file()
  ]
  print(Counter(ext_list))
  return dict(Counter(ext_list))

print(count_file_extensions('./src'))