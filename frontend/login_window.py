import tkinter as tk
from main_app_window import MainAppWindow
from constants import *
import os
import utils


class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Logowanie")
        self.root.geometry(f"{window_width}x{window_height}")
        self.root.configure(bg=bg_color)

        self.label = tk.Label(self.root, text="Logowanie", bg=bg_color, fg=text_color, font=custom_font_bold)
        self.label.pack(pady=80)

        login_frame = tk.Frame(self.root, bg=frame_color, padx=10, pady=10)
        login_frame.pack()

        login_label = tk.Label(login_frame, text="Login:", bg=frame_color, fg=text_color, font=midi_font)
        login_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.login_entry = tk.Entry(login_frame, bg=bg_entry_color, fg=text_color, font=midi_font)
        self.login_entry.grid(row=0, column=1, padx=10, pady=10)

        password_label = tk.Label(login_frame, text="Hasło:", bg=frame_color, fg=text_color, font=midi_font)
        password_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        self.password_entry = tk.Entry(login_frame, show="*", bg=bg_entry_color, fg=text_color, font=midi_font)
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        self.error_label = tk.Label(self.root, text="", bg=bg_color, fg=error_color, font=mini_font)
        self.error_label.pack(pady=10)

        self.success_label = tk.Label(self.root, text="", bg=bg_entry_color, fg=success_color, font=mini_font)
        self.success_label.pack(pady=10)

        login_button = tk.Button(
            login_frame,
            text="Zaloguj",
            bg=button_confirmation_color,
            fg=button_fg_color,
            font=midi_font_bold,
            command=self.login,
            relief=tk.FLAT,
            activebackground=active_bg_color,
            activeforeground=active_fg_color,
        )
        login_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

        registration_label = tk.Label(
            self.root,
            text="Nie masz jeszcze konta?",
            bg=bg_color,
            fg=text_color,
            font=mini_font,
        )
        registration_label.pack(pady=5)

        registration_button = tk.Button(
            self.root,
            text="Zarejestruj się",
            bg=button_bg_color,
            fg=button_fg_color,
            font=mini_font_underline,
            command=self.open_registration_window,
            relief=tk.FLAT,
        )
        registration_button.config(
            padx=2,
            pady=2,
            activebackground=active_bg_color,
            activeforeground=active_fg_color,
        )
        registration_button.pack(pady=10)

    def login(self):
        username = self.login_entry.get()
        password = self.password_entry.get()

        user_directory = os.path.join("users", username)
        if not os.path.exists(user_directory):
            self.error_label.config(text="Taki użytkownik nie istnieje")
            return

        password_file = os.path.join(user_directory, "password.txt")
        if not os.path.isfile(password_file):
            self.error_label.config(text="Taki użytkownik nie istnieje")
            return

        with open(password_file, "r") as file:
            stored_password = file.read().strip()

        if password != stored_password:
            self.error_label.config(text="Podano błędne hasło")
        else:
            self.error_label.config(text="")
            self.success_label.config(text="Zalogowano pomyślnie")
            self.root.after(1000, self.open_main_app_window)

    def open_registration_window(self):
        utils.open_registration_window(self.root)

    def open_main_app_window(self):
        utils.open_main_app_window(self.root)
