from controller.numsum import numsum

import pandas as pd
from model.csv_reader import csv_reader

# Force Pandas to show everything
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 200)

content2 = csv_reader("resources/file2.csv")

print("Total rows:", len(content2))
print("Columns:", content2.columns.tolist())
print("Item_ID dtype:", content2['Item_ID'].dtype)
print("All Item_ID values:", content2['Item_ID'].tolist())
print()
print("=== Full DataFrame ===")
print(content2)
print()
print("Is 'amugus' present?", 'amugus' in content2['Item_ID'].astype(str).values)