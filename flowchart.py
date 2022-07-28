'''
Semua sintaksis dasar bahasa pemrograman terdiri dari :
- Sekuensial  : langkah berurutan
- Percabangan : langkah melompat jika kondisi terpenuhi
- Perulangan  : mengulang langkah yang sama berkali-kali selama/sampai kondisi terpenuhi
'''

#Sekuensial
print('Ibu berkata, "Pergi ke toko"')
print('Budi menjawab, "Baik, apa yang harus saya lakukan di toko?"')
print('Ibu menjawab, "Beli satu botol susu, dan jika ada telor beli 6"')
print("maka Budi berangkat ke toko")

#Percabangan
jumlah_botol_susu = 173
jumlah_telur = 1587
print(f"jumlah botol susu {jumlah_botol_susu} botol")
print(f"jumlah telur {jumlah_telur} butir")
if jumlah_botol_susu > 0:
    print("Budi mengecek harganya, dan ternyata uangnya cukup")
    if jumlah_telur == 0:
        print("Budi membeli 1 botol susu")
    else:
        print("Budi membeli 1 botol susu & 6 butir telur")
else:
    print("Budi tidak jadi membeli 1 botol susu")
print("Budi pulang ke rumah")
print("Menyampaikan hasilnya kepada Ibu")

