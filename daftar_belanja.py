#membuat daftar belanja
#menambah daftar belanja
def tambah_belanja(text):
    file = open('belanja.txt','a+')
    file.write('\n' + text)


#list belanja
def daftar_belanja():
    file =open('belanja.txt', 'a+')
    file.seek(0)
    text = file.read()
    print(text)

#tentang apps
def tentang_program():
    tentang = open('about.txt', 'r')
    apps =tentang.read()
    print(apps)

def tanya_pengguna():
    print('Silahkan masukkan keperlan belanja anda ke Daftar Belanja')
    print('=================== Daftar Belanja ======================')
    tambah_belanja(input('Mau belanja apa : '))

def membaca_daftar_source_code():
    kode = open('source.txt', 'r')
    apps = kode.read()
    print(apps)

loop = True

print('========================= Menu ==========================')
print('1. Tambah ke Daftar Belanja')
print('2. List Belanja')
print('3. Quit/Keluar')
print('4. About Apps')
print('View Code')
print('==========================================================')
while (loop):
    print('\n')
    menu = input('Masukkan menu = ')
    if menu == "1":
        tanya_pengguna()
    elif menu == "2":
        daftar_belanja()
    elif menu == "3":
        quit()
    elif menu == "4":
        tentang_program()
    elif menu == "5":
        membaca_daftar_source_code()
    else:
        print("command not found")





