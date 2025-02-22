import pyautogui
import os

from PIL import ImageGrab


class ScreenShot:
    def __init__(self) -> None:
        self.PATH = os.path.join("assets", "image.png")

    def take_screenshot(self, region=None):
        if region == None:
            screenshot = ImageGrab.grab()
        else:
            screenshot = ImageGrab.grab(bbox=region)
        screenshot.save(self.PATH, "PNG")
        screenshot.close()

    def capture_region(self):
        print("Select the region to capture by dragging your mouse.")

        # Get the initial position (start point)
        start_point = pyautogui.position()
        print("Start point captured, now move your mouse to the end point.")

        # Wait for the user to select the end point
        while True:
            end_point = pyautogui.position()
            if end_point != start_point:
                break
        # Define the region: (left, top, right, bottom)
        left = min(start_point.x, end_point.x)
        top = min(start_point.y, end_point.y)
        right = max(start_point.x, end_point.x)
        bottom = max(start_point.y, end_point.y)

        region = (left, top, right, bottom)

        # Take screenshot of the selected region
        self.take_screenshot(region)
