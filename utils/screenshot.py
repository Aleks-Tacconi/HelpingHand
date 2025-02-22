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
