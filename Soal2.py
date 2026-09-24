a = int(input("Masukkan angka 1: "))
b = int(input("Masukkan angka 2: "))
c = int(input("Masukkan angka 3: "))

if a > b and a > c:
    print("Terbesar:", a)
elif b > a and b > c:
    print("Terbesar:", b)
else:
    print("Terbesar:", c)