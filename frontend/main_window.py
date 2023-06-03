import tkinter as tk
from tkinter import ttk
import os.path
from constants import *
import utils


class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Aplikacja do predykcji typu osobowości")
        self.root.geometry(f"{window_width}x{window_height}")
        self.root.configure(bg=bg_color)

        self.label = tk.Label(
            self.root,
            text="Witaj!",
            bg=bg_color,
            fg=text_color,
            font=custom_font_bold,
            wraplength=300,
        )
        self.label.pack(pady=80)

        self.label = tk.Label(
            self.root,
            text="Zapraszamy do wypróbowania naszej aplikacji do predykcji typu osobowości na podstawie aktywności cyfrowej!",
            bg=bg_color,
            fg=text_color,
            font=midi_font,
            wraplength=300,
        )
        self.label.pack(pady=0)

        self.start_button = tk.Button(
            self.root,
            text="Zaczynamy!",
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
        utils.open_login_window(self.root)