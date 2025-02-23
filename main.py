import os
import time
import keyboard

from ai import AI
import threading
from utils import get_wiki_url
from utils import scrape_url
from utils import read_file
from utils import read_titles
from utils import ScreenShot
from utils import find_closest_match
from voice_output import generate_response_voice
from voice_output2 import generate_response_voice2
from text_overlay import create_overlay

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
    response = "Red Sand"

    if response is None:
        return "Error"

    title = find_closest_match(response.lower(), TITLES)
    print(title)

    url = get_wiki_url(title)
    content = scrape_url(url)

    if content:
        info = read_file(os.path.join("db", "info.txt"))
        summary = ai.text_prompt(TEXT_PROMPT + info)

        return summary
    return "Error"

def print_sentence_letter_by_letter(sentence, delay=0.1):
    for letter in sentence:
        print(letter, end='', flush=True)
        time.sleep(delay)
    print()

def main() -> None:
    ai = AI()
    screen = ScreenShot()
    while True:
        if keyboard.is_pressed("k"):
            screen.take_screenshot()
            summary = query(ai)

            if summary != "Error":
                generate_response_voice2(summary)
                create_overlay(summary, font_size=12, x=100, y=100)

if __name__ == "__main__":
    main()
