def read_file(file: str) -> str:
    with open(file=file, mode="r", encoding="utf-8") as f:
        content = "\n".join(f.readlines())

    return content
