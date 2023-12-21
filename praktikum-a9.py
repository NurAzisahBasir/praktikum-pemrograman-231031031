import os
os.system('clear')

def judul():
    print('PROGRAM MENGHITUNG LUAS DAN KELILING'.center(45))
    print('BANGUN DATAR PERSEGI'.center(45))
    print()

def inputan():
    panjang = float(input('Masukkan panjang: '))
    lebar = float(input('Masukkan lebar: '))
    return panjang,lebar

# def luasan(panjang,lebar):
#     hasil = panjang * lebar
#     return hasil

# def keliling(panjang,lebar):
#     hasil = (panjang+lebar)*2
#     return hasil

def hitung(panjang,lebar):
    luas = panjang*lebar
    kel = (panjang+lebar)*2
    return luas,kel

def tampil(pesan,nilai):
    print(f'Hasil perhitungan nilai {pesan}: {nilai}')

def pilihan():
    pilih = input('Apakah ingin melanjutkan? [y/n]')
    if pilih == 'y':
        a = True
    else :
        a = False
        print('Dadah!')
    return a

a = True
while a:

    # Judul
    judul()

    # Inputan panjang dan lebar
    panjang,lebar = inputan()

    # Hitung luas dan keliling
    luas,kel = hitung(panjang,lebar)

    # Cetak atau display
    tampil('luas',luas)
    tampil('keliling',kel)

    # pilihan
    a = pilihan()