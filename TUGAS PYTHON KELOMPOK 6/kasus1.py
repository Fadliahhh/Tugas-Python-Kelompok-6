import math

def hitung_keliling_bola(jari_jari):
    return 2 * math.pi * jari_jari

def hitung_luas_bola(jari_jari):
    return 4 * math.pi * jari_jari ** 2

def hitung_volume_bola(jari_jari):
    return (4/3) * math.pi * jari_jari ** 3

def hitung_keliling_kubus(sisi):
    return 12 * sisi

def hitung_luas_kubus(sisi):
    return 6 * sisi ** 2

def hitung_volume_kubus(sisi):
    return sisi ** 3

def hitung_keliling_balok(panjang, lebar, tinggi):
    return 4 * (panjang + lebar + tinggi)

def hitung_luas_balok(panjang, lebar, tinggi):
    return 2 * ((panjang * lebar) + (panjang * tinggi) + (lebar * tinggi))

def hitung_volume_balok(panjang, lebar, tinggi):
    return panjang * lebar * tinggi

def main():
    while True:
        print("Menu:")
        print("a) Bola")
        print("b) Kubus")
        print("c) Balok")

        pilihan = input("Masukkan pilihan (a/b/c): ")

        if pilihan.lower() == 'a':
            print("1. Keliling")
            print("2. Luas")
            print("3. Volume")
            statement = int(input("Masukkan statement (1/2/3): "))

            if statement == 1:
                jari_jari = float(input("Masukkan jari-jari bola: "))
                print("Keliling bola:", hitung_keliling_bola(jari_jari))
            elif statement == 2:
                jari_jari = float(input("Masukkan jari-jari bola: "))
                print("Luas bola:", hitung_luas_bola(jari_jari))
            elif statement == 3:
                jari_jari = float(input("Masukkan jari-jari bola: "))
                print("Volume bola:", hitung_volume_bola(jari_jari))
            else:
                print("Pilihan tidak valid")

        elif pilihan.lower() == 'b':
            print("1. Keliling")
            print("2. Luas")
            print("3. Volume")
            statement = int(input("Masukkan statement (1/2/3): "))

            if statement == 1:
                sisi = float(input("Masukkan panjang sisi kubus: "))
                print("Keliling kubus:", hitung_keliling_kubus(sisi))
            elif statement == 2:
                sisi = float(input("Masukkan panjang sisi kubus: "))
                print("Luas kubus:", hitung_luas_kubus(sisi))
            elif statement == 3:
                sisi = float(input("Masukkan panjang sisi kubus: "))
                print("Volume kubus:", hitung_volume_kubus(sisi))
            else:
                print("Pilihan tidak valid")

        elif pilihan.lower() == 'c':
            print("1. Keliling")
            print("2. Luas")
            print("3. Volume")
            statement = int(input("Masukkan statement (1/2/3): "))

            if statement == 1:
                panjang = float(input("Masukkan panjang balok: "))
                lebar = float(input("Masukkan lebar balok: "))
                tinggi = float(input("Masukkan tinggi balok: "))
                print("Keliling balok:", hitung_keliling_balok(panjang, lebar, tinggi))
            elif statement == 2:
                panjang = float(input("Masukkan panjang balok: "))
                lebar = float(input("Masukkan lebar balok: "))
                tinggi = float(input("Masukkan tinggi balok: "))
                print("Luas balok:", hitung_luas_balok(panjang, lebar, tinggi))
            elif statement == 3:
                panjang = float(input("Masukkan panjang balok: "))
                lebar = float(input("Masukkan lebar balok: "))
                tinggi = float(input("Masukkan tinggi balok: "))
                print("Volume balok:", hitung_volume_balok(panjang, lebar, tinggi))
            else:
                print("Pilihan tidak valid")

        else:
            print("Pilihan tidak valid")

        ulangi = input("Apakah Anda ingin mengulangi (ya/tidak)? ")
        if ulangi.lower() != 'ya':
            break

if __name__ == "__main__":
    main()
