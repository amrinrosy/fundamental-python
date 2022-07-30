#Menentukna bilangan prima atau bukan
angka = int(input('Masukkan angka : '))
if (angka == 2 or angka == 3 or angka == 5 or angka == 7) or (angka%2 != 0 and angka%3 != 0 and angka%5 != 0 and angka%7 != 0):
    print('{} merupakan bilangan prima'.format(angka))
else:
    print('{} bukan merupakan bilangan prima'.format(angka))

#Menentukan daftar bilangan prima antara 2 bilangan
angka_awal = int(input('Masukkan angka awal : '))
angka_akhir = int(input('Masukkan angka akhir : '))
list_angka = [i for i in range(angka_awal, angka_akhir +1)]
bilangan_prima = [i for i in list_angka if (i == 2 or i == 3 or i == 5 or i == 7)or (i%2 != 0 and i%3 != 0 and i%5 != 0 and i%7 != 0)]
print(bilangan_prima)

