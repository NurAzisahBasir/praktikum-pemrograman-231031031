pwd_benar1 = 'si23a'
a = True
i = 0
limit1 = 3
while a:
    i += 1
    pwd1 = input('Masukkan password lapisan pertama: ')
    if pwd1 == pwd_benar1:
        print('Lapisan pertama berhasil dibuka!')

        pwd_benar2 = 'l0v3 m3'
        a = True
        i = 0
        limit2 = 3
        while a:
            i += 1
            pwd2 = input('Masukkan password lapisan kedua: ')
            if pwd2 == pwd_benar2:
                print('Lapisan kedua berhasil dibuka!')

                pwd_benar3 = 'd3v1l'
                a = True
                i = 0
                limit3 = 3
                while a:
                    i += 1
                    pwd3 = input('Masukkan password lapisan terakhir: ')
                    if pwd3 == pwd_benar3:
                        print('Lapisan terakhir berhasil dibuka!\nSelamat datang di dunia yang kejam')
                        a = False
                    else:
                        print('Password Salah!')
                        if i == limit3:
                            a = False
                            print('Kesempatan habis. Silahkan menghubungi operator!')
                        else:
                            print(f'Kesempatan anda tersisa {limit3 - i} kali')
            else:
                print('Password Salah!')
                if i == limit2:
                    a = False
                    print('Kesempatan habis. Silahkan menghubungi operator!')
                else:
                    print(f'Kesempatan anda tersisa {limit2 - i} kali')
    else:
        print('Password Salah!')
        if i == limit1:
            a = False
            print('Kesempatan habis. Silahkan menghubungi operator!')
        else:
            print(f'Kesempatan anda tersisa {limit1 - i} kali')


