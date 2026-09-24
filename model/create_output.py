import pandas as pd


def create_output(frame, file_name):

    
    frame.to_csv(f"resources/{file_name}.csv", index=False)