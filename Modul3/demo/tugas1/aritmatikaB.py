from functools import reduce

# Fungsi rekursif untuk menghitung suku ke-n dalam baris aritmetika-geometri
def baris_aritmetika_geometri(a, d, r, n, hasil=None):
    if hasil is None:
        hasil = []
    
    if n == 1:
        hasil.append(a)
    else:
        # Rekursif untuk menghitung suku ke-(n-1)
        baris_aritmetika_geometri(a, d, r, n - 1, hasil)
        # Menambahkan suku ke-n ke dalam daftar hasil
        Un = a + (n - 1) * d * (r ** (n - 1))
        hasil.append(Un)
    
    return hasil

# Fungsi untuk menghitung deret dari baris tanpa menggunakan lambda
def hitung_deret(baris):
    return sum(baris)

# Input dari pengguna
a = int(input("Masukkan suku pertama (a): "))
d = int(input("Masukkan beda (d): "))
r = int(input("Masukkan rasio (r): "))
n = int(input("Masukkan jumlah suku (n): "))

# Membuat baris aritmetika-geometri
baris = baris_aritmetika_geometri(a, d, r, n)

# Menghitung deret dari baris
deret = hitung_deret(baris)

# Output hasil
print("Baris Aritmetika-Geometri:", baris)
print("Deret Aritmetika-Geometri:", deret)
