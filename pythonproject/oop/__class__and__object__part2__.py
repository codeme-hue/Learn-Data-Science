# Definisikan class Karyawan
class Karyawan:
    nama_perusahaan = 'ABC'
    def __init__(self, nama, usia, pendapatan):
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan
# Buat object bernama aksara dan senja
aksara = Karyawan('Aksara', 25, 8500000)
senja = Karyawan('Senja', 28, 12500000)
# Cetak objek bernama aksara
print(aksara.nama + ', Usia: ' + str(aksara.usia) + ', Pendapatan ' + str(aksara.pendapatan))
# Cetak objek bernama senja
print(senja.nama + ', Usia: ' + str(senja.usia) + ', Pendapatan ' + str(senja.pendapatan))

"""
class Karyawan:
    nama_perusahaan = 'ABC'
    def __init__(self, nama, usia, pendapatan):
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan
        if usia > 30:
            self.pendapatan += 1500000

karyawan_1 = Karyawan('Budi', 35, 7500000)
karyawan_2 = Karyawan('Didi', 30, 8000000)

total_pengeluaran = karyawan_1.pendapatan + karyawan_2.pendapatan
print(total_pengeluaran)
"""

"""
class Karyawan:
    nama_perusahaan = 'ABC'
    tunjangan_transportasi = 500000
    def __init__(self, nama, usia, pendapatan):
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan

karyawan_1 = Karyawan('Budi', 35, 5000000)
karyawan_2 = Karyawan('Didi', 30, 5000000)
karyawan_1.__class__.nama_perusahaan = 1000000

total_pengeluaran = karyawan_1.__class__.tunjangan_transportasi
total_pengeluaran += karyawan_2. __class__.tunjangan_transportasi
total_pengeluaran += karyawan_1.pendapatan
total_pengeluaran += karyawan_2.pendapatan
print(total_pengeluaran)
"""