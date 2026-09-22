import tkinter as tk
from tkinter import MULTIPLE, filedialog


def submit(label):
    selected = [listbox.get(i) for i in listbox.curselection()]
    if len(selected) != 2:
        label.config(text="Please select exactly 2 files")
    else:
        label.config(text=f"Selected: {selected[0]} and {selected[1]}")    
    
def add_file_to_listbox(file_path):
    listbox.insert(listbox.size(), file_path)
    
    
def uploadfile():
    file_path = filedialog.askopenfilename(title="select a file"
                                           ,filetypes=(("csv files", "*.csv")
                                                       , ("XML files", "*.xml")
                                                       , ("all files", "*.*")))
    if file_path:
        add_file_to_listbox(file_path)
        print(f"Uploaded file path: {file_path}")
        
def selection_change(event):
    if len(listbox.curselection()) > 2:
        selected = listbox.curselection()
        for i in selected[:-2]:
            
            listbox.selection_clear(i)
    
    
         
    
        
window = tk.Tk()
window.title("csv Merger")
window.minsize(width=200, height=200)
window.geometry("400x400")
upload_button = tk.Button(window, text="Upload File", command = uploadfile)
upload_button.pack()
listbox = tk.Listbox(window, selectmode = MULTIPLE)
listbox.bind("<<ListboxSelect>>", selection_change)
listbox.pack()
assist_label = tk.Label(window, text = "please select two files to sum",)
assist_label.pack()

return_message = tk.Label(window, text = "")

confitm_button = tk.Button(window, text="start merging", command = lambda: submit(return_message))
confitm_button.pack()
return_message.pack()

window.mainloop()