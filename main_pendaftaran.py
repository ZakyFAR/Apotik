import pendaftaran_pemeriksaan
print('1. Tambahkan Data Pendaftaran')
print('2. Ubah Data Pendaftaran')
print('3. Hapus Data Pendaftaran')
print('4. Mencari data Pendaftaran')
print('5. Tampilkan data Pendaftaran')
menu2 = int(input(' Pilih : '))
if(menu2 == 1):
    tanggal=input('Masukan tanggal[YY,MM,DD] :')
    nomor_urut=int(input('Masukan Nomor Urut :'))
    nama=input('Nama : ')
    print('1. Pria')
    print('2. Wanita')
    jk=int(input('Pilih Jenis Kelamin Anda :' ))
    if (jk==1):
        jenis_kelamin=('Pria')
    elif (jk==2):
        jenis_kelamin=('Wanita')
    else :
        jenis_kelamin=('Tidak Terdaftar')
    umur=int(input('Umur :'))
    alamat=input('Alamat : ')
    data=[tanggal,nomor_urut,nama,jenis_kelamin,umur,alamat]
    pendaftaran_pemeriksaan.add(data)
    
elif(menu2 == 2):
    nomor_urut=int(input('Masukan Nomor Urut :'))
    tanggal=input('Masukan tanggal[YY,MM,DD] :')
    nama=input('Ubah Nama Menjadi : ')
    print('1. Pria')
    print('2. Wanita')
    jk=int(input('Pilih Jenis Kelamin Anda :' ))
    if (jk==1):
        jenis_kelamin=('Pria')
    elif (jk==2):
        jenis_kelamin=('Wanita')
    else :
        jenis_kelamin=('Tidak Terdaftar')
    umur=int(input('Umur :'))
    alamat=input('Alamat : ')
    data=[nama,alamat,jenis_kelamin,umur,nomor_urut,tanggal]
    pendaftaran_pemeriksaan.edit(data)
elif(menu2 == 3):
    nama_pendaftaran = input('Nama:')
    data=[nama_pendaftaran]
    pendaftaran_pemeriksaan.search(data)
    confirm = input('Yakin menghapus data pasien ini? [Y/N] : ')
    if(confirm == 'Y' or 'y'):
        pendaftaran_pemeriksaan.delete(data)
    else:
        print('Tidak jadi menghapus data pasien!')
elif(menu2 == 4):
    nama=input('Masukan Nama yang Anda cari : ')
    data=[nama]
    pendaftaran_pemeriksaan.search(data)
elif(menu2 == 5):
        pendaftaran_pemeriksaan.show()
