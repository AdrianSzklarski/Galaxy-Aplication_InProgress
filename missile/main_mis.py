import tkinter as tk
from PIL import Image
from modules.main_window import MainApp

class Missile:
    def __init__(self, root):
        self.root = root
        self.main = MainApp(self.root)
        self.my_canvas = self.main.my_canvas
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        self.get_buttons()
        self.get_list()

    def get_test_function(self):
        self.test = print('Test Button')

    def get_list(self):
        # Positions of widget buttons
        _WIDTH = 300
        _HEIGHT = 100
        _X = 0.04
        _Y = 0.07

        # Position button
        if self.screen_width <= 2048:
            self._positionX = self.screen_width * _X
            self._positionY = self.screen_height * _Y
        elif 2048 < self.screen_width < 4096:
            self._positionX = self.screen_width * (_X / 2)
            self._positionY = self.screen_height * _Y

        # Add buttons
        button1 = tk.Button(text="Engineering", borderwidth=5, fg='red',
                            font='Times 28 bold', compound="center", command=self.get_test_function)

        button2 = tk.Button(text="Programming", borderwidth=5, fg='red',
                            font='Times 28 bold', compound="center", command=self.get_test_function)

        button3 = tk.Button(text="Missile", borderwidth=5, fg='red',
                            font='Times 28 bold', compound="center", command=self.get_test_function)

        button4 = tk.Button(text="Aircraft", borderwidth=5, fg='red',
                            font='Times 28 bold', compound="center", command=self.get_test_function)

        button5 = tk.Button(text="Games", borderwidth=5, fg='red',
                            font='Times 28 bold', compound="center", command=self.get_test_function)

        # Dimensions and location of buttons
        self.my_canvas.create_window(self._positionX, self._positionY, anchor="nw", window=button1,
                                     height=_HEIGHT, width=_WIDTH)
        self.my_canvas.create_window(self._positionX, self._positionY*3, anchor="nw", window=button2,
                                     height=_HEIGHT, width=_WIDTH)
        self.my_canvas.create_window(self._positionX, self._positionY*5, anchor="nw", window=button3,
                                     height=_HEIGHT, width=_WIDTH)
        self.my_canvas.create_window(self._positionX, self._positionY*7, anchor="nw", window=button4,
                                     height=_HEIGHT, width=_WIDTH)
        self.my_canvas.create_window(self._positionX, self._positionY*9, anchor="nw", window=button5,
                                     height=_HEIGHT, width=_WIDTH)

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

        image_exit = btn_exit.resize((_WIDTH_SMALL, _HEIGHT_SMALL), Image.ANTIALIAS)

        image_exit.save(fp="/home/adrian/Pulpit/my_application/photo/small_exitScale.png")

        btn_exit = tk.PhotoImage(file="/home/adrian/Pulpit/my_application/photo/small_exitScale.png")

        exit_btn = tk.Button(borderwidth=1, image=btn_exit, command=quit)

        self.my_canvas.create_window(self._positionX*21.2, self._positionY*11, anchor="nw", window=exit_btn,
                                     height=60, width=60)


if __name__=='__main__':
    root = tk.Tk()
    app = Missile(root)
    root.mainloop()