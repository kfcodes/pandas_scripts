import requests
from process_data.process_packing_list_data import process_data
from .xlsx.write_file import write_xlsx_file

URL = "test"
r = requests.get(url = URL)
data = r.json()
new_data = process_data(data)
write_xlsx_file(new_data)

