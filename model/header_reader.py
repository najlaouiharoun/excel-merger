import pandas as pd 
from model.detect_encoding import detect_encoding
def header_reader (file_path):
    
    try:
        titles = pd.read_csv(file_path, nrows=1,dtype=str,encoding='utf-8-sig').columns.tolist()
        return titles
    except UnicodeDecodeError:
        pass
    try:
        encod = detect_encoding(file_path)
        titles = pd.read_csv(file_path, nrows=1,dtype=str,encoding = encod).columns.tolist()
        return titles
    except (UnicodeDecodeError,LookupError):
        titles = pd.read_csv(file_path, nrows=1,dtype=str,encoding = 'latin-1').columns.tolist()
        return titles  
    
