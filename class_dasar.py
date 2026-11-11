class Siswa:
    def __init__(self, nama, kelas):
        self.nama = nama
        self.kelas = kelas

siswa1 = Siswa("Raditya", "XI RPL")
siswa2 = Siswa("Budi", "XI TKJ")
print(siswa1.nama, "-", siswa1.kelas)
print(siswa2.nama, "-", siswa2.kelas)
