import mysql.connector as myconn

def connect():
    return myconn.connect(
        host='Localhost',
        user='root',
        password='Bharatpur2001',
        database='bank_system'
    )
