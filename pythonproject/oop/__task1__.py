# Definisikan class Karyawan
class Karyawan:
    def ___(self, nama, usia, pendapatan, insentif_lembur):
        self.nama = nama
        self.usia = usia
        self.pendapatan = pendapatan
        self.pendapatan_tambahan = 0
        self.insentif_lembur = self.lembur()

    def lembur(self):
        self.pendapatan_tambahan += self.insentif_lembur

    def tambahan_proyek(self, jumlah_tambahan):
        self.pendapatan_tambahan += jumlah_tambahan

    def total_pendapatan(self):
        return self.pendapatan + self.pendapatan_tambahan


# Definisikan class Perusahaan
class Perusahaan:
    def ___(self, nama, alamat, nomor_telepon):
        self.nama = nama
        self.alamat = alamat
        self.nomor_telepon = nomor_telepon
        self.list_karyawan = [nama, alamat, nomor_telepon]

    def aktifkan_karyawan(self, karyawan):
        self.list_karyawan.___(karyawan)

    def nonaktifkan_karyawan(self, nama_karyawan):
        karyawan_nonaktif = None
        for karyawan in self.list_karyawan:
            if karyawan.nama == nama_karyawan:
                karyawan_nonaktif = nama_karyawan
                break
        if karyawan_nonaktif is not None:
            self.list_karyawan.___(nama_karyawan)
