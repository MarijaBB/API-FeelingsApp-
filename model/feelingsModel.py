from config import *

def get_feelings():
    mydb = mydb_connection()  
    mycursor = mydb.cursor()
    sql = 'SELECT * FROM Feelings'
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    return [f for f in myresult]

def get_feeling(id):
    mydb =  mydb_connection()  
    mycursor = mydb.cursor()
    sql = 'SELECT * FROM Feelings WHERE FeelingId = %s'
    val = (id,)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchone()
    return myresult

def new_feeling(feeling_name, image_file, color_code):
    mydb =  mydb_connection()  
    mycursor = mydb.cursor()
    sql = 'INSERT INTO Feelings (FeelingName, Image, ColorCode) VALUES(%s,%s,%s)'
    val = [(feeling_name, image_file, color_code)]
    mycursor.executemany(sql, val)
    mydb.commit()
    return mycursor.lastrowid

def update_feeling(feeling_id, feeling_name_new, image_file_new, color_new):
    mydb =  mydb_connection()  
    mycursor = mydb.cursor()
    sql = """UPDATE feelings
            SET feelingname = %s, image = %s, colorcode = %s
            WHERE feelingid = %s"""
    val = [(feeling_name_new, image_file_new, color_new, feeling_id)]
    mycursor.executemany(sql, val)
    mydb.commit()

def change_feeling_name(feeling_id, feeling_name_new):
    mydb =  mydb_connection()  
    mycursor = mydb.cursor()
    sql = """UPDATE feelings
            SET feelingname = %s
            WHERE feelingid = %s"""
    val = [(feeling_name_new, feeling_id)]
    mycursor.executemany(sql, val)
    mydb.commit()

def change_feeling_color(feeling_id, color):
    mydb =  mydb_connection()  
    mycursor = mydb.cursor()
    sql = """UPDATE feelings
            SET colorcode = %s
            WHERE feelingid = %s"""
    val = [(color, feeling_id)]
    mycursor.executemany(sql, val)
    mydb.commit()

def change_feeling_icon(feeling_id, icon):
    mydb =  mydb_connection()  
    mycursor = mydb.cursor()
    sql = """UPDATE feelings
            SET image = %s
            WHERE feelingid = %s"""
    val = [(icon, feeling_id)]
    mycursor.executemany(sql, val)
    mydb.commit()

def delete_feeling_by_id(feeling_id):
    mydb =  mydb_connection()  
    mycursor = mydb.cursor()
    sql = """DELETE FROM Feelings
            WHERE feelingid = %s"""
    val = (feeling_id,)
    mycursor.execute(sql, val)
    mydb.commit()

def get_feelingId(feelingName):
    mydb =  mydb_connection()  
    mycursor = mydb.cursor()
    sql = 'SELECT FeelingId FROM Feelings WHERE FeelingName=%s'
    val = (feelingName,)
    mycursor.execute(sql,val)
    myresult = mycursor.fetchone()
    return myresult[0]
