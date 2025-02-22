from PIL import ImageGrab
import os

path = os.path.join("assets", "image.png")
screenshot = ImageGrab.grab()
screenshot.save(path, "PNG")
screenshot.close()
