from config import *
from model.feelingsModel import get_feelingId

def get_messages():
    mydb =  mydb_connection()  
    mycursor = mydb.cursor()
    sql = 'SELECT * FROM Messages'
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return [f for f in myresult]

def get_messages_for_feeling_name(feeling_name):
    mydb =  mydb_connection()  
    mycursor = mydb.cursor()
    feeling_id = get_feelingId(feeling_name)
    sql = 'SELECT * FROM Messages WHERE feelingId = %s'
    val = (feeling_id,)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    return [f for f in myresult]

def create_message(message, feelingName):
    mydb =  mydb_connection()
    mycursor = mydb.cursor()
    sql = 'INSERT INTO Messages (message, feelingId) VALUES (%s,%s)'
    val = [(message, get_feelingId(feelingName))]
    mycursor.executemany(sql, val)
    mydb.commit()

def change_message_for_id(message, id):
    mydb =  mydb_connection()  
    mycursor = mydb.cursor()
    sql = """UPDATE messages
            SET message = %s
            WHERE messageid = %s"""
    val = [(message, id)]
    mycursor.executemany(sql, val)
    mydb.commit()


def delete_message_by_id(id):
    mydb =  mydb_connection()  
    mycursor = mydb.cursor()
    sql = """DELETE FROM Messages
            WHERE messageid = %s"""
    val = (id,)
    mycursor.execute(sql, val)
    mydb.commit()
