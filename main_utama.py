print("1. MENU PENDAFTARAN PEMERIKSAAN MATA")
print("2. MENU PEMERIKSAAN MATA")
print("3. MENU PEMBELIAN KACAMATA")
menu=int(input("Pilih : "))
if(menu==1):
    import main_pendaftaran
elif(menu==2):
    import main_pemeriksaan
elif(menu==3):
    import main_pembelian_km
else:
    ("MENU TIDAK TERSEDIA")
