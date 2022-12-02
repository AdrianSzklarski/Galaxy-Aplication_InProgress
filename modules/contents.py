from modules.main_window import MainApp
import tkinter as tk


class Contents:
    def __init__(self, root):
        self.root = root
        self.main = MainApp(self.root)
        self.test = 'Test Fuction'


    def __str__(self):
        return self.test

# if __name__ == '__main__':
#     """The main program call"""
#     root = tk.Tk()
#     app = Contents(root)
#     root.mainloop()
