import pandas as pd
from model.detect_encoding import detect_encoding

def csv_reader (file_path):
    try:
        content = pd.read_csv(file_path,dtype= str,encoding='utf-8-sig')
        content.columns = content.columns.str.strip()  # Remove whitespace from headers
        return content
    except UnicodeDecodeError:
        pass
    try:
        encod = detect_encoding(file_path)
        content = pd.read_csv(file_path,dtype=str,encoding = encod )
        content.columns = content.columns.str.strip()  # Remove whitespace from headers
        return content
    except (UnicodeDecodeError,LookupError):
        content = pd.read_csv(file_path, dtype=str, encoding='latin-1')
        content.columns = content.columns.str.strip()  # Remove whitespace from headers
        return content
            
