daftar_siswa = [
    {"nama": "Raditya", "nilai": 85},
    {"nama": "Budi", "nilai": 70},
    {"nama": "Sari", "nilai": 92},
]
for s in daftar_siswa:
    print(s["nama"], "mendapat nilai", s["nilai"])
print("Jumlah siswa:", len(daftar_siswa))
