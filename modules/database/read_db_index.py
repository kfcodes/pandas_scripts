from .read import read_to_dataframe

def read_production_documentation(id):
    try:

        data = read_to_dataframe(id)
        return(data);

    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)
