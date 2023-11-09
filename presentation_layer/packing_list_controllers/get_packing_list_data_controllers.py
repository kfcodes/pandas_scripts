from ...data_access_layer.read_database_functions import read_selected_data_to_dataframe


def get_all_packing_lists():

    try:

        # Read the data from the database
        packing_lists = read_data('DBFILE')

        # Processs the data into html
        html_data = data_html(packing_lists);

        return(html_data);

    except Exception as ex:
        print("Data could not be processed: \n", ex)
