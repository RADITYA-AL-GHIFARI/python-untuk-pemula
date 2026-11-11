class Siswa:
    def __init__(self, nama, nilai):
        self.nama = nama
        self.nilai = nilai

    def perkenalan(self):
        print("Halo, saya", self.nama)

    def status(self):
        if self.nilai >= 75:
            return "Lulus"
        return "Belum lulus"

siswa1 = Siswa("Raditya", 85)
siswa1.perkenalan()
print("Status:", siswa1.status())
siswa2 = Siswa("Budi", 60)
siswa2.perkenalan()
print("Status:", siswa2.status())
