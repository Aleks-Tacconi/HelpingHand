import tkinter as tk
import keyboard
import ctypes
import json


class GUI(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attributes("-fullscreen", True)
        self.config(bg="black")
        self.settings_dict = {
            "binds": {"Full Screenshot": "[", "Area Screenshot": "]"},
            "voice": "TOBETOKEN",  # TOKEN TO BE PLACED
        }
        self.load_settings()
        self.binds_list = []

        for desc, bind in self.settings_dict["binds"].items():
            bind_info = tk.Label(self, text=desc)
            bind_button = tk.Button(
                self, text=bind, bg="white", command=lambda x = desc: self.change_bind(x)
            )

        self.female_voice = tk.Button(self, command=lambda: self.change_voice("token"))
        self.male_voice = tk.Button(self, command=lambda: self.change_voice("token1"))

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
        bind = keyboard.read_event()
        self.settings_dict["binds"][key] = bind
