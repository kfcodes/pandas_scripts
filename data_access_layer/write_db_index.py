from .stored_procedure import call_stored_procedure
from .write import write_to_database

import os
from dotenv import load_dotenv
load_dotenv("../.env")

def write_to_database(data, name):
    try:
        data.to_sql(os.getenv(name), database_connection(),if_exists='append', index=False)
        print("Data was inserted into database")
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)

def update_db(data):
    try:
        call_stored_procedure("STOREDPROCEDURE1");
        write_to_database(data, 'DB')
        call_stored_procedure("STOREDPROCEDURE2");
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)

def update_po(data):
    try:
        call_stored_procedure("STOREDPROCEDURE3");
        write_to_database(data, 'PO')
        call_stored_procedure("STOREDPROCEDURE4");
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)

def update_poi(data):
    try:
        call_stored_procedure("STOREDPROCEDURE5");
        write_to_database(data, 'POI')
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)

def update_components(data):
    try:
        call_stored_procedure("STOREDPROCEDURE7");
        write_to_database(data, 'COMPONENT')
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)

def update_labels(data):
    try:
        call_stored_procedure("STOREDPROCEDURE8");
        write_to_database(data, 'LABEL')
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)

def update_schedule(data):
    try:
        write_to_database(data, 'SCHEDULE')
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)

def update_stock(data):
    try:
        call_stored_procedure("STOREDPROCEDURE11");
        write_to_database(data, 'SCHEDULE')
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)
