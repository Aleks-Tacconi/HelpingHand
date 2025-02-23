import ctypes
from tkinter import Tk, Label
import time

GWL_EXSTYLE = -20
WS_EX_LAYERED = 0x00080000
WS_EX_TRANSPARENT = 0x00000020
WS_EX_TOPMOST = 0x00000008

root = Tk()

x = 1920
y = 1080
fg_color = "red"
font_size = 20
root.attributes("-topmost", True, "-transparentcolor", root["bg"])
root.overrideredirect(True)
root.geometry(f"{x}x{y}+0+850")

label = Label(root, text="", font=("Arial", font_size), fg="white", bg=root["bg"])
label.place(relx=0.5, rely=0.1, anchor="center")


def create_overlay(text="Overlay Text"):
    label.config(text=text)
    root.update_idletasks()
    hwnd = ctypes.windll.user32.FindWindowW(None, text)
    styles = WS_EX_LAYERED | WS_EX_TRANSPARENT | WS_EX_TOPMOST
    ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, styles)

    root.update()
    root.update_idletasks()
