from tkinter import Image
import tkinter as tk
from PIL import Image

CONST_SCREEN_HEIGHT_MORE = 0.85

CONST_SCREEN_WIDTH_MORE = 0.45

CONST_SCREEN_WIDTH_LESS = 0.9


class MainApp:
    """A class that adds a background to a program"""
    def __init__(self, root):
        self.frame = None
        self.root = root
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=0, column=0)

        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()

        # calling modules
        self.get_background()
        self.get_settings_window()

    def get_canvas(self):
        self.my_canvas = tk.Canvas(self.frame, width=self.screen_width, height=self.screen_height, bg='white')
        self.my_canvas.grid()
        return self.my_canvas

    def get_settings_window(self):
        """
        The method sets the window parameters:
        - height;
        - width;
        and enters the application title
        """
        # Adjusting the window size to the screen
        self.root.title("Task Application by Adrian Szklarski, 2022")
        if self.screen_width <= 2048:
            self.root.geometry(
                f"{round(self.screen_width * CONST_SCREEN_WIDTH_LESS)}x{round(self.screen_height * CONST_SCREEN_WIDTH_LESS)}")
        elif 2048 < self.screen_width < 4096:
            self.root.geometry(
                f"{round(self.screen_width * CONST_SCREEN_WIDTH_MORE)}x{round(self.screen_height * CONST_SCREEN_HEIGHT_MORE)}")
        else:
            print('Change your monitor resolution below 4096px')

        self.root.resizable(False, False)

    def get_background(self):
        """
        The method applies a background to the application:
        Input: global width and height of the monitor window
        Performs scaling and converting *.*jpg to *.*png
        Output: Canvas, Frame
        """
        link_of_background = r'/home/adrian/Pulpit/my_application/photo/'
        foto_background = Image.open(link_of_background + "photo1.jpg")
        image = foto_background.resize((self.screen_width, self.screen_height), Image.ANTIALIAS)
        image.save(fp=link_of_background + "background.png")
        self.bg = tk.PhotoImage(file=link_of_background + "background.png")
        self.get_canvas().create_image(0, 0, image=self.bg, anchor="nw")

