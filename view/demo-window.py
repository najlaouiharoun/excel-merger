from cProfile import label
import tkinter as tk
from tkinter import filedialog

def select_file(label):
    label.config(text="select 2 files") 
    
    
def uploadfile():
    file_path = filedialog.askopenfilename(title="select a file"
                                           ,filetypes=(("csv files", "*.csv")
                                                       , ("XML files", "*.xml")
                                                       , ("all files", "*.*")))
    if file_path:
        print(f"Uploaded file path: {file_path}")
        
def slection_change(event):
    selection = event.widget.curselection()
    if selection:
        index = selection[0]
         
    
        
window = tk.Tk()
window.title("csv Merger")
window.minsize(width=200, height=200)
window.geometry("400x400")
upload_button = tk.Button(window, text="Upload File", command= lambda: uploadfile())
upload_button.pack()
listbox = tk.Listbox(window)
listbox.bind("<<ListboxSelect>>", slection_change)
confirm_button = tk.Label(window, text="please select two files to sum",)
confirm_button.pack()

label = tk.Label(window, text="")

tk.Button(window, text="start merging", command=lambda: select_file(label)).pack()
label.pack()

window.mainloop()