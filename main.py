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
from utils import load_data
from text_overlay import root



IMAGE_PROMPT = """
Given the image provided
- It is an image from minecraft
- Identify and describe the item the center of the image
- include type and as much visual details as possible
"""

TEXT_PROMPT = """
Given the following information in a coherent way for a new player in maximum 30 words.
Give information in this order of importance if applicable (Give in sentence format like as a casual conversation): 
- Name of item
- The Crafting Recipe if applicable
- What recommended tool/method is used to acquire this item
- Special facts
\n\n
"""

TITLES = read_titles()

class Global:
    def __init__(self):
        self.start = False
def query(ai: AI) -> str | None:
    create_overlay("Processing...")
    response = ai.image_prompt(IMAGE_PROMPT)
    response = ai.text_prompt("Identify what Minecraft item the following text is about, reply with only the name of the item:\n" + response)
    #response = "Red Sand"
    print(response)

    if response is None:
        return "Error"

    title = find_closest_match(response, TITLES)
    load_data(title.lower())
    print(title)



    info = read_file(os.path.join("db", "info.json"))
    summary = ai.text_prompt(TEXT_PROMPT + info)

    return summary


def print_sentence_letter_by_letter(sentence, a, delay=0.07):
    while not a.start:
        continue

    word = ""
    words = []
    for letter in sentence + " ":
        print(letter, end="", flush=True)
        word += letter

        if letter == " ":
            words.append(word)
            create_overlay(" ".join(words))
            word = ""
        if len(words) == 7:
            words = []


        time.sleep(delay)

    print()
    a.start = False
    time.sleep(delay)
    create_overlay("")

def load_keybind():
    try:
        with open("keybind.txt", "r") as file:
            return file.read().strip()
    except FileNotFoundError:
        return "k"

def main() -> None:
    ai = AI()
    screen = ScreenShot()
    globals = Global()
    while True:

        keybind = load_keybind()
        if keyboard.is_pressed("k"):
            print("Processing...")
            screen.take_screenshot()
            summary = query(ai)

            if summary != "Error":
                threading.Thread(target=generate_response_voice2, args=(summary, globals)).start()
                print_sentence_letter_by_letter(summary, globals)
                #create_overlay(summary, font_size=12, x=100, y=100)

        root.update()
        root.update_idletasks()

if __name__ == "__main__":
    main()
