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
        airButton = tk.Menu(file_menu, tearoff=0)
        arduinoButton = tk.Menu(file_menu, tearoff=0)
        engineeringButton = tk.Menu(file_menu, tearoff=0)
        gamesButton = tk.Menu(file_menu, tearoff=0)
        missileButton = tk.Menu(file_menu, tearoff=0)
        programmingButton = tk.Menu(file_menu, tearoff=0)
        recruitingTasksButton = tk.Menu(file_menu, tearoff=0)
        techButton = tk.Menu(file_menu, tearoff=0)
        helpmenu = tk.Menu(file_menu, tearoff=0)

        file_menu.add_cascade(label="File", menu=filemenu)

        # file
        filemenu.add_command(label="New")
        filemenu.add_command(label="Save")
        filemenu.add_command(label="Save as...")
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=quit)

        # air
        file_menu.add_cascade(label="Aircraft", menu=airButton)
        airButton.add_command(label="Aerodynamics --LOCKED--", command=self.get_air)
        airButton.add_command(label="Flight dynamics --LOCKED--", command=self.get_air)
        airButton.add_command(label="Automation and control --LOCKED--", command=self.get_air)
        airButton.add_command(label="Projects --LOCKED--", command=self.get_air)

        # arduino
        file_menu.add_cascade(label="Arduino", menu=arduinoButton)
        arduinoButton.add_command(label="--LOCKED--", command=self.get_arduino)
        arduinoButton.add_command(label="--LOCKED--", command=self.get_arduino)
        arduinoButton.add_command(label="--LOCKED--", command=self.get_arduino)
        arduinoButton.add_command(label="--LOCKED--", command=self.get_arduino)
        arduinoButton.add_command(label="--LOCKED--", command=self.get_arduino)

        # engineering
        file_menu.add_cascade(label="Engineering", menu=engineeringButton)
        engineeringButton.add_command(label="Mathematics --LOCKED--", command=self.get_engineering)
        engineeringButton.add_command(label="Mechanics --LOCKED--", command=self.get_engineering)
        engineeringButton.add_command(label="Fluid mechanics --LOCKED--", command=self.get_engineering)
        engineeringButton.add_command(label="Aerodynamics --LOCKED--", command=self.get_engineering)
        engineeringButton.add_command(label="Automation and control --LOCKED--", command=self.get_engineering)
        engineeringButton.add_command(label="Thermodynamics --LOCKED--", command=self.get_engineering)
        engineeringButton.add_command(label="Physics --LOCKED--", command=self.get_engineering)

        # games
        file_menu.add_cascade(label="Games", menu=gamesButton)
        gamesButton.add_command(label="--LOCKED--", command=self.get_games)
        gamesButton.add_command(label="--LOCKED--", command=self.get_games)
        gamesButton.add_command(label="--LOCKED--", command=self.get_games)
        gamesButton.add_command(label="--LOCKED--", command=self.get_games)
        gamesButton.add_command(label="--LOCKED--", command=self.get_games)

        # missile
        file_menu.add_cascade(label="Missile", menu=missileButton)
        missileButton.add_command(label="Aerodynamics --LOCKED--", command=self.get_missile)
        missileButton.add_command(label="Flight dynamics --LOCKED--", command=self.get_missile)
        missileButton.add_command(label="Ballistics --LOCKED--", command=self.get_missile)
        missileButton.add_command(label="Rocket propulsion --LOCKED--", command=self.get_missile)
        missileButton.add_command(label="Automation and control --LOCKED--", command=self.get_missile)
        missileButton.add_command(label="Projects --LOCKED--", command=self.get_missile)

        # programming
        file_menu.add_cascade(label="Programming", menu=programmingButton)
        programmingButton.add_command(label="Basic level --LOCKED--", command=self.get_programming)
        programmingButton.add_command(label="Intermediate level  --LOCKED--", command=self.get_programming)
        programmingButton.add_command(label="Advanced level --LOCKED--", command=self.get_programming)
        programmingButton.add_command(label="Master level --LOCKED--", command=self.get_programming)
        programmingButton.add_command(label="Specialized level --LOCKED--", command=self.get_programming)

        # recruitingTasks
        file_menu.add_cascade(label="Recruiting", menu=recruitingTasksButton)
        recruitingTasksButton.add_command(label="--LOCKED--", command=self.get_recruiting)
        recruitingTasksButton.add_command(label="--LOCKED--", command=self.get_recruiting)
        recruitingTasksButton.add_command(label="--LOCKED--", command=self.get_recruiting)
        recruitingTasksButton.add_command(label="--LOCKED--", command=self.get_recruiting)
        recruitingTasksButton.add_command(label="--LOCKED--", command=self.get_recruiting)

        # tech&Python
        file_menu.add_cascade(label="Technology", menu=techButton)
        techButton.add_command(label="--LOCKED--", command=self.get_tech)
        techButton.add_command(label="--LOCKED--", command=self.get_tech)
        techButton.add_command(label="--LOCKED--", command=self.get_tech)
        techButton.add_command(label="--LOCKED--", command=self.get_tech)
        techButton.add_command(label="--LOCKED--", command=self.get_tech)


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
