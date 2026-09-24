import tkinter as tk
from view.widget_helper import WidgetHelper   # adjust to wherever your class lives

def run_app():
    root = tk.Tk()
    root.title("CSV Merger")
    root.geometry("400x500")
    WidgetHelper(root)
    root.mainloop()

if __name__ == "__main__":
    run_app()