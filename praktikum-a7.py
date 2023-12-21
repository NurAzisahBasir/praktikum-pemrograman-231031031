# Inisialisasi variabel
password_benar = 'l0v3 m3'
maks_kesalahan = 3
kesalahan = 0

# Perulangan untuk maksimal tiga kali kesalahan
while kesalahan < maks_kesalahan:
    # Meminta user memasukkan password
    password_input = input("Masukkan Password: ")

    # Memeriksa apakah password yang dimasukkan benar
    if password_input == password_benar:
        print("Selamat Anda Login!")
        break  # Keluar dari perulangan jika password benar
    else:
        kesalahan += 1
        sisa_kesalahan = maks_kesalahan - kesalahan
        print(f"Password Salah! Kesempatan anda tersisa {sisa_kesalahan} kali.")

# Pesan jika kesalahan maksimal tercapai
if kesalahan == maks_kesalahan:
    print("Anda kehabisan kesempatan")