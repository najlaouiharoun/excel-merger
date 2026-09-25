
import pandas as pd

from controller.round_if_num import _round_if_num
from model.create_output import create_output
from model.csv_reader import csv_reader
def stupid_sum(filepath1, filepath2, file_name):
    content1 = csv_reader(filepath1)
    content2 = csv_reader(filepath2)
    
    names1 = list(content1.columns)
    names2 = list(content2.columns)
    rows = max(len(content1), len(content2))
    cols = max(len(names1), len(names2))
    
    # Pad both to the same shape, with integer column labels
    content1.columns = range(len(names1))
    content2.columns = range(len(names2))
    content1 = content1.reindex(index=range(rows), columns=range(cols))
    content2 = content2.reindex(index=range(rows), columns=range(cols))
    
    # Now they're guaranteed the same shape. Direct element-wise combine:
    n1 = content1.apply(pd.to_numeric, errors='coerce')
    n2 = content2.apply(pd.to_numeric, errors='coerce')
    null1 = content1.isna()
    null2 = content2.isna()
    
    result_df = content2.astype(object)
    result_df[null2 & ~null1] = content1[null2 & ~null1]
    both_num = n1.notna() & n2.notna()
    result_df[both_num] = n1[both_num] + n2[both_num]
    
    # Restore names
    result_df.columns = [names1[i] if i < len(names1) else names2[i] for i in range(cols)]
    result_df = result_df.map(_round_if_num)
    create_output(result_df, file_name)
    return result_df