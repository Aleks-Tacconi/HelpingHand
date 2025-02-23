import os
import time
import keyboard

import gui as g
from ai import AI
import threading
from utils import read_file
from utils import read_titles
from utils import ScreenShot
from utils import find_closest_match
from voice_output import generate_response_voice
from voice_output2 import generate_response_voice2
from text_overlay import create_overlay
from utils import load_data
from text_overlay import root
from speak import speak


IMAGE_PROMPT = """
Given the image provided
- It is an image from minecraft
- Identify and describe the item the center of the image
- include type and as much visual details as possible
"""

TEXT_PROMPT = """
Must address me as Pookie.
Given the following information in a coherent way for a new player in maximum 50 words.
Give information in this order of importance if applicable (Give in sentence format like as a casual conversation): 
- Do not give any information related to golden pickaxe unless the item is golden or a gold pickaxe.
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
    response = ai.text_prompt(
        "Identify what Minecraft item the following text is about, reply with only the name of the item:\n"
        + response
    )
    # response = "Red Sand"
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


def check(ai, everything):
    summary = query(ai)
    if summary != "Error":
        threading.Thread(
            target=generate_response_voice2, args=(summary, everything)
        ).start()
        print_sentence_letter_by_letter(summary, everything)
        # create_overlay(summary, font_size=12, x=100, y=100)

def main() -> None:
    ai = AI()
    screen = ScreenShot()
    everything = Global()
    gui = g.GUI()



    while True:
        if gui.timer == 0:
            if keyboard.is_pressed(","):
                gui.toggle()
                gui.update()
                gui.update_idletasks()
                time.sleep(1)

            if keyboard.is_pressed(gui.settings_dict["binds"]["Voice Record"]):
                speach = speak()
                print(speach)
                response = ai.text_prompt(speach + "\n\n" + "Give me a simple but concise answer with relevant information, max 50 words. You must call me Pookie and act like you love me. Note: the questions will always be related to minecraft")
                threading.Thread(target=generate_response_voice2, args=(response, everything)).start()
                print_sentence_letter_by_letter(response, everything)

            if keyboard.is_pressed(gui.settings_dict["binds"]["Full Screenshot"]):
                print("Processing...")
                screen.take_screenshot()
                check(ai, everything)

            if keyboard.is_pressed(gui.settings_dict["binds"]["Area Screenshot"]):
                print("Processing...")
                create_overlay("Select the region to capture by dragging your mouse.")
                screen.capture_region()
                check(ai, everything)
        else:
            gui.timer -= 1
            time.sleep(0.1)

        root.update()
        root.update_idletasks()


if __name__ == "__main__":
    main()
