class Orang:
    def __init__(self, nama):
        self.nama = nama

    def sapa(self):
        print("Halo, saya", self.nama)

class Siswa(Orang):
    def __init__(self, nama, kelas):
        super().__init__(nama)
        self.kelas = kelas

    def info(self):
        print(self.nama, "kelas", self.kelas)

class Guru(Orang):
    def mengajar(self):
        print(self.nama, "sedang mengajar")

s = Siswa("Raditya", "XI RPL")
s.sapa()
s.info()
g = Guru("Pak Andi")
g.sapa()
g.mengajar()
