from physical_layer.data_access_layer.database_connection import database_connection as db

import os
from dotenv import load_dotenv
load_dotenv(".env")

def call_stored_procedure(procedure):
    try:
        connection = db().raw_connection()
        cursor = connection.cursor()
        cursor.execute(os.getenv(procedure));
        cursor.close()
        connection.commit()
        print("Called the stored function")
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)
