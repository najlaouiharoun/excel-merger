import pandas as pd


def create_output(frame):

    
    frame.to_csv("resources/output.csv", index=False)