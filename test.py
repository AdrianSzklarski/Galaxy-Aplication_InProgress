import serial
import tkinter as tk

class SerialCode:
    def __init__(self, ser, root):
        self.ser = ser
        self.root = root

        self.get_code()

    def get_code(self):
        while True:
            data = self.ser .readline().decode("UTF-8")

            if data.find("H1: ") == 0:
                # Your code
                pass
            elif data.find("..") == 0:
                # Your code
                pass

    def get_window(self):
        # Kod of tkinter

if __name__ == '__main__':
    root = tk.Tk()
    app = SerialCode(serial.Serial('com7', 9600), root)

