import mysql.connector
def mydb_connection():
    try:
        mydb = mysql.connector.connect(
                host="localhost",
                user="",     # not showing publicly
                password="", # not showing publicly
                database = "feelDB",
                auth_plugin="mysql_native_password"
            )
        return mydb
    except mysql.connector.Error as err:
        raise RuntimeError(f"Database connection failed: {err}")
    
mydb_connection()