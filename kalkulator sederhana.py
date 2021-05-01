#fungsi kalkulator yang dimasukkan adalah pertambahan, pengurangan, perkalian, pembagian
#kemudian akan dijadikan menu kalkulator

#fungsi pertambahan
def add(a, b):
    return a + b

#fungsi pengurangan
def subtract(a, b):
    return a - b

#fungsi perkalian
def multiply(a, b):
    return a * b

#fungsi pembagian
def divide(a, b):
    return a / b

#menu kalkulator
print("======Menu Kalkulator======")
print("1. Penjumlahan")
print("2. Pengurangan")
print("3. Perkalian")
print("4. Pembagian")

#membuat input user
menu = input("Masukkan pilihan menu(1, 2, 3, 4) =")

angka1 = int(input("Masukkan bilangan pertama : "))
angka2 = int(input("Masukkan bilangan kedua : "))

if menu == '1':
    print(angka1, "+", angka2, "=", add(angka1, angka2))

elif menu == '2':
    print(angka1, "-", angka2, "=", subtract(angka1, angka2))

elif menu == '3':
    print(angka1, "*", angka2, "=", multiply(angka1, angka2))

elif menu == '4':
    print(angka1, "/", angka2, "=", divide(angka1, angka2))

else :
    print("menu tidak terdaftar")