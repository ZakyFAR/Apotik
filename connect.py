#bulid in
import mysql.connector

#fungsi koneksi
def koneksi():
    db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        passwd = "",
        database = "periksa_mata",
        autocommit = True
    )

    if db.is_connected():
        return db
    else:
        print('DB disconnect!')
