import tkinter as tk
from tkinter import ttk
import os.path
from constants import *
import utils_front


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Personality type prediction app")
        self.root.geometry(f"{window_width}x{window_height}")
        self.root.configure(bg=bg_color)

        self.label = tk.Label(
            self.root,
            text="Welcome!",
            bg=bg_color,
            fg=text_color,
            font=custom_font_bold,
            wraplength=300,
        )
        self.label.pack(pady=80)

        self.label = tk.Label(
            self.root,
            text="You are invited to try our personality type prediction app based on digital activity",
            bg=bg_color,
            fg=text_color,
            font=midi_font,
            wraplength=300,
        )
        self.label.pack(pady=0)

        self.start_button = tk.Button(
            self.root,
            text="Let's start!",
            bg=button_bg_color,
            fg=button_fg_color,
            font=midi_font_bold,
            command=self.open_login_window,
            relief=tk.FLAT,
        )
        self.start_button.config(
            padx=2,
            pady=2,
            activebackground=active_bg_color,
            activeforeground=active_fg_color,
        )
        self.start_button.pack(pady=40)

    def open_login_window(self):
        utils_front.open_login_window(self.root)
