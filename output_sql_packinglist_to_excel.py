from os import wait
import requests
import pandas as pd

# The API endpoint that I want to hit to get the packing list data
# api-endpoint
URL = "Test"
r = requests.get(url = URL)
data = r.json()
df = pd.json_normalize(data)

selected_columns.to_excel("packing_list.xlsx")
print("The packing list was outputted to the file")
