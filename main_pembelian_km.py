import pembelian
print('1. Tambah data pembelian kacamata')
print('2. Ubah data pembelian kacamata')
print('3. Hapus data pembelian kacamata')
print('4. Mencari Data pembelian kacamata')
print('5. Tampilkan data pembelian kacamata')
menu2=int(input('[data]Pilih: '))
if(menu2==1):
    tanggal=input('Tanggal [YYYY-MM-DD] :')
    nama=input('Nama: ')
    alamat=input('Alamat: ')
    nomor_hp=input('Nomor HP :')
    print("1. kacamata kode A = 350.000")
    print("2. kacamata kode B = 500.000")
    print("3. kacamata kode C = 750.000")
    print("4. kacamata kode D = 800.000")
    print("5. kacamata kode E = 950.000")
    print("6. kacamata kode F = 1000.000")
    pilih=int(input("masukan tipe kacamata :"))
    if(pilih==1):
        print("kacamata kode A = 350.000")
        tipe_kacamata=('tipe kacamata A')
        jumlah=int(input('jumlah pembelian :'))
        anti_radiasi=input("apakah ingin menggunakan anti radiasi? [Y/N] :")
        if(anti_radiasi=='Y'):
            anti_radiasi=150000
            harga=350000
            total=jumlah*(350000+150000)
        elif(anti_radiasi == 'N'):
            anti_radiasi=0
            harga=350000
            total=350000*jumlah
        else:
            print("menu tidak tersedia")

    if(pilih==2):
        print("kacamata kode B = 500.000")
        tipe_kacamata=('tipe kacamata B')
        jumlah=int(input('jumlah pembelian :'))
        anti_radiasi=input("apakah ingin menggunakan anti radiasi? [Y/N] :")
        if(anti_radiasi=='Y'):
            anti_radiasi=150000
            harga=500000
            total=jumlah*(500000+150000)
        elif(anti_radiasi == 'N'):
            anti_radiasi=0
            harga=500000
            total=500000*jumlah
        else:
            print("menu tidak tersedia")

    if(pilih==3):
        print("kacamata kode C = 750.000")
        tipe_kacamata=('tipe kacamata C')
        jumlah=int(input('jumlah pembelian :'))
        anti_radiasi=input("apakah ingin menggunakan anti radiasi? [Y/N] :")
        if(anti_radiasi=='Y'):
            anti_radiasi=150000
            harga=750000
            total=jumlah*(750000+150000)
        elif(anti_radiasi == 'N'):
            anti_radiasi=0
            harga=750000
            total=750000*jumlah
        else:
            print("menu tidak tersedia")

    if(pilih==4):
        print("kacamata kode D = 800.000")
        tipe_kacamata=('tipe kacamata D')
        jumlah=int(input('jumlah pembelian :'))
        anti_radiasi=input("apakah ingin menggunakan anti radiasi? [Y/N] :")
        if(anti_radiasi=='Y'):
            anti_radiasi=150000
            harga=800000
            total=jumlah*(800000+150000)
        elif(anti_radiasi == 'N'):
            anti_radiasi=0
            harga=800000
            total=800000*jumlah
        else:
            print("menu tidak tersedia")

    if(pilih==5):
        print("kacamata kode E = 950.000")
        tipe_kacamata=('tipe kacamata E')
        jumlah=int(input('jumlah pembelian :'))
        anti_radiasi=input("apakah ingin menggunakan anti radiasi? [Y/N] :")
        if(anti_radiasi=='Y'):
            anti_radiasi=150000
            harga=950000
            total=jumlah*(950000+150000)
        elif(anti_radiasi == 'N'):
            anti_radiasi=0
            harga=950000
            total=950000*jumlah
        else:
            print("menu tidak tersedia")

    if(pilih==6):
        print("kacamata kode F = 1.000.000")
        tipe_kacamata=('tipe kacamata F')
        jumlah=int(input('jumlah pembelian :'))
        anti_radiasi=input("apakah ingin menggunakan anti radiasi? [Y/N] :")
        if(anti_radiasi=='Y'):
            anti_radiasi=150000
            harga=1000000
            total=jumlah*(1000000+150000)
        elif(anti_radiasi == 'N'):
            anti_radiasi=0
            harga=1000000
            total=1000000*jumlah
        else:
            print("menu tidak tersedia")
    else:
        print("menu tidak tersedia")
    print("total yang harus dibayar :Rp ",total)
    
    data=[tanggal,nama,alamat,nomor_hp,tipe_kacamata,jumlah,anti_radiasi,harga,total]
    pembelian.add(data)
elif(menu2==2):
    id=int(input("masukan id yang akan diubah :"))
    nama=input('Ubah nama menjadi : ')
    alamat=input('Alamat: ')
    nomor_hp=int(input('Nomor HP :'))
    print("1. kacamata kode A = 350.000")
    print("2. kacamata kode B = 500.000")
    print("3. kacamata kode C = 750.000")
    print("4. kacamata kode D = 800.000")
    print("5. kacamata kode E = 950.000")
    print("6. kacamata kode F = 1000.000")
    pilih=int(input("masukan tipe kacamata :"))
    if(pilih==1):
        print("kacamata kode A = 350.000")
        tipe_kacamata=('tipe kacamata A')
        jumlah=int(input('jumlah pembelian :'))
        anti_radiasi=input("apakah ingin menggunakan anti radiasi? [Y/N] :")
        if(anti_radiasi=='Y'):
            anti_radiasi=150000
            harga=350000
            total=jumlah*(350000+150000)
        elif(anti_radiasi == 'N'):
            anti_radiasi=0
            harga=350000
            total=350000*jumlah
        else:
            print("menu tidak tersedia")

    if(pilih==2):
        print("kacamata kode B = 500.000")
        tipe_kacamata=('tipe kacamata B')
        jumlah=int(input('jumlah pembelian :'))
        anti_radiasi=input("apakah ingin menggunakan anti radiasi? [Y/N] :")
        if(anti_radiasi=='Y'):
            anti_radiasi=150000
            harga=500000
            total=jumlah*(500000+150000)
        elif(anti_radiasi == 'N'):
            anti_radiasi=0
            harga=500000
            total=500000*jumlah
        else:
            print("menu tidak tersedia")

    if(pilih==3):
        print("kacamata kode C = 750.000")
        tipe_kacamata=('tipe kacamata C')
        jumlah=int(input('jumlah pembelian :'))
        anti_radiasi=input("apakah ingin menggunakan anti radiasi? [Y/N] :")
        if(anti_radiasi=='Y'):
            anti_radiasi=150000
            harga=750000
            total=jumlah*(750000+150000)
        elif(anti_radiasi == 'N'):
            anti_radiasi=0
            harga=750000
            total=750000*jumlah
        else:
            print("menu tidak tersedia")

    if(pilih==4):
        print("kacamata kode D = 800.000")
        tipe_kacamata=('tipe kacamata D')
        jumlah=int(input('jumlah pembelian :'))
        anti_radiasi=input("apakah ingin menggunakan anti radiasi? [Y/N] :")
        if(anti_radiasi=='Y'):
            anti_radiasi=150000
            harga=800000
            total=jumlah*(800000+150000)
        elif(anti_radiasi == 'N'):
            anti_radiasi=0
            harga=800000
            total=800000*jumlah
        else:
            print("menu tidak tersedia")

    if(pilih==5):
        print("kacamata kode E = 950.000")
        tipe_kacamata=('tipe kacamata E')
        jumlah=int(input('jumlah pembelian :'))
        anti_radiasi=input("apakah ingin menggunakan anti radiasi? [Y/N] :")
        if(anti_radiasi=='Y'):
            anti_radiasi=150000
            harga=950000
            total=jumlah*(950000+150000)
        elif(anti_radiasi == 'N'):
            anti_radiasi=0
            harga=950000
            total=950000*jumlah
        else:
            print("menu tidak tersedia")

    if(pilih==6):
        print("kacamata kode F = 1.000.000")
        tipe_kacamata=('tipe kacamata F')
        jumlah=int(input('jumlah pembelian :'))
        anti_radiasi=input("apakah ingin menggunakan anti radiasi? [Y/N] :")
        if(anti_radiasi=='Y'):
            anti_radiasi=150000
            harga=1000000
            total=jumlah*(1000000+150000)
        elif(anti_radiasi == 'N'):
            anti_radiasi=0
            harga=1000000
            total=1000000*jumlah
        else:
            print("menu tidak tersedia")
    else:
        print("menu tidak tersedia")
    print("total yang harus dibayar :Rp ",total)
    
    data=[nama,alamat,nomor_hp,tipe_kacamata,jumlah,harga,total,id]
    pembelian.edit(data)
elif(menu2==3):
    nama_pembelian_kacamata=input('Nama :')
    data=[nama_pembelian_kacamata]
    pembelian.search(data)
    confirm=input('Yakin menghapus data pembelian kacamata ini? [Y/N]:')
    if(confirm=='Y'):
        pembelian.delete(data)
    else:
        print('Tidak jadi menghapus data!')
elif(menu2==4):
    nama=input('Masukan Nama yang Anda cari = ')
    data=[nama]
    pembelian.search(data)
elif(menu2==5):
        pembelian.show()
else:
    print('Menu tidak tersedia')

