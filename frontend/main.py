import tkinter as tk
from tkinter import ttk
from constants import *
from main_window import MainWindow


if __name__ == "__main__":
    root = tk.Tk()
    app = MainWindow(root)
    root.mainloop()
