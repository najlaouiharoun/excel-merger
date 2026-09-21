
from controller.compare import compare
from model.csv_reader import csv_reader
import pandas as pd
def numsum (filepath1, filepath2):
    #filepaths contain the same titles
    if not compare(filepath1, filepath2):
        return False
    #read the content of the files
    result ={}
    content1 = csv_reader(filepath1)
    content2 = csv_reader(filepath2)
    
  
    #combining content dataframes by id
    combined_df =pd.concat([content1, content2], ignore_index=True) 
    #combining the dupe ids in the dataframe and summing the values of the other columns 
    result = combined_df.groupby('Item_ID', as_index=False).sum()

    result.to_csv('resources/output.csv', index=False)
    return result 
    
