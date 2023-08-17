import os
from dotenv import load_dotenv
load_dotenv("../../.env")
from .connect import database_connection as db

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


