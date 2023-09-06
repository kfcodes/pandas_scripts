from .read import read_select_to_dataframe

def get_production_documentation(id):
    try:

        select = "PRODUCTIONINFO"
        finished_product_info = read_select_to_dataframe(select, id)

        return(finished_product_info);

    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)


def get_product_components(id):
    try:

        select = "COMPONENTS"

        components = read_select_to_dataframe(select, id)

        return(components);

    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)
