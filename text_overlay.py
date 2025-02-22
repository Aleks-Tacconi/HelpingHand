import ctypes
import os
from tkinter import Tk, Label

GWL_EXSTYLE = -20
WS_EX_LAYERED = 0x00080000
WS_EX_TRANSPARENT = 0x00000020
WS_EX_TOPMOST = 0x00000008

def create_overlay(text="Overlay Text", font_size=40, fg_color="red", x=500, y=300):
    if os.name == 'nt':
        root = Tk()
        root.title(text)
        root.attributes("-topmost", True, "-transparentcolor", root["bg"])
        root.overrideredirect(True)
        root.geometry(f"+{x}+{y}")

        label = Label(root, text=text, font=("Arial", font_size), fg=fg_color, bg=root["bg"])
        label.pack()

        root.update_idletasks()
        hwnd = ctypes.windll.user32.FindWindowW(None, text)
        styles = WS_EX_LAYERED | WS_EX_TRANSPARENT | WS_EX_TOPMOST
        ctypes.windll.user32.SetWindowLongW(hwnd, GWL_EXSTYLE, styles)

        root.mainloop()

    elif os.name == 'posix':
        root = Tk()
        root.title(text)
        root.attributes("-topmost", True)
        root.geometry(f"+{x}+{y}")
        root.configure(bg="black")

        label = Label(root, text=text, font=("Arial", font_size), fg=fg_color, bg="black")
        label.pack()

        root.update_idletasks()
        root.attributes("-transparentcolor", "black")

        root.mainloop()

create_overlay("Hello, World!", font_size=50, x=100, y=100)
