import tkinter as tk

from modules.tkinter_app import FirstPageApp

if __name__ == '__main__':
    """The main program call"""
    root = tk.Tk()
    app = FirstPageApp(root)
    root.mainloop()