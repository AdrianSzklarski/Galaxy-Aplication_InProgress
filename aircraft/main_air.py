import tkinter as tk
from PIL import Image
from modules.main_window import MainApp


class Air:
    def __init__(self, root):
        self.root = root
        self.main = MainApp(self.root)
        self.my_canvas = self.main.my_canvas
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()
        self.get_buttons()

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
    app = Air(root)
    root.mainloop()