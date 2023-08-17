from connect import database_connection as db

def call_stored_procedure():
    try:
        connection = db().raw_connection()
        cursor = connection.cursor()
        cursor.execute('Call storedProcedure();');
        cursor.close()
        connection.commit()
    except Exception as ex:
        print("Connection could not be made due to the following error: \n", ex)


call_stored_procedure();
