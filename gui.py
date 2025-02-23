import tkinter as tk
import keyboard
import ctypes
import json


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

        scale = 0.0
        for desc, bind in self.settings_dict["binds"].items():
            scale += 0.1
            bind_button = tk.Button(
                self, text=desc, bg="white", command=lambda x=desc: self.change_bind(x)
            )
            bind_button.place(relx=0.2, rely=0.1+scale, anchor="center")
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
                button.place(relx=0.2, rely=0.1 + scale, anchor="center")

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

    def change_bind(self, key):
        print(1)
        bind = keyboard.read_event()
        key_str = bind.name
        self.settings_dict["binds"][key] = key_str
        self.write_settings()
