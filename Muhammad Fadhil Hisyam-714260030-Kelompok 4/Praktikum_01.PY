# ===============================================
# Praktikum 1: NESTED IF (EVALUASI KELULUSAN)
# Nama : Muhammad Fadhil Hisyam
# Kelas : 1B
# ===============================================


kehadiran = int(input("Jumlah kehadiran (1-14): "))
nilai = int(input("Nilai ujian (1-100): "))

if kehadiran >= 12:
    if nilai >= 75:
        print("LULUS - Nilai memuaskan")
    else:
        print("REMEDIAL - Nilai ujian kurang")
else:
    print("TIDAK LLULUS - KEHADIRAN KURANG DARI 12")