
from controller.compare import compare
from model.csvreader import csv_reader
def numsum (filepath1, filepath2):
    #filepaths contain the same titles
    if not compare(filepath1, filepath2):
        return False
    result ={}
    content1 = csv_reader(filepath1)
    content2 = csv_reader(filepath2)
    for key in content1:
        for id in content1['Item_ID']:
            print(id)
    return 
    
