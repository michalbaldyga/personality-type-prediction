import tkinter as tk
from constants import *
import os
import time
import utils_front


class RegistrationWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Rejestracja")
        self.root.geometry(f"{window_width}x{window_height}")
        self.root.configure(bg=bg_color)

        self.label = tk.Label(
            self.root,
            text="Rejestracja",
            bg=bg_color,
            fg=text_color,
            font=custom_font_bold,
        )
        self.label.pack(pady=80)

        main_frame = tk.Frame(self.root, bg=frame_color, padx=10, pady=10)
        main_frame.pack(padx=10)

        login_label = tk.Label(
            main_frame,
            text="Login:",
            bg=frame_color,
            fg=text_color,
            font=midi_font,
        )
        login_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.login_entry = tk.Entry(
            main_frame,
            bg=bg_entry_color,
            fg=text_color,
            font=midi_font,
        )
        self.login_entry.grid(row=0, column=1, padx=10, pady=10)

        password_label = tk.Label(
            main_frame,
            text="Hasło:",
            bg=frame_color,
            fg=text_color,
            font=midi_font,
        )
        password_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        self.password_entry = tk.Entry(
            main_frame,
            show="*",
            bg=bg_entry_color,
            fg=text_color,
            font=midi_font,
        )
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        confirm_password_label = tk.Label(
            main_frame,
            text="Powtórz hasło:",
            bg=frame_color,
            fg=text_color,
            font=midi_font,
        )
        confirm_password_label.grid(row=2, column=0, padx=10, pady=10, sticky=tk.W)

        self.confirm_password_entry = tk.Entry(
            main_frame,
            show="*",
            bg=bg_entry_color,
            fg=text_color,
            font=midi_font,
        )
        self.confirm_password_entry.grid(row=2, column=1, padx=10, pady=10)

        self.error_label = tk.Label(
            self.root,
            text="",
            bg=bg_color,
            fg=error_color,
            font=mini_font,
        )
        self.error_label.pack(pady=10)

        self.success_label = tk.Label(
            self.root,
            text="",
            bg=bg_color,
            fg=success_color,
            font=mini_font,
        )
        self.success_label.pack(pady=10)

        registration_button = tk.Button(
            main_frame,
            text="Zarejestruj się",
            bg=button_confirmation_color,
            fg=button_fg_color,
            font=midi_font_bold,
            command=self.register,
            relief=tk.FLAT,
            activebackground=active_bg_color,
            activeforeground=active_fg_color,
        )
        registration_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        registration_button = tk.Button(
            self.root,
            text="Powrót od logowania",
            bg=button_bg_color,
            fg=button_fg_color,
            font=mini_font_underline,
            command=self.open_login_window,
            relief=tk.FLAT,
        )
        registration_button.config(
            padx=2,
            pady=2,
            activebackground=active_bg_color,
            activeforeground=active_fg_color,
        )
        registration_button.pack(pady=10)

    def register(self):
        username = self.login_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if not username or not password or not confirm_password:
            self.error_label.config(text="Wszystkie pola muszą być wypełnione")
            return

        user_directory = os.path.join("users", username)
        if os.path.exists(user_directory):
            self.error_label.config(text="Taki użytkownik już istnieje")
            return

        if password != confirm_password:
            self.error_label.config(text="Podane hasła nie są jednakowe")
            return

        os.makedirs(user_directory)
        password_file = os.path.join(user_directory, "password.txt")
        with open(password_file, "w") as file:
            file.write(password)

        # Usunięcie poprzednich komunikatów o błędach i sukcesie
        self.error_label.config(text="")
        self.success_label.config(text="")

        self.login_entry.delete(0, tk.END)
        self.password_entry.delete(0, tk.END)
        self.confirm_password_entry.delete(0, tk.END)

        self.success_label.config(text="Rejestracja przebiegła pomyślnie!")

        # Otwieranie okna logowania po pomyślnej rejestracji z opóźnieniem 1 sekundy
        self.root.after(5000, self.open_login_window)

    def open_login_window(self):
        utils_front.open_login_window(self.root)
