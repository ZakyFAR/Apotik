import mysql.connector
import connect
db = connect.koneksi()

#Menambahkan data baru ke dalam tabel Pembelian kacamata
def add(data):
    cursor = db.cursor()
    sql = """INSERT INTO pembelian (tanggal,nama,alamat,nomor_hp,tipe_kacamata,jumlah,anti_radiasi,harga,total) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    cursor.execute(sql,data)
    db.commit()
    print(' Data Pembelian kacamata berhasil ditambahkan!'.format(cursor.rowcount))

#Menampilkan seluruh data dari tabel Pembelian kacamata
def show():
    cursor = db.cursor()
    sql = """SELECT * FROM pembelian"""
    cursor.execute(sql)
    results = cursor.fetchall()
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    print("|TANGGAL\t|ID\t|NAMA\t\t|ALAMAT\t\t|NOMOR HP\t|TIPE KACAMATA\t\t|JUMLAH\t|ANTI RADIASI\t|HARGA\t\t|TOTAL\t|")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    for data in results:
        print("|",data[0],"\t|",data[1],"\t|",data[2],"\t|",data[3],"\t|",data[4],"\t|",data[5],"\t|",data[6],"\t|",data[7],"\t|",data[8],"\t|",data[9],"|")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------")

#Mengubah data per record berdasarkan id pada tabel Pembelian kacamata
def edit(data):
    cursor=db.cursor()
    sql="""UPDATE pembelian SET nama=%s,alamat=%s,nomor_hp=%s,tipe_kacamata=%s,jumlah=%s,harga=%s,total=%s WHERE id=%s"""
    cursor.execute(sql,data)
    db.commit()
    print(' Data Pembelian kacamata berhasil diubah!'.format(cursor.rowcount))

#Menghapus data dari tabel Pembelian kacamata
def delete(data):
    cursor = db.cursor()
    sql = """DELETE FROM pembelian WHERE nama=%s"""
    cursor.execute(sql,data)
    db.commit()
    print(' Data Pembelian kacamata berhasil dihapus!'.format(cursor.rowcount))

#Mencari data dari tabel Pembelian kacamata
def search(data):
    cursor = db.cursor()
    sql = """SELECT * FROM Pembelian WHERE nama=%s"""
    cursor.execute(sql,data)
    results = cursor.fetchall()
    
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    print("|TANGGAL\t|ID\t|NAMA\t\t|ALAMAT\t\t|NOMOR HP\t|TIPE KACAMATA\t\t|JUMLAH\t|ANTI RADIASI\t|HARGA\t\t|TOTAL\t|")
    print("--------------------------------------------------------------------------------------------------------------------------------------------------")
    for data in results:
        print("|",data[0],"\t|",data[1],"\t|",data[2],"\t|",data[3],"\t|",data[4],"\t|",data[5],"\t|",data[6],"\t|",data[7],"\t|",data[8],"\t|",data[9],"|")
        print("--------------------------------------------------------------------------------------------------------------------------------------------------")



