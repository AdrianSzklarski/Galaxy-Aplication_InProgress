from tkinter import Image
import tkinter as tk
from PIL import Image

from modules.contents import Contents
from modules.main_window import MainApp

CONST_SCREEN_HEIGHT_MORE = 0.85

CONST_SCREEN_WIDTH_MORE = 0.45

CONST_SCREEN_WIDTH_LESS = 0.9


class FirstPageApp:
    def __init__(self, root):
        self.root = root
        self.main = MainApp(self.root)
        self.my_canvas = self.main.my_canvas

        self.frame = None
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=0, column=0)

        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()

        # calling modules
        self.get_welcome()
        self.get_buttons()

    def get_welcome(self):
        """A method that adds text to the first page"""
        #  Welcome text
        title = """Learning is easy, programming is easy"""
        welcome = """WELCOME TO MY PROGRAM"""
        signature = "Adrian Szklarski"

        if self.screen_width <= 2048:
            self.positionX = CONST_SCREEN_WIDTH_LESS
            self.positionY = CONST_SCREEN_WIDTH_LESS / 2
        elif 2048 < self.screen_width < 4096:
            self.positionX = CONST_SCREEN_WIDTH_MORE
            self.positionY = CONST_SCREEN_HEIGHT_MORE / 2

        self.my_canvas.create_text(self.screen_width * self.positionX * 0.5, self.positionY + 80,
                                   text=title,
                                   font=("Helvetica", 40),
                                   justify='center', fill="white")

        self.my_canvas.create_text(self.screen_width * self.positionX * 0.5, self.positionY + 200,
                                   text=welcome,
                                   font=("Batang", 50),
                                   justify='center', fill="black")

        self.my_canvas.create_text(self.screen_width * self.positionX * 0.69, self.positionY + 290,
                                   text=signature,
                                   font=("Purisa", 20, 'italic'),
                                   justify='center', fill="black")

    def get_content(self):
        Contents(self.root)

    def get_buttons(self):
        """Method to add an in and out button on the front page"""
        # Positions of widget buttons
        _WIDTH = 400
        _HEIGHT = 250
        _X = 0.22
        _Y = 0.4

        # Position button
        if self.screen_width <= 2048:
            self._positionX = self.screen_width * _X
            self._positionY = self.screen_height * _Y
        elif 2048 < self.screen_width < 4096:
            self._positionX = self.screen_width * (_X / 2)
            self._positionY = self.screen_height * _Y

        # Photo to button
        photo_exit = Image.open("/home/adrian/Pulpit/my_application/photo/start_program.png")
        photo_start = Image.open("/home/adrian/Pulpit/my_application/photo/exit.png")

        image_exit = photo_exit.resize((_WIDTH, _HEIGHT), Image.ANTIALIAS)
        image_start = photo_start.resize((_WIDTH, _HEIGHT), Image.ANTIALIAS)

        image_exit.save(fp="/home/adrian/Pulpit/my_application/photo/start_programScale.png")
        image_start.save(fp="/home/adrian/Pulpit/my_application/photo/exitScale.png")

        exit_scale = tk.PhotoImage(file="/home/adrian/Pulpit/my_application/photo/start_programScale.png")
        start_scale = tk.PhotoImage(file="/home/adrian/Pulpit/my_application/photo/exitScale.png")

        # Add buttons
        button1 = tk.Button(text="Start program", borderwidth=5, image=exit_scale, fg='red',
                            font='Times 28 bold', compound="center", command=self.get_content)

        button2 = tk.Button(text="Exit", borderwidth=5, image=start_scale, fg='red',
                            font='Times 28 bold', compound="center", command=quit)

        # Dimensions and location of buttons
        self.my_canvas.create_window(self._positionX, self._positionY, anchor="nw", window=button1,
                                     height=_HEIGHT, width=_WIDTH)
        self.my_canvas.create_window(self._positionX + (self._positionY * 1.2), self._positionY, anchor="nw", window=button2,
                                     height=_HEIGHT, width=_WIDTH)

