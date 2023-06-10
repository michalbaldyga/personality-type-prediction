import tkinter as tk
from login_window import LoginWindow
from registration_window import RegistrationWindow
from main_app_window import MainAppWindow


# from twitter_prediction_window import TwitterPredictionWindows

def open_login_window(root):
    root.destroy()
    root = tk.Tk()
    app = LoginWindow(root)
    root.mainloop()


def open_registration_window(root):
    root.destroy()
    root = tk.Tk()
    app = RegistrationWindow(root)
    root.mainloop()


def open_main_app_window(root):
    root.destroy()
    root = tk.Tk()
    app = MainAppWindow(root)
    root.mainloop()
