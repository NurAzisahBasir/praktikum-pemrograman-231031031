a = True

while a:
    # Meminta user memasukkan pilihan
    pilih = input('Pilihan: ')
    if pilih == 'ya':
        print('Selamat Datang')
        # Menghentikan perulangan dengan mengubah variabel a menjadi false
        a = False
    elif pilih == 'tidak':
        print('Sampai Jumpa')
        # Menghentikan perulangan dengan mengubah variabel a menjadi false
        a = False
    else:
        # program tetap berjalan diluar jawaban ya dan tidak
        print('Silahkan coba lagi')



