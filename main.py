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
from utils.data import load_data
from voice_output import generate_response_voice
from voice_output2 import generate_response_voice2
from text_overlay import create_overlay
import ctypes

IMAGE_PROMPT = """
Given the image provided

- identify the most central item in the image
- reply only with the name of the item
- ignore all other details or description
"""

TEXT_PROMPT = """
Given the following information present the most important information for a new player in maximum 30 words. Also,
prioritise recipies that can be made from the block if applicable.\n\n
"""

TITLES = read_titles()

class Global:
    def __init__(self):
        self.start = False





def query(ai: AI) -> str | None:
    #response = ai.image_prompt(IMAGE_PROMPT)
    response = "Red Sand"

    if response is None:
        return "Error"

    title = find_closest_match(response, TITLES)
    print(title)

    load_data(title.lower())
    info = read_file(os.path.join("db", "info.json"))
    summary = ai.text_prompt(TEXT_PROMPT + info)

    return summary


def print_sentence_letter_by_letter(sentence, a, delay=0.08):
    while not a.start:
        continue
    for letter in sentence:
        print(letter, end="", flush=True)

        time.sleep(delay)
    print()
    a.start = False


def main() -> None:
    ai = AI()
    screen = ScreenShot()
    globals = Global()
    while True:
        if keyboard.is_pressed("k"):
            print("Pressed")
            screen.take_screenshot()
            summary = query(ai)

            if summary != "Error":
                threading.Thread(target=generate_response_voice2, args=(summary, globals)).start()
                print_sentence_letter_by_letter(summary, globals)

                #create_overlay(summary, font_size=12, x=100, y=100)

if __name__ == "__main__":
    main()
