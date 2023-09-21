from xlsx.read_xlsx_file import read_full_xlsx_file
from database.write_db_index import update_stock

def process_stock_file():
    try:
        data = read_full_xlsx_file('STOCKFILE')
        update_stock(data);
    except Exception as ex:
        print("Data could not be processed: \n", ex)

process_stock_file()
