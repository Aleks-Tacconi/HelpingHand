from PIL import ImageGrab
import os

path = os.path.join('..', 'assets', "image.jpg")
screenshot = ImageGrab.grab()
screenshot.save(path, 'JPEG')
screenshot.close()
