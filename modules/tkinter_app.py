from tkinter import Image
import tkinter as tk
from PIL import Image, ImageTk


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

        # canvas
        self.my_canvas = tk.Canvas(self.frame, width=self.screen_width, height=self.screen_height, bg='white')
        self.my_canvas.grid()

        # calling modules
        self.get_settings_window()
        self.get_background()

    def get_settings_window(self):
        """
        The method sets the window parameters:
        - height;
        - width;
        and enters the application title
        @rtype: object
        """
        self.root.title("Task Application by Adrian Szklarski, 2022")
        self.root.geometry(f"{self.screen_width}x{self.screen_height}")

    def get_background(self):
        """
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


