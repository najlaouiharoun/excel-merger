
from model.header_reader import header_reader
def compare (filepath1, filepath2):
    titles1 = header_reader(filepath1)
    titles2 = header_reader(filepath2)
    return set(titles1) == set(titles2)
    

