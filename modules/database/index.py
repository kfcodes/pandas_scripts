from .stored_procedure import call_stored_procedure
from .write import write_to_database

def update_db(data):
    try:
        call_stored_procedure("STOREDPROCEDURE1");
        write_to_database(data, 'tpdb_table')
        call_stored_procedure("STOREDPROCEDURE2");
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)

def update_po(data):
    try:
        call_stored_procedure("STOREDPROCEDURE3");
        write_to_database(data, 'tpo_table')
        call_stored_procedure("STOREDPROCEDURE4");
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)

def update_poi(data):
    try:
        call_stored_procedure("STOREDPROCEDURE5");
        write_to_database(data, 'tpoi_table')
        call_stored_procedure("STOREDPROCEDURE6");
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)
