from xlsx.read_xlsx_file import read_full_xlsx_file
from process_data.process_stock_data import process_stock_data
from database.write_db_index import update_stock

def process_stock_file():
    try:
        data = read_full_xlsx_file('STOCKFILE')
        processed_data = process_stock_data(data);
        update_stock(processed_data);
    except Exception as ex:
        print("Data could not be processed: \n", ex)

process_stock_file()
