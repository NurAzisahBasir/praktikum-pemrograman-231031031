print('praktikum-a2\n\n')
#Nama, NIM, Kelas
print('Nama    : Nur Azisah Basir')
print('NIM     : 231031031')
print('Prodi   : SI23-A\n')
#Ini Operator Assignment
a = 19
print('Nilai a adalah', a)
a+=3
print('Nilai a+=3 sekarang adalah', a)
print()
a = 19
print('Nilai a adalah', a)
a-=3
print('Nilai a-=3 sekarang adalah', a)
print()
a = 19
print('Nilai a adalah', a)
a*=2
print('Nilai a*=2 sekarang adalah', a)
print()
a = 19
print('Nilai a adalah', a)
a/=2
print('Nilai a/=2 sekarang adalah', a)
print()
a = 3
print('Nilai a adalah', a)
a**=2
print('Nilai a**=2 sekarang adalah', a)
print()
a = 35
print('Nilai a adalah', a)
a%=32
print('Nilai a%=32 sekarang adalah', a)
print()
a = 35
print('Nilai a adalah', a)
a//=32
print('Nilai a//=32 sekarang adalah', a)
print()
#Tugas melanjutkan untuk operator selanjutnya LINE 25- LINE 59
a = 3
print('Nilai a adalah', a)
a&=4
print('Nilai a&=4 sekarang adalah', a)
print()
a = 6
print('Nilai a adalah', a)
a|=3
print('Nilai a|=3 sekarang adalah', a)
print()
a = 7
print('Nilai a adalah', a)
a^=2
print('Nilai a^=2 sekarang adalah', a)
print()
a = 5
print('Nilai a adalah', a)
a>>=3
print('Nilai a>>=3 sekarang adalah', a)
print()
a = 4
print('Nilai a adalah', a)
a<<=4
print('Nilai a<<=4 sekarang adalah', a)
print()


#OPERATOR PERBANDINGAN
a = 9
b = 13
print()
print('\n-----Besar dari 31')
hasil = a >31
print(a,'> 31 adalah', hasil)
hasil = b >31
print(b,'> 31 adalah', hasil)
print()
print('\n-----Kecil dari 31')
hasil = a <31
print(a,'< 31 adalah', hasil)
hasil = b <31
print(b,'< 31 adalah', hasil)
print()
print('\n-----Besar atau sama dari 31')
hasil = a >=31
print(a,'>= 31 adalah', hasil)
hasil = b >=31
print(b,'>= 31 adalah', hasil)
print()
print('\n-----Kecil atau sama dari 31')
hasil = a <=31
print(a,'<= 31 adalah', hasil)
hasil = b <=31
print(b,'<= 31 adalah', hasil)
print()
print('\n-----Sama dari 31')
hasil = a ==31
print(a,'== 31 adalah', hasil)
hasil = b ==31
print(b,'== 31 adalah', hasil)
print()
print('\n-----Tidak sama dari 31')
hasil = a !=31
print(a,'!= 31 adalah', hasil)
hasil = b !=31
print(b,'!= 31 adalah', hasil)
print()

#OPERATOR LOGIKA
a = True
b = False
print('\n=====AND=====')

hasil = a and a
print(a, 'and', a, 'hasilnya=', hasil)
hasil = a and b
print(a, 'and', b, 'hasilnya=', hasil)
hasil = b and a
print(b, 'and', a, 'hasilnya=', hasil)
hasil = b and b
print(b, 'and', b, 'hasilnya=', hasil)

print('\n=====OR=====')

hasil = a or a
print(a, 'or', a, 'hasilnya=', hasil)
hasil = a or b
print(a, 'or', b, 'hasilnya=', hasil)
hasil = b or a
print(b, 'or', a, 'hasilnya=', hasil)
hasil = b or b
print(b, 'or', b, 'hasilnya=', hasil)

print('\n=====XOR=====')

hasil = a ^ a
print(a, 'xor', a, 'hasilnya=', hasil)
hasil = a ^ b
print(a, 'xor', b, 'hasilnya=', hasil)
hasil = b ^ a
print(b, 'xor', a, 'hasilnya=', hasil)
hasil = b ^ b
print(b, 'xor', b, 'hasilnya=', hasil)

print('\n=====NOT=====')

hasil = not a
print('not', a, 'hasilnya=', hasil)
hasil = not b
print('not', b, 'hasilnya=', hasil)

#OPERATOR MEMBERSHIP
print('\n==========IN')
nama = 'Azisah'

test = 'sa'
cek = test in nama
print(test,'terdapat di',nama, 'adalah', cek)

test = 'as'
cek = test in nama
print(test,'terdapat di',nama, 'adalah', cek)
print()
test1 = 'a'
test2 = 'i'
test3 = 'u'
test4 = 'e'
test5 = 'o'

cek = test1 in nama
print(test1, 'terdapat di', nama,'adalah', cek)
cek = test2 in nama
print(test2, 'terdapat di', nama,'adalah', cek)
cek = test3 in nama
print(test3, 'terdapat di', nama,'adalah', cek)
cek = test4 in nama
print(test4, 'terdapat di', nama,'adalah', cek)
cek = test5 in nama
print(test5, 'terdapat di', nama,'adalah', cek)

print('\n==========NOT IN')

cek = test1 not in nama
print(test1, 'tidak terdapat di', nama,'adalah', cek)
cek = test2 not in nama
print(test2, 'tidak terdapat di', nama,'adalah', cek)
cek = test3 not in nama
print(test3, 'tidak terdapat di', nama,'adalah', cek)
cek = test4 not in nama
print(test4, 'tidak terdapat di', nama,'adalah', cek)
cek = test5 not in nama
print(test5, 'tidak terdapat di', nama,'adalah', cek)
print('\n'*2)
