import pymysql

def get_connector():
    conn = pymysql.connect(
        host = "localhost",
        user = "root",
        password = "Niki321905jain",
        database = "sakila",
        port = 3306
    )
    return conn