import os
import keyboard

from ai import AI

from utils import get_wiki_url
from utils import scrape_url
from utils import read_file
from utils import read_titles
from utils import take_screenshot
from utils import find_closest_match

from voice_output import generate_response_voice

IMAGE_PROMPT = """
Given the image provided

- identify the most central item in the image
- reply only with the name of the item
- ignore all other details or description
"""

TEXT_PROMPT = """
Given the following information summarize the most important content
relevant to a user playing a game into a short paragraph:\n\n
"""

TITLES = read_titles()


def query(ai: AI) -> str | None:
    # response = ai.image_prompt(IMAGE_PROMPT)
    response = "Birch tree"

    if response is None:
        return "Error"

    title = find_closest_match(response.upper(), TITLES)
    print(title)

    url = get_wiki_url(title)
    content = scrape_url(url)

    if content:
        info = read_file(os.path.join("db", "info.txt"))
        summary = ai.text_prompt(TEXT_PROMPT + info)

        return summary
    return "Error"


def main() -> None:
    ai = AI()

    while True:
        if keyboard.is_pressed("k"):
            take_screenshot()
            summary = query(ai)

            if summary != "Error":
                generate_response_voice(summary)


if __name__ == "__main__":
    main()
