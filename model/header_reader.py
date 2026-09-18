import pandas as pd 

def header_reader (filepath):
    titles = pd.read_csv(filepath, nrows=1).columns.tolist()
    return titles
    
