import pandas as pd 

def csv_reader (filepath):
    content = pd.read_csv(filepath,dtype={"Item_ID": str})
    content.columns = content.columns.str.strip()  # Remove whitespace from headers
    return content
    
