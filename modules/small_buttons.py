import webbrowser

from modules.main_window import MainApp
import tkinter as tk
from PIL import Image

class SmallButtons:
    def __init__(self, root):
        self.root = root
        self.main = MainApp(self.root)
        self.my_canvas = self.main.my_canvas

        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()

        self.get_buttons()

    def get_github(self):
        webbrowser.open_new(r"https://github.com/AdrianSzklarski")

    def get_linked(self):
        webbrowser.open_new(r"https://www.linkedin.com/in/szklarskiadrian/")

    def get_buttons(self):
        """Method to add an in and out button on the front page"""
        # Positions of widget buttons
        _WIDTH_SMALL = _HEIGHT_SMALL = 60
        _X = 0.04
        _Y = 0.07

        # Position button
        if self.screen_width <= 2048:
            self._positionX = self.screen_width * _X
            self._positionY = self.screen_height * _Y
        elif 2048 < self.screen_width < 4096:
            self._positionX = self.screen_width * (_X / 2)
            self._positionY = self.screen_height * _Y

        btn_exit = Image.open("/home/adrian/Pulpit/my_application/photo/small_exit.png")
        btn_gitH = Image.open("/home/adrian/Pulpit/my_application/photo/GitHub.png")
        btn_link = Image.open("/home/adrian/Pulpit/my_application/photo/Linkedin.png")

        image_exit = btn_exit.resize((_WIDTH_SMALL, _HEIGHT_SMALL), Image.ANTIALIAS)
        image_gitH = btn_gitH.resize((_WIDTH_SMALL, _HEIGHT_SMALL), Image.ANTIALIAS)
        image_link = btn_link.resize((_WIDTH_SMALL, _HEIGHT_SMALL), Image.ANTIALIAS)

        image_exit.save(fp="/home/adrian/Pulpit/my_application/photo/small_exitScale.png")
        image_gitH.save(fp="/home/adrian/Pulpit/my_application/photo/GitHubScale.png")
        image_link.save(fp="/home/adrian/Pulpit/my_application/photo/Linkedin.png")

        btn_exit = tk.PhotoImage(file="/home/adrian/Pulpit/my_application/photo/small_exitScale.png")
        btn_gitH = tk.PhotoImage(file="/home/adrian/Pulpit/my_application/photo/GitHubScale.png")
        btn_link = tk.PhotoImage(file="/home/adrian/Pulpit/my_application/photo/Linkedin.png")

        exit_btn = tk.Button(borderwidth=1, image=btn_exit, command=quit)
        self.gitH_btn = tk.Button(borderwidth=1, image=btn_gitH, command=self.get_github)
        self.link_btn = tk.Button(borderwidth=1, image=btn_link, command=self.get_linked)

        self.my_canvas.create_window(self._positionX*21.2, self._positionY*11, anchor="nw", window=exit_btn,
                                     height=60, width=60)
        self.my_canvas.create_window(self._positionX*20.2, self._positionY*11, anchor="nw", window=self.gitH_btn,
                                     height=60, width=60)
        self.my_canvas.create_window(self._positionX*19.2, self._positionY*11, anchor="nw", window=self.link_btn,
                                     height=60, width=60)

