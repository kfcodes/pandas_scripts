from dotenv import load_dotenv
load_dotenv("../.env")

def process_stock_data(data):
    try:
        print(data)
    except Exception as ex:

        print("Data could not be processed: \n", ex)


