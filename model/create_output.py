import pandas as pd


def create_output(dict):
    frame = pd.DataFrame(dict)

    
    frame.to_csv("resources/output.csv", index=False)