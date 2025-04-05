import mysql.connector

def get_connector():
    conn = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "1234",
        database = "sakila",
        port = 3306
    )
    return conn