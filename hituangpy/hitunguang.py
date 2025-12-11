# Fungsi untuk format rupiah dengan titik
def rupiah(n):
    return f"Rp{n:,}".replace(",", ".")

print("==============================================")
print("  Matematika Diskrit Kelas E-2024")
print("  1.Rizki Dwi Santoso                  24110037")
("==============================================\n")

# Input jumlah uang (boleh pakai titik, tidak boleh huruf)
while True:
    inp = input("Masukkan jumlah uang (contoh: 1.250.000): ")

    # Cek apakah ada huruf
    if any(ch.isalpha() for ch in inp):
        print("❌ Input tidak boleh mengandung huruf! Coba lagi.\n")
        continue

    # Cek apakah hanya angka, titik, atau spasi
    allowed = set("0123456789.")
    if not all(ch in allowed for ch in inp):
        print("❌ Input hanya boleh angka dan titik! Coba lagi.\n")
        continue

    # Jika lolos semua, keluar dari loop
    break

# Menghapus titik untuk dihitung sebagai angka
total_uang = int(inp.replace(".", ""))

# Daftar pecahan uang Indonesia
pecahan = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]

sisa = total_uang

print(f"\nTotal uang: {rupiah(total_uang)}")
print("Rincian pecahan:")

for p in pecahan:
    jumlah = sisa // p
    sisa = sisa % p
    print(f"Pecahan {rupiah(p)} = {jumlah} lembar")

print(f"Sisa uang yang tidak terbagi: {rupiah(sisa)}")
    