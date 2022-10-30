class MainCodeOfApp:
    def __init__(self, root):
        """

        @rtype: object
        """
        self.frame = None
        self.root = root
        self.screen_width = root.winfo_screenwidth()
        self.screen_height = root.winfo_screenheight()

        # calling modules
        self.get_settings_window()

    def get_settings_window(self):
        """

        @rtype: object
        """
        self.root.title("Task Application by Adrian Szklarski, 2022")
        self.root.geometry(f"{self.screen_width}x{self.screen_height}")


