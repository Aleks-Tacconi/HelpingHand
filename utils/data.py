import json
import os


def load_data(key: str) -> None:
    path = os.path.join("db", "wiki_data.json")
    with open(file=path, mode="r", encoding="utf-8") as f:
        dct = json.load(f)

    item = {key: dct[key]}

    path = os.path.join("db", "info.json")
    with open(file=path, mode="w", encoding="utf-8") as f:
        json.dump(item, f)
