import mysql.connector
import connect
db = connect.koneksi()

#Menambahkan data baru ke dalam tabel pendaftaran
def add(data):
    cursor = db.cursor()
    sql = """INSERT INTO pendaftaran_pemeriksaan(tanggal,nomor_urut,nama,jenis_kelamin,umur,alamat) VALUES (%s,%s,%s,%s,%s,%s)"""
    cursor.execute(sql,data)
    db.commit()
    print(' Data Pendaftar berhasil ditambahkan!'.format(cursor.rowcount))

#Menampilkan seluruh data dari tabel pendaftaran
def show():
    cursor = db.cursor()
    sql = """SELECT * FROM pendaftaran_pemeriksaan"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print("-----------------------------------------------------------------------------------------------------------------")
    print("|TANGGAL\t|NOMOR URUT\t|NAMA\t\t\t|JENIS KELAMIN\t\t|UMUR\t|ALAMAT\t\t\t|")
    print("-----------------------------------------------------------------------------------------------------------------")
    for data in results:
        print("|",data[0],"\t|",data[1],"\t\t|",data[2],"\t\t|",data[3],"\t\t|",data[4],"\t|",data[5],"\t\t|")
        print("-----------------------------------------------------------------------------------------------------------------")

#Mengubah data per record berdasarkan id pada tabel pendaftaran
def edit(data):
    cursor=db.cursor()
    sql="""UPDATE pendaftaran_pemeriksaan SET nama=%s,alamat=%s,jenis_kelamin=%s,umur=%s WHERE nomor_urut=%s and tanggal=%s"""
    cursor.execute(sql,data)
    db.commit()
    print(' Data Pendaftar berhasil diubah!'.format(cursor.rowcount))

#Menghapus data dari tabel pendaftaran
def delete(data):
    cursor = db.cursor()
    sql = """DELETE FROM pendaftaran_pemeriksaan WHERE nama=%s"""
    cursor.execute(sql,data)
    db.commit()
    print(' Data Pendaftar berhasil dihapus!'.format(cursor.rowcount))

#Mencari data dari tabel pendaftaran
def search(data):
    cursor = db.cursor()
    sql = """SELECT * FROM pendaftaran_pemeriksaan WHERE nama=%s"""
    cursor.execute(sql,data)
    results = cursor.fetchall()

    print("------------------------------------------------------------------------------------------------------------------")
    print("|TANGGAL\t|NOMOR URUT\t|NAMA\t\t\t|JENIS KELAMIN\t\t|UMUR\t|ALAMAT\t\t\t|")
    print("------------------------------------------------------------------------------------------------------------------")
    for data in results:
        print("|",data[0],"\t|",data[1],"\t\t|",data[2],"\t\t|",data[3],"\t\t|",data[4],"\t|",data[5],"\t\t|")
        print("------------------------------------------------------------------------------------------------------------------")
