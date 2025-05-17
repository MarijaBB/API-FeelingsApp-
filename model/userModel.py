from config import *
from services.hash_password import hash_password
from datetime import datetime

def get_user_by_id(id):
    mydb =  mydb_connection()  
    mycursor = mydb.cursor()
    sql = "SELECT UserId, Username, Email, DATE_FORMAT(CreatedAt, '%d/%m/%Y') FROM Users WHERE UserId = %s"
    val = (id,)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchone()
    return myresult

def create_user(username, email, password):
    password_hash = hash_password(password) # ovo mozda treba u kontroleru
    mydb =  mydb_connection()
    mycursor = mydb.cursor()
    sql = 'INSERT INTO Users (UserName, Email, PasswordHash, CreatedAt) VALUES (%s,%s,%s,%s)'
    val = [(username, email, password_hash, datetime.now())]
    mycursor.executemany(sql, val)
    mydb.commit()
    

def delete_user_by_id(id):
    mydb =  mydb_connection()  
    mycursor = mydb.cursor()
    sql = """DELETE FROM Users
            WHERE userid = %s"""
    val = (id,)
    mycursor.execute(sql, val)
    mydb.commit()
