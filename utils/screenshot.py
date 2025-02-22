import os
from PIL import ImageGrab

PATH = os.path.join("assets", "image.png")

def take_screenshot(PATH):
    screenshot = ImageGrab.grab()
    screenshot.save(PATH, "PNG")
    screenshot.close()
