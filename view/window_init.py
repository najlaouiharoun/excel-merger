class WindowInit:
    def __init__(self, window):
        self.window = window
        self.window.title("csv Merger")
        self.window.minsize(width=200, height=200)
        self.window.geometry("400x400")