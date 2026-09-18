import pandas as pd 

def csv_reader (filepath):
    content = pd.read_csv(filepath).to_dict()
    return content
    
