
def buat_baris_aritmetika(a, d, n):
    return [a + i * d for i in range(n)]


a = int(input("Masukkan suku pertama (a): "))
d = int(input("Masukkan beda (d): "))
n = int(input("Masukkan jumlah suku (n): "))


baris_aritmetika = buat_baris_aritmetika(a, d, n)


print("Baris Aritmetika:", baris_aritmetika)
