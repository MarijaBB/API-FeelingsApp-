from datetime import datetime
from config import *


def get_history_for_user(userId):
    mydb =  mydb_connection()  
    mycursor = mydb.cursor()
    sql = "SELECT userId, FeelingId, DATE_FORMAT(CreatedAt, '%d/%m/%Y') FROM History WHERE userId = %s"
    val = (userId,)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchall()
    return [f for f in myresult]

def create_history_input(userId,feelingId):
    mydb =  mydb_connection()
    mycursor = mydb.cursor()
    sql = 'INSERT INTO History (UserId, FeelingId, CreatedAt) VALUES (%s,%s,%s)'
    val = [(userId, feelingId, datetime.now())]
    mycursor.executemany(sql, val)

    mydb.commit()


def delete_history_entry_by_id(id):
    mydb =  mydb_connection()  
    mycursor = mydb.cursor()
    sql = """DELETE FROM History
            WHERE historyid = %s"""
    val = (id,)
    mycursor.execute(sql, val)
    mydb.commit()

def delete_history_entries_for_user(userid):
    mydb =  mydb_connection()  
    mycursor = mydb.cursor()
    sql = """DELETE FROM History
            WHERE userid = %s"""
    val = (userid,)
    mycursor.execute(sql, val)
    mydb.commit()
