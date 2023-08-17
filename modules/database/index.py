from .stored_procedure import call_stored_procedure
from .write import write_to_database

def updateDB(data):
    try:
        call_stored_procedure("STOREDPROCEDURE1");
        write_to_database(data, 'tpdb_table')
        call_stored_procedure("STOREDPROCEDURE2");
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)
