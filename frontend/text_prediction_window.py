import threading
import tkinter as tk
import sys
import os
from tkinter import ttk

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'backend'))
from backend.predict import predict
from constants import *
import utils_front


class TextPredictionWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Text prediction")
        self.root.geometry(f"{window_width}x{window_height}")
        self.root.configure(bg=bg_color)

        self.title_label = tk.Label(self.root, text="Text prediction", bg=bg_color, fg=twitter_color,
                                    font=custom_font_bold)
        self.title_label.pack(pady=30)

        description_label = tk.Label(
            self.root,
            text="Prediction based on given text. Please enter below text based on which prediction will take place",
            bg=bg_color,
            fg=text_color,
            font=midi_font,
            wraplength=300,
        )
        description_label.pack(pady=20)

        details_frame = tk.Frame(self.root, bg=frame_color, padx=10, pady=10)
        details_frame.pack()

        self.text_entry = tk.Text(details_frame, height=14, width=40)
        self.text_entry.pack()

        self.error_label = tk.Label(self.root, text="", bg=bg_color, fg=error_color, font=mini_font)
        self.error_label.pack()
        self.registration_button = tk.Button(
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
        self.predict_button = tk.Button(
            details_frame,
            text="Predict",
            bg=twitter_color,
            fg=button_fg_color,
            font=midi_font_bold,
            command=self.predict_personality,
            relief=tk.FLAT,
            activebackground=active_bg_color,
            activeforeground=active_fg_color
        )
        self.predict_button.pack(pady=7)

        self.progress_bar = ttk.Progressbar(self.root,
                                            orient='horizontal',
                                            length=300,
                                            mode='indeterminate')
        self.progress_bar.pack(pady=5)
        self.progress_bar.pack_forget()

        self.result_label = tk.Label(self.root,
                                     text="",
                                     bg=bg_color,
                                     fg=text_color,
                                     font=midi_font)
        self.result_label.pack(pady=10)
        self.registration_button.pack(pady=5)
        self.registration_button.pack_forget()
        # TODO Add details about personality types

        '''
            self.button_text_details = tk.Button(
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
            self.button_text_details.pack(pady=10)
            self.button_text_details.pack_forget()  # hide a button
        '''

    def predict_personality(self):
        self.result_label.config(text="")
        entered_text = self.text_entry.get("1.0", 'end-1c')

        if not entered_text or entered_text == '':
            self.error_label.config(text="Field cannot be empty")
            self.result_label.config(text="")
            return

        # Removal of previous error messages
        self.error_label.config(text="")

        threading.Thread(target=self.prepare_prediction, args=(entered_text,), daemon=True).start()

    # TODO details of the type
    '''
    def show_details(self):
        pass
    '''

    def prepare_prediction(self, entered_text):
        self.registration_button.pack_forget()
        self.progress_bar.pack(pady=5)
        self.progress_bar.start()
        self.registration_button.pack(pady=10)

        # Code to process prediction based on entered text
        if entered_text != '':
            predicted_types = predict(entered_text)
        else:
            self.error_label.config(text="Entered text is empty")
            self.result_label.config(text="")
            return

        if predicted_types is None:
            self.error_label.config(text="Can't load model")
            self.result_label.config(text="")
            return

        # Removal of previous error messages
        self.error_label.config(text="")
        self.progress_bar.stop()
        self.progress_bar.pack_forget()

        # Display of the prediction result
        self.result_label.config(text="Prediction result:\n\n "
                                      + "  1." + predicted_types[0]
                                      + "  2." + predicted_types[1]
                                      + "  3." + predicted_types[2])

    def open_main_app_window(self):
        utils_front.open_main_app_window(self.root)
