import os
import requests
from bs4 import BeautifulSoup


HEADINGS = ["h1", "h2", "h3", "h4", "h5", "h6"]
OUTPUT_PATH = os.path.join("db", "info.json")


def get_wiki_url(block_name: str) -> str:
    block_name = block_name.replace(" ", "_")

    return f"https://minecraft.fandom.com/wiki/{block_name}"


def scrape_url(url: str) -> bool:
    response = requests.get(url)

    if response.status_code != 200:
        return False

    soup = BeautifulSoup(response.text, "html.parser")
    headings = soup.find_all(HEADINGS)
    paragraphs = soup.find_all("p")

    paragraph_index = 0

    with open(file=OUTPUT_PATH, mode="w+", encoding="utf-8") as f:
        for heading in headings:
            f.write(heading.get_text() + "\n")
            f.write("-" * len(heading.get_text()) + "\n")

            while paragraph_index < len(paragraphs):
                if paragraphs[paragraph_index].find_previous(HEADINGS) == heading:
                    f.write(paragraphs[paragraph_index].get_text())
                    paragraph_index += 1
                else:
                    break

            f.write("\n\n")

        return True

    return False
