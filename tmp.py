import json


def func(path: str) -> None:
    with open(f"db/wiki_data/{path}.json", "r") as file:
        parsed_data = json.load(file)

    with open("db/wiki_data/titles.txt", "a") as f:
        for data in parsed_data:
            f.write(data["title"] + "\n")


if __name__ == "__main__":
    with open("db/wiki_data/titles.txt", "w") as f:
        f.write("")

    func("blocks_data")
    func("items_data")
    func("mobs_data")
