
def write_xlsx_file(data):
    try:
        data.to_excel("test.xlsx")
        print("Data was written to file")
    except Exception as ex:
        print("Could not write to file file: \n", ex)

