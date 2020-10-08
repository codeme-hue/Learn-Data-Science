# Data
uang_jalan = 1500000
jumlah_hari = 31
list_plat_nomor = [8993, 2198, 2501, 2735, 3772, 4837, 9152]
# Pengecekan kendaraan dengan nomor pelat ganjil atau genap
# Deklarasikan kendaraan_genap dan kendaraan_ganjil = 0
kendaraan_genap = 0
kendaraan_ganjil = 0
for plat_nomor in list_plat_nomor:
    if plat_nomor % 2 == 0:
        kendaraan_genap += plat_nomor
        print(kendaraan_genap)
    else:
        kendaraan_ganjil += plat_nomor
        print(kendaraan_ganjil)
#Total pengeluaran untuk kendaraan dengan nomor pelat ganjil
# dan genap dalam 1 bulan
i = 0
total_pengeluaran = 0
while i <= jumlah_hari:
    if i % 2 == 0:
        kendaraan_genap *= i
        #print(kendaraan_genap)
    else:
        kendaraan_ganjil *= i
        #print(kendaraan_ganjil)
    #i += total_pengeluaran
# Cetak total pengeluaran
print(i)