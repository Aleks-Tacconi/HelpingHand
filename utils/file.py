import os

def read_file(file: str) -> str:
    with open(file=file, mode="r", encoding="utf-8") as f:
        content = "\n".join(f.readlines())

    return content

def read_titles() -> list:
    titles = []

    file = os.path.join("db", "titles.txt")

    with open(file=file, mode="r", encoding="utf-8") as f:
        for title in f.readlines():
            titles.append(title.strip().upper())

    return titles
