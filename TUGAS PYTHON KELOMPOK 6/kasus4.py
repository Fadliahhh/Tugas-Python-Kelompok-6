baris = int(input("Masukan jumlah baris : "))
for i in range(baris + 1, 0, -1):
    for j in range(0, i - 1):
        print("*", end=' ')
    print(" ")
