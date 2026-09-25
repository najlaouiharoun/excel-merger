import os
import tkinter as tk
from tkinter import filedialog

from controller.numsum import numsum
from controller.stupid_sum import stupid_sum

class WidgetHelper:
    def __init__(self,root):
        self._root = root
        self._files = []
        self._listbox = tk.Listbox(root, selectmode=tk.MULTIPLE)
        self._upload_button = tk.Button(root, text="Upload File", command=self.upload_file)
        self._label1 = tk.Label(root, text="please select two files to sum")
        self._label2= tk.Label(root, text="(optionnal) sort by common file id below:")
        self._label3 = tk.Label(root, text="please enter the output file name")
        self._label4 = tk.Label(root, text="welcome!")
        self._id_entry = tk.Entry(root)
        self._output_name_entry = tk.Entry(root)
        self._clear_button = tk.Button(root, text="Clear Selection", command=self.clear_file)
        self._submit_button = tk.Button(root, text="Start Merging", command=self.submit)
        
        self.create_widgets()
    def upload_file(self):
        file_path = filedialog.askopenfilename(title="select a file"
                                           ,filetypes=(("csv files", "*.csv")
                                                       , ("XML files", "*.xml")
                                                       , ("all files", "*.*")))
        if file_path:
            self._files.append(file_path)
            self._listbox.insert(self._listbox.size(), os.path.basename(file_path))
            self._label4.config(text = f"Uploaded file path: {file_path}")


            
    def create_widgets(self):
        self._upload_button.pack()
        self._listbox.pack()
        self._label2.pack()
        self._id_entry.pack()
        self._label3.pack()
        self._output_name_entry.pack()
        self._submit_button.pack()
        self._label4.pack()
        
    def get_selected_paths(self):
        indices = self._listbox.curselection()
        return [self._files[i] for i in indices ]
        
    def clear_file(self):
        self._files.clear()
        self._listbox.delete(0,tk.END)
    def submit (self):
        selected = self.get_selected_paths()
        if len(selected) != 2:
            self._label4.config(text="Please select exactly 2 files")
            return
        try:
            id_col= self._id_entry.get().strip()
            name= self._output_name_entry.get() or "result"
            self._label4.config(text=f"loading...")
            self._root.update()
            if id_col == "":
                state = stupid_sum(selected[0],selected[1],name)
            else:
                state = numsum(selected[0],selected[1],name,id_col)
            if state is False:
                self._label4.config(text=f"files don't match!") 
                 
                self._root.update()
            else:
                self._label4.config(text=f"✅ Merge complete!")
                self._root.update()

        except KeyError as e :
            self._label4.config(text=f"column {e} not found") 
            self._root.update()

        except Exception as e:
            self._label4.config(text=f"unknown error: {e}") 
            self._root.update()


