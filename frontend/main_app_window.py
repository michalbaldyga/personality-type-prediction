import tkinter as tk
from constants import *
from twitter_prediction_window import TwitterPredictionWindow


class MainAppWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Strona główna")
        self.root.geometry(f"{window_width}x{window_height}")
        self.root.configure(bg=bg_color)

        self.label = tk.Label(
            self.root,
            text="Strona główna",
            bg=bg_color,
            fg=text_color,
            font=custom_font_bold,
        )
        self.label.pack(pady=80)

        description_label = tk.Label(
            self.root,
            text="Odkryj swoją lub czyjąś osobowość dzięki naszej zaawansowanej "
            "analizie danych cyfrowych! \n\nWykorzystując informacje z platform "
            "społecznościowych, takich jak Twitter, "
            "nasza aplikacja oferuje precyzyjne prognozy dotyczące "
            "typu osobowości. Odkryj, jakie wnioski można wyciągnąć z danych i "
            "zanurz się w fascynującym świecie analizy cyfrowej!",
            bg=bg_color,
            fg=text_color,
            font=midi_font,
            wraplength=300,
        )
        description_label.pack(pady=10)

        twitter_button = tk.Button(
            self.root,
            text="Twitter",
            bg=twitter_color,
            fg=button_fg_color,
            font=midi_font_bold,
            command=self.open_twitter_prediction,
            relief=tk.FLAT,
        )
        twitter_button.config(
            padx=2,
            pady=2,
            activebackground=active_bg_color,
            activeforeground=active_fg_color,
        )
        twitter_button.pack(pady=10)

    def open_twitter_prediction(self):
        self.root.destroy()
        twitter_window = tk.Tk()
        app = TwitterPredictionWindow(twitter_window)
        twitter_window.mainloop()
