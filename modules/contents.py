from modules.small_buttons import SmallButtons
from tech.main_tech import Tech
from aircraft.main_air import Air
from arduino.main_adruino import Arduino
from engineering.main_eng import Engineering
from games.main_game import Games
from missile.main_mis import Missile
from modules.main_window import MainApp
import tkinter as tk
from programming.main_prog import Programming
from recruiting.main_rt import Recruiting

class Contents:
    def __init__(self, root):
        self.root = root
        self.main = MainApp(self.root)
        self.my_canvas = self.main.my_canvas

        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()

        SmallButtons(self.root)
        self.get_menu()

    def get_menu(self):
        menu = tk.Menu(self.root)
        file_menu = tk.Menu(menu)
        self.root.config(menu=file_menu)

        filemenu = tk.Menu(file_menu, tearoff=0)
        helpmenu = tk.Menu(file_menu, tearoff=0)

        file_menu.add_cascade(label="File", menu=filemenu)

        # File
        filemenu.add_command(label="New")
        filemenu.add_command(label="Save")
        filemenu.add_command(label="Save as...")

        # Image
        file_menu.add_command(label="Aircraft", command=self.get_air)
        file_menu.add_command(label="Arduino&Python", command=self.get_arduino)
        file_menu.add_command(label="Engineering", command=self.get_engineering)
        file_menu.add_command(label="Games", command=self.get_games)
        file_menu.add_command(label="Missile", command=self.get_missile)
        file_menu.add_command(label="Programming", command=self.get_programming)
        file_menu.add_command(label="RecruitingTasks", command=self.get_recruiting)
        file_menu.add_command(label="tech&Python", command=self.get_tech)

        # Help
        file_menu.add_cascade(label="Help", menu=helpmenu)
        helpmenu.add_command(label="About program")
        helpmenu.add_command(label="About...")

    def get_air(self):
        Air(self.root)

    def get_arduino(self):
        Arduino(self.root)

    def get_engineering(self):
        Engineering(self.root)

    def get_games(self):
        Games(self.root)

    def get_missile(self):
        Missile(self.root)

    def get_programming(self):
        Programming(self.root)

    def get_recruiting(self):
        Recruiting(self.root)

    def get_tech(self):
        Tech(self.root)

if __name__ == '__main__':
    """The main program call"""
    root = tk.Tk()
    app = Contents(root)
    root.mainloop()
