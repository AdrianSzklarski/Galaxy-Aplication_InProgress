import tkinter as tk
class Games:
    def __init__(self, root):
        self.root = root

        self.get_test()

    def get_test(self):
        label = tk.Label(self.root, text='Welcome in the games')
        label.pack(ipadx=10, ipady=10)

if __name__=='__main__':
    root = tk.Tk()
    app = Games(root)
    root.mainloop()