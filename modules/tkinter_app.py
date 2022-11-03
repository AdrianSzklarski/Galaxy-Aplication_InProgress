from tkinter import Image
import tkinter as tk
from PIL import Image, ImageTk

CONST_SCREEN_HEIGHT_MORE = 0.85

CONST_SCREEN_WIDTH_MORE = 0.45

CONST_SCREEN_WIDTH_LESS = 0.9


class MainCodeOfApp:
    def __init__(self, root):
        """

        @rtype: object
        """
        self.frame = None
        self.root = root
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=0, column=0)

        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        print(self.screen_width, self.screen_height)

        # canvas
        self.my_canvas = tk.Canvas(self.frame, width=self.screen_width, height=self.screen_height, bg='white')
        self.my_canvas.grid()

        # calling modules
        self.get_settings_window()
        self.get_background()
        self.get_welcome()

    def get_settings_window(self):
        """
        The method sets the window parameters:
        - height;
        - width;
        and enters the application title
        @rtype: object
        """
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
        """/
        The method applies a background to the application:
        Input: global width and height of the monitor window
        Performs scaling and converting *.*jpg to *.*png
        Output: Canvas, Frame
        @rtype: object
        """
        link_of_background = r'/home/adrian/Pulpit/my_application/photo/'
        foto_background = Image.open(link_of_background + "photo1.jpg")
        image = foto_background.resize((self.screen_width, self.screen_height), Image.ANTIALIAS)
        image.save(fp=link_of_background + "background.png")
        self.bg = tk.PhotoImage(file=link_of_background + "background.png")
        self.my_canvas.create_image(0, 0, image=self.bg, anchor="nw")

    def get_welcome(self):
        #  Welcome text
        title = """Learning is easy, programming is easy"""
        welcome = """WELCOME TO MY PROGRAM"""
        signature = "Adrian Szklarski"

        if self.screen_width <= 2048:
            positionX = CONST_SCREEN_WIDTH_LESS
            positionY = CONST_SCREEN_WIDTH_LESS/2
        elif 2048 < self.screen_width < 4096:
            positionX = CONST_SCREEN_WIDTH_MORE
            positionY = CONST_SCREEN_HEIGHT_MORE/2


        self.my_canvas.create_text(self.screen_width * positionX * 0.5, positionY+80,
                                   text=title,
                                   font=("Helvetica", 40),
                                   justify='center', fill="white")

        self.my_canvas.create_text(self.screen_width * positionX  * 0.5, positionY+200,
                                   text=welcome,
                                   font=("Batang", 50),
                                   justify='center', fill="black")

        self.my_canvas.create_text(self.screen_width * positionX * 0.69, positionY+290,
                                   text=signature,
                                   font=("Purisa", 20, 'italic'),
                                   justify='center', fill="black")
    def get_buttons(self):
        pass
