
from controller.compare import compare
from model.create_output import create_output
from model.csv_reader import csv_reader
import pandas as pd
def numsum (filepath1, filepath2,file_name,shared_id="Item_ID", ):
    #filepaths contain the same titles
    if not compare(filepath1, filepath2):
        return False
    #read the content of the files
    result ={}
    content1 = csv_reader(filepath1)
    content2 = csv_reader(filepath2)
    content1[shared_id] = content1[shared_id].astype(str).replace('nan', None)
    content2[shared_id] = content2[shared_id].astype(str).replace('nan', None)
    print (content2)
    #combining content dataframes by id
    merged_dataframes =pd.merge(content1, content2,on=shared_id,how = "outer", suffixes=('_1', '_2')) 
    result = {shared_id: merged_dataframes[shared_id]}
    #getting columns other than id
    columns = content1.columns.drop(shared_id)
    #combining the non id dataframe data and summing the values of summable columns
    for column in columns:
        c1_df_merge = pd.to_numeric(merged_dataframes[f'{column}_1'], errors='coerce')
        c2_df_merge = pd.to_numeric(merged_dataframes[f'{column}_2'], errors='coerce') 
        # catching safe columns and excluding non numeric columns
        both_nums = c1_df_merge.notna() & c2_df_merge.notna()
        summed_col = c2_df_merge + c1_df_merge
        # If File 2 is NaN, use File 1's value
        file2_val = merged_dataframes[f'{column}_2']
        file1_val = merged_dataframes[f'{column}_1']
        final_col = file2_val.astype(object).copy()
        final_col[file2_val.isna()] = file1_val[file2_val.isna()]
        #now we sum the safe columns where there are numbers
        final_col[both_nums] = summed_col[both_nums]
        result[column] = final_col
    result_df = pd.DataFrame(result)
    create_output(result_df,file_name)
    return result_df
    
