from .read import read_select_to_dataframe

def read_production_documentation(id):
    try:

        select = "TEST"
        data = read_select_to_dataframe(select, id)

        return(data);

    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)
