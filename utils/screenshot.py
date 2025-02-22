<<<<<<< HEAD
from PIL import ImageGrab
import tkinter as tk
import os



class ScreenShot:
    def __init__(self, X, Y) -> None:
        self.PATH = os.path.join("assets", "image.png")
        self.X = X
        self.Y = Y

    def take_screenshot(self):
        screenshot = ImageGrab.grab()
        screenshot.save(self.PATH, "PNG")
        screenshot.close()

    def take_screenshot_area(self):
        screenshot = ImageGrab.grab()
        screenshot.save(self.PATH, "PNG")
        screenshot.close()
=======
import os
from PIL import ImageGrab

PATH = os.path.join("assets", "image.png")

def take_screenshot():
    screenshot = ImageGrab.grab()
    screenshot.save(PATH, "PNG")
    screenshot.close()
>>>>>>> a68296e1a71298b086ca19b9124ec410721f9a9c
