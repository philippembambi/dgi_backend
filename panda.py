import pandas as pd
import json

df = pd.read_excel("file_example_XLS_10.xls", sheet_name="Sheet1")
# df = pd.read_excel("file_example_XLS_10.xls", sheet_name="Sheet1", usecols=['First Name', 'Gender'])

# Convert DataFrame into a list of dictionaries
dict_data = df.to_dict(orient="records")
with open("contribution.json", "w") as infile:
    json.dump(dict_data, infile, indent=3)