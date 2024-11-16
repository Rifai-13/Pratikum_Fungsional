def pisahkan_genap_ganjil(input_bilangan):

    # Tulis kode dibawah
    list_genap = []
    tuple_ganjil = ()
    # Memisahkan bilangan dan mengelompokkan ke genap atau ganjil
    for x in input_bilangan.split():
        bilangan =  int(x)
        if bilangan % 2 == 0:
           list_genap.append(bilangan)
        else:
           tuple_ganjil += (bilangan,)

    return list_genap, tuple_ganjil

# Meminta pengguna memasukkan bilangan yang dipisahkan oleh spasi
input_bilangan = input("Masukkan beberapa bilangan yang dipisahkan oleh spasi: ")

# Memanggil fungsi untuk memisahkan bilangan genap dan ganjil
result_genap, result_ganjil = pisahkan_genap_ganjil(input_bilangan)
print("hasil genap : ", result_genap)
print("hasil ganjil : ", result_ganjil) 