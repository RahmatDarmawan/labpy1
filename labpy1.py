print("Program menentukan bilangan terbesar dari 3 bilangan")
a = int(input ("masukkan nilai ke-1 : " ))
b = int(input ("masukkan nilai ke-2 : " ))
c = int(input ("masukkan nilai ke-3 : " ))

if a > b and a > c:
    print(a, " adalah nilai terbesar ")
elif b > a and b >c:
    print(b, " adalah nilai terbesar ")
else:
    print(c, " adalah nilai terbesar ")

