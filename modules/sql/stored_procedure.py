from dotenv import load_dotenv
load_dotenv(".env")
from connect import database_connection
import sqlalchemy as sqlalchemy


def call_stored_procedure():
    try:
        cursor = database_connection().raw_connection().cursor();
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)


call_stored_procedure();
