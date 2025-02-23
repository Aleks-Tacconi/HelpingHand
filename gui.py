import tkinter as tk
import keyboard
import ctypes
import json
import time
import threading

class GUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attributes("-fullscreen", True)
        self.attributes("-transparentcolor", self["bg"])
        self.attributes("-topmost", True)

        self.overrideredirect(True)
        self.settings_dict = {
            "binds": {
                "Full Screenshot": "[",
                "Area Screenshot": "p",
                "Voice Record": "v",
            },
            "voice": "bIQlQ61Q7WgbyZAL7IWj",
        }
        self.load_settings()
        self.binds_list = []
        self.open = True
        self.k = None
        self.timer = 0

        scale = 0.0
        for desc, bind in self.settings_dict["binds"].items():
            scale += 0.1
            bind_button = tk.Button(
                self, text=desc, bg="black", command=lambda x=desc: self.change_bind(x), fg="white", font=("Arial", 20, "bold")
            )
            bind_button.place(relx=0.1, rely=0.0+scale, anchor="center", width=350, height=80)
            self.binds_list.append(bind_button)

        self.female_voice = tk.Button(
            self, command=lambda: self.change_voice("bIQlQ61Q7WgbyZAL7IWj")
        )
        self.male_voice = tk.Button(
            self, command=lambda: self.change_voice("XjdmlV0OFXfXE6Mg2Sb7")
        )

    def toggle(self):
        if self.open:
            for button in self.binds_list:
                button.place_forget()
            self.open = False
        else:
            scale = 0.0
            for button in self.binds_list:
                scale += 0.1
                button.place(relx=0.1, rely=0.0 + scale, anchor="center", width=350, height=80)

            self.open = True

    def change_voice(self, voice):
        self.settings_dict["voice"] = voice

    def write_settings(self):
        with open("settings.json", "+w", encoding="UTF-8") as f:
            json.dump(self.settings_dict, f)

    def load_settings(self):
        with open("settings.json", "r") as f:
            binds = json.load(f)
        if not binds:
            self.write_settings()
        else:
            self.settings_dict = binds

    def user_input(self):
        bind = keyboard.read_event()
        self.k = bind

    def change_bind(self, key):
        for button in self.binds_list:
            button["state"] = tk.DISABLED
            button.config(bg="red")

        self.update()
        self.update_idletasks()

        self.k = None
        threading.Thread(target=self.user_input).start()

        while self.k is None:
            self.update()
            self.update_idletasks()

        self.timer = 2

        key_str = self.k.name

        self.settings_dict["binds"][key] = key_str
        self.write_settings()
        self.toggle()

        for button in self.binds_list:
            button["state"] = tk.ACTIVE
            button.config(bg="black")

        self.update()
        self.update_idletasks()