siswa = {"nama": "Raditya", "kelas": "XI RPL", "sekolah": "SMKN 2 Singaparna"}
print("Nama:", siswa["nama"])
siswa["hobi"] = "ngoding"
print("Setelah ditambah:", siswa)
for kunci, nilai in siswa.items():
    print(kunci, "=", nilai)
