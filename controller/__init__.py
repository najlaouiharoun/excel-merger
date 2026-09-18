

from controller.compare import compare
from model.csvreader import csv_reader


def numsum(filepath1, filepath2):
    if not compare(filepath1, filepath2):
        return False
    content1 = csv_reader(filepath1)
    content2 = csv_reader(filepath2)
    print(content1)
    print(content2)
    