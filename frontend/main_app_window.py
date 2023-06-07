import tkinter as tk
from constants import *
from twitter_prediction_window import TwitterPredictionWindow


class MainAppWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Main Page")
        self.root.geometry(f"{window_width}x{window_height}")
        self.root.configure(bg=bg_color)

        self.label = tk.Label(
            self.root,
            text="Main Page",
            bg=bg_color,
            fg=text_color,
            font=custom_font_bold,
        )
        self.label.pack(pady=80)

        description_label = tk.Label(
            self.root,
            text="Discover your or someone else's personality with our advanced "
             "analyzing app! \n\nUsing information from social media platforms such as Twitter, "
             "our application offers precise forecasts for a "
             "personality type. Discover what conclusions can be drawn from the data and "
             "immerse yourself in the fascinating world of digital analysis!",
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
