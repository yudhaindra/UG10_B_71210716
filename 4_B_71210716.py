a = float(input("Masukkan angka : "))


if (a%2 == 0) and (a%3 != 0) :
    print("Bilangan tersebut habis dibagi 2 dan tidak habis dibagi 3? Jawab: YA")
    if (a%5 != 0) or (a%10 == 0):
        print("Apakah bilangan tersebut juga tidak habis dibagi 5 atau habis dibagi 10? Jawab: IYA DONG") 
    else:
        print("angka salah")
else:
    print("Bilangan tersebut tidak habis dibagi 2 dan habis dibagi 3. Program dihentikan")