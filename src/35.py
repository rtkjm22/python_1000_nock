from pathlib import Path


def count_specific_extension_files(directory: str, ext: str) -> int:
    result: int = 0
    for file in Path(directory).rglob("*"):
        if file.is_file() and file.suffix.lower() == f".{ext.lower()}":
            result += 1
    return result


print(count_specific_extension_files("./src", "py"))
