import pemeriksaan_mata
print('1. Tambahkan Hasil Pemeriksaan')
print('2. Hapus Hasil Pemeriksaan')
print('3. Ubah Hasil Pemeriksaan Data Mata ')
print('4. Mencari Data Hasil')
print('5. Tampilkan Hasil Pemeriksaan')
menu2 = int(input(' Pilih : '))
if (menu2==1):
    tanggal=input('Masukan Tanggal [yyyy-MM-DD] :'  )
    nama=input('Isikan Nama : ')
    mata_kanan=float(input ('Masukan Data Mata Kanan :'))
    mata_kiri=float(input('Masukan Data Mata Kiri :'))
    if (mata_kanan<0 and mata_kiri<0):
        jenis_kacamata=('Lensa Minus keduanya')
    elif (mata_kanan>0 and mata_kiri>0):
        jenis_kacamata=('Lensa Plus keduanya')
    elif(mata_kanan<0 and mata_kiri==0):
        jenis_kacamata=('lensa Kiri Minus dan lensa Kanan Normal')
    elif(mata_kanan<0 and mata_kiri>0):
        jenis_kacamata=('lensa Kiri Minus dan lensa Kanan Plus')
    elif(mata_kanan==0 and mata_kiri<0):
        jenis_kacamata=('lensa Kiri Normal dan lensa Kanan Minus')
    elif(mata_kanan==0 and mata_kiri>0):
        jenis_kacamata=('lensa Kiri Normal dan lensa Kanan Plus')
    elif(mata_kanan>0 and mata_kiri<0):
        jenis_kacamata=('lensa Kiri Plus dan lensa Kanan Minus')
    elif(mata_kanan>0 and mata_kiri==0):
        jenis_kacamata=('lensa Kiri Plus dan lensa Kanan Normal')
    else:
        jenis_kacamata=('Mata Normal')
    lain_lain=input('Masukan Keterangan Lain Lain : ')
    data = [tanggal,nama,mata_kanan, mata_kiri,jenis_kacamata,lain_lain]
    pemeriksaan_mata.add(data)

elif(menu2 == 2):
    nama=input(' Masukan id yang akan di hapus : ')
    data = [id]
    #hasil.search(data)
    confirm = input('Yakin menghapus ini? [Y/N] : ')
    if(confirm == 'Y' or 'y'):
        pemeriksaan_mata.delete(data)
    else:
        print('Tidak jadi menghapus data !')

elif(menu2 == 3):
    nama = input('Nama : ')
    mata_kanan=float(input ('Masukan Data Mata Kanan :'))
    mata_kiri=float(input('Masukan Data Mata Kiri :'))
    if (mata_kanan<0 and mata_kiri<0):
        jenis_kacamata=('Lensa Minus keduanya')
    elif (mata_kanan>0 and mata_kiri>0):
        jenis_kacamata=('Lensa Plus keduanya')
    elif(mata_kanan<0 and mata_kiri==0):
        jenis_kacamata=('lensa Kiri Minus dan lensa Kanan Normal')
    elif(mata_kanan<0 and mata_kiri>0):
        jenis_kacamata=('lensa Kiri Minus dan lensa Kanan Plus')
    elif(mata_kanan==0 and mata_kiri<0):
        jenis_kacamata=('lensa Kiri Normal dan lensa Kanan Minus')
    elif(mata_kanan==0 and mata_kiri>0):
        jenis_kacamata=('lensa Kiri Normal dan lensa Kanan Plus')
    elif(mata_kanan>0 and mata_kiri<0):
        jenis_kacamata=('lensa Kiri Plus dan lensa Kanan Minus')
    elif(mata_kanan>0 and mata_kiri==0):
        jenis_kacamata=('lensa Kiri Plus dan lensa Kanan Normal')
    else:
        jenis_kacamata=('Mata Normal')
        
    data = [mata_kanan,mata_kiri,jenis_kacamata,nama]
    pemeriksaan_mata.edit(data)


elif (menu2==4):
    nama=input('Nama Yang Anda Cari : ')
    data=[nama]
    pemeriksaan_mata.search(data)

elif(menu2 == 5):
        pemeriksaan_mata.show()
