import mysql.connector
import connect
db = connect.koneksi()
#menambah data
def add(data):
    cursor = db.cursor()
    sql = """INSERT INTO pemeriksaan_mata (tanggal,nama,mata_kanan, mata_kiri,jenis_kacamata,lain_lain) VALUES (%s, %s, %s, %s, %s, %s)"""
    cursor.execute(sql, data)
    db.commit()
    print(' Data member berhasil ditambahkan!'.format(cursor.rowcount))

#Menampilkan seluruh data
def show():
    cursor = db.cursor()
    sql = """SELECT * FROM pemeriksaan_mata"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    print("|id|    Tanggal    | NAMA |Data Mata Kiri\t|Data Mata Kanan\t|\t\tJenis kacamata\t\t|\tLain Lain\t|")
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    for data in results:
        print("|",data[0],"|",data[1],"\t|",data[2],"|",data[3],"\t\t|",data[4],"\t\t\t|",data[5],"\t|",data[6],"\t\t|")
        print("-----------------------------------------------------------------------------------------------------------------------------------------")
#Menghapus data dari tabel member
def delete(data):
    cursor = db.cursor()
    sql = """DELETE FROM pemeriksaan_mata WHERE id=%s"""
    cursor.execute(sql, id)
    db.commit()
    print(' Data berhasil dihapus!'.format(cursor.rowcount))
    
#Mengubah data mata
def edit(data):
    cursor = db.cursor()
    sql = """UPDATE pemeriksaan_mata SET mata_kanan= %s, mata_kiri=%s, jenis_kacamata=%s WHERE nama=%s"""
    cursor.execute(sql, data)
    db.commit()
    print(' Data Mata berhasil diubah!'.format(cursor.rowcount))


#Mencari data tertentu
def search(data):
    cursor = db.cursor()
    sql = """SELECT * FROM pemeriksaan_mata WHERE nama=%s"""
    cursor.execute(sql,data)
    results = cursor.fetchall()
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    print("|id|    Tanggal    | NAMA |Data Mata Kiri\t|Data Mata Kanan\t|\t\tJenis kacamata\t\t|\tLain Lain\t|")
    print("-----------------------------------------------------------------------------------------------------------------------------------------")
    for data in results:
        print("|",data[0],"|",data[0],"\t|",data[1],"|",data[2],"\t\t|",data[3],"\t\t\t|",data[4],"\t|",data[5],"\t\t|")
        print("-----------------------------------------------------------------------------------------------------------------------------------------")



