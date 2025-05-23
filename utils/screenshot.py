import os

import keyboard
import pyautogui
from PIL import ImageGrab


class ScreenShot:
    def __init__(self) -> None:
        self.PATH = os.path.join("db", "image.png")

    def take_screenshot(self, region=None):
        if region is None:
            screenshot = ImageGrab.grab()
        else:
            screenshot = ImageGrab.grab(bbox=region)
        screenshot.save(self.PATH, "PNG")
        screenshot.close()

    def capture_region(self):
        try:
            print("Select the region to capture by dragging your mouse.")

            start_point = pyautogui.position()
            print("Start point captured, now move your mouse to the end point.")

            while True:

                if keyboard.is_pressed("p"):
                    print("Selection finished.")
                    break

            end_point = pyautogui.position()

            left = min(start_point[0], end_point[0])
            top = min(start_point[1], end_point[1])
            right = max(start_point[0], end_point[0])
            bottom = max(start_point[1], end_point[1])

            region = (left, top, right, bottom)

            self.take_screenshot(region)
        except:
            return self.take_screenshot()
