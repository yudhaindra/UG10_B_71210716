b1 = float(input("Bil1 : "))
b2 = float(input("Bil2 : "))
kal= str(input("Masukkan kalimat : "))


if "kali" in kal:
    hasil = b1*b2
    print("Hasil perkalian",b1,"dengan",b2,"adalah",hasil)
elif "kurang"in kal:
    hasil = b1-b2
    print("Hasil pengurangan",b1,"dengan",b2,"adalah",hasil)
elif "bagi"in kal:
    hasil = b1/b2
    print("Hasil pembagian",b1,"dengan",b2,"adalah",hasil)
elif "tambah"in kal:
    hasil = b1+b2
    print("Hasil penjumlahan",b1,"dengan",b2,"adalah",hasil)
else:
    print("Tidak ada operator aritmatika pada kalimat!!!")
