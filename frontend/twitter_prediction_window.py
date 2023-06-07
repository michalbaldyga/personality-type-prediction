import tkinter as tk
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))
print(os.path.realpath("backend"))
from backend.predict import predict
from backend.user_input import get_tweets
from constants import *
import utils_front


class TwitterPredictionWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Twitter prediction")
        self.root.geometry(f"{window_width}x{window_height}")
        self.root.configure(bg=bg_color)

        self.title_label = tk.Label(self.root, text="Twitter prediction", bg=bg_color, fg=twitter_color, font=custom_font_bold)
        self.title_label.pack(pady=30)

        description_label = tk.Label(
            self.root,
            text="Prediction based on Twitter username. Please enter below the nickname of the user whose personality "
                 "type you want to predict and the number of tweets (from the most recent) based on which the "
                 "prediction will take place",
            bg=bg_color,
            fg=text_color,
            font=midi_font,
            wraplength=300,
        )
        description_label.pack(pady=20)

        details_frame = tk.Frame(self.root, bg=frame_color, padx=10, pady=10)
        details_frame.pack()

        username_label = tk.Label(details_frame, text="nickname:", bg=frame_color, fg=text_color, font=midi_font)
        username_label.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W)

        self.username_entry = tk.Entry(details_frame, bg=bg_entry_color, fg=text_color, font=midi_font)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        tweet_label = tk.Label(details_frame, text="no. tweets:", bg=frame_color, fg=text_color, font=midi_font)
        tweet_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.W)

        self.tweet_value = tk.StringVar()
        self.tweet_value.set("0")

        self.tweet_entry = tk.Entry(
            details_frame,
            bg=bg_entry_color,
            fg=text_color,
            font=midi_font,
            textvariable=self.tweet_value,
        )
        self.tweet_entry.grid(row=1, column=1, padx=10, pady=10)
        self.tweet_entry.bind("<KeyRelease>", self.update_scale_value)

        self.tweet_scale_value = tk.IntVar()
        self.tweet_scale_value.set(0)

        self.scale = tk.Scale(
            details_frame,
            from_=0,
            to=1000,
            orient=tk.HORIZONTAL,
            command=self.on_scale_change,
            variable=self.tweet_scale_value,
            bg=frame_color,
            fg=text_color,
            font=midi_font,
            highlightthickness=0,
        )
        self.scale.set(0)
        self.scale.grid(row=2, column=1, padx=10, pady=10, sticky=tk.W)

        self.error_label = tk.Label(self.root, text="", bg=bg_color, fg=error_color, font=mini_font)
        self.error_label.pack()

        predict_button = tk.Button(
            details_frame,
            text="Predict",
            bg=twitter_color,
            fg=button_fg_color,
            font=midi_font_bold,
            command=self.predict_personality,
            relief=tk.FLAT,
            activebackground=active_bg_color,
            activeforeground=active_fg_color,
        )
        predict_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.result_label = tk.Label(self.root, text="Prediction results", bg=bg_color, fg=text_color, font=midi_font)
        self.result_label.pack(pady=10)

        registration_button = tk.Button(
            self.root,
            text="Go back",
            bg=bg_color,
            fg=text_color,
            font=mini_font_underline,
            command=self.open_main_app_window,
            relief=tk.FLAT,
            padx=2,
            pady=2,
            activebackground=bg_color,
            activeforeground=active_fg_color,
        )
        registration_button.pack(pady=10)

        self.button_twitter_details = tk.Button(
            self.root,
            text="Click here to see a detailed description",
            bg=twitter_color,
            fg=button_fg_color,
            font=mini_font,
            command=self.show_details,
            relief=tk.FLAT,
            padx=2,
            pady=2,
            activebackground=active_bg_color,
            activeforeground=active_fg_color,
        )
        self.button_twitter_details.pack(pady=10)
        # Hide the button at the beginning
        self.button_twitter_details.pack_forget()

    def predict_personality(self):
        username = self.username_entry.get()
        tweet_count = int(self.tweet_entry.get())

        if not username or not tweet_count:
            self.error_label.config(text="Fields cannot be empty")
            self.result_label.config(text="")
            # Hide button in case of error
            self.button_twitter_details.pack_forget()
            return

        # Removal of previous error messages
        self.error_label.config(text="")

        if tweet_count <= 0:
            self.error_label.config(text="The number of tweets must be greater than zero")
            self.result_label.config(text="")
            # Hide button in case of error
            self.button_twitter_details.pack_forget()
            return

        # Removal of previous error messages
        self.error_label.config(text="")

        # Code to process prediction based on Twitter username
        tweets_content = get_tweets(username, tweet_count)
        if tweets_content != '':
            predicted_types = predict(tweets_content)
        else:
            self.error_label.config(text="Account does not exist or has no tweets")
            self.result_label.config(text="")
            # Hide button in case of error
            self.button_twitter_details.pack_forget()
            return

        if predicted_types is None:
            self.error_label.config(text="Can't load model")
            self.result_label.config(text="")
            # Hide button in case of error
            self.button_twitter_details.pack_forget()
            return

        # Removal of previous error messages
        self.error_label.config(text="")

        # Display of the prediction result
        self.result_label.config(text="Prediction result:\n\n "
                                      + "  1." + predicted_types[0]
                                      + "  2." + predicted_types[1]
                                      + "  3." + predicted_types[2])
        # Displaying the button after a correct prediction
        self.button_twitter_details.pack()

    def on_scale_change(self, value):
        self.tweet_value.set(value)

    def update_scale_value(self, event):
        try:
            value = int(self.tweet_value.get())
            self.scale.set(value)
        except ValueError:
            pass

    def show_details(self):
        pass

    def open_main_app_window(self):
        utils_front.open_main_app_window(self.root)
