import tkinter as tk
from modules.main_window import MainApp
from modules.small_buttons import SmallButtons


class Arduino:
    def __init__(self, root):
        self.root = root
        self.main = MainApp(self.root)
        self.my_canvas = self.main.my_canvas
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        SmallButtons(self.root)
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
        button1 = tk.Button(text="--LOCKED--", borderwidth=5, fg='red',
                            font='Times 28 bold', compound="center", command=self.get_test_function)

        button2 = tk.Button(text="--LOCKED--", borderwidth=5, fg='red',
                            font='Times 28 bold', compound="center", command=self.get_test_function)

        button3 = tk.Button(text="--LOCKED--", borderwidth=5, fg='red',
                            font='Times 28 bold', compound="center", command=self.get_test_function)

        button4 = tk.Button(text="--LOCKED--", borderwidth=5, fg='red',
                            font='Times 28 bold', compound="center", command=self.get_test_function)

        button5 = tk.Button(text="--LOCKED--", borderwidth=5, fg='red',
                            font='Times 28 bold', compound="center", command=self.get_test_function)

        # Dimensions and location of buttons
        self.my_canvas.create_window(self._positionX, self._positionY, anchor="nw", window=button1,
                                     height=_HEIGHT, width=_WIDTH)
        self.my_canvas.create_window(self._positionX, self._positionY * 3, anchor="nw", window=button2,
                                     height=_HEIGHT, width=_WIDTH)
        self.my_canvas.create_window(self._positionX, self._positionY * 5, anchor="nw", window=button3,
                                     height=_HEIGHT, width=_WIDTH)
        self.my_canvas.create_window(self._positionX, self._positionY * 7, anchor="nw", window=button4,
                                     height=_HEIGHT, width=_WIDTH)
        self.my_canvas.create_window(self._positionX, self._positionY * 9, anchor="nw", window=button5,
                                     height=_HEIGHT, width=_WIDTH)

if __name__=='__main__':
    root = tk.Tk()
    app = Arduino(root)
    root.mainloop()