print('Tugas Praktikum 3'.center(40))
nama = 'Nur Azisah Basir'
nim  = '231031031'
prodi= 'Sistem Informasi A'
print(f'''
Nama\t: {nama}
NIM\t: {nim}
prodi\t: {prodi}\n\n''')


'''Dari beberapa string berikut, buatkan manipulasi kode
agar hasil outputnya sesuai'''


str1 = 'duFort Frankel Von Neumann'
#output: NEUMANN DUFORT FRANKEL VON
new1 = str1.upper()
new1 = new1.split()
print(new1)
print('str1')
print(new1[-1],new1[0],new1[1],new1[2])
print(new1[-1],' '.join(new1[:3]),'\n')

str2 = 'duFort Frankel Von Neumann'
#output: DFV NEUMANN
print('str2')
print(new1[0][0]+new1[1][0]+new1[2][0],new1[3],'\n')

str3 = 'duFort Frankel Von Neumann'
#output: DUFORT FVN
print('str3')
print(new1[0],new1[1][0]+new1[2][0]+new1[3][0],'\n')

str4 = 'duFort Frankel Von Neumann'
#output: N duFort FV
print('str4')
new4 = str4.split()
print(new4[3][0],new4[0],new4[1][0]+new4[2][0],'\n')

str5 = 'duFort Frankel Von Neumann'
#output: NEUMANN d f v
print('str5')
str5 = str5.casefold().split()
print(new1[-1],str5[0][0],str5[1][0],str5[2][0],'\n')

str6 = 'duFort Frankel Von Neumann'
#output: NEUMANN DFV
print('str6')
print(new1[-1],new1[0][0]+new1[1][0]+new1[2][0],'\n')

str7 = '@duFort Frankel Von Neumann$'
#output: duFort Frankel Von NEUMANN
print('str7')
str7 = str7.strip('@$').split()
up7 = str7[-1].upper()
str7 = str7[:3]
print(' '.join(str7),up7,'\n')

str8 = '#duFort4Frankel4Von4Neumann$'
#output: duFort Frankel Von Neumann
print('str8')
str8 = str8.replace('4',' ')
print(str8.strip('#$'),'\n')

str9 = '@duFort@-^Frankel*-(Von(-(Neumann$'
#output: duFort Frankel Von Neumann
print('str9')
str9 = str9.split('-')
print(str9[0].strip('@'),str9[1].strip('^*'),str9[2].strip('('),str9[3].strip('($'))
print()

str10 = '@DUFort@1^FraNkel*1(VoN(1(NeuMann^'
#output: duFort Frankel Von Neumann
print('str10')
str10 = str10.split('1')
up10_1 = str10[0][:3].casefold().strip('@')
up10_1 = up10_1+str10[0][3:].strip('@')
up10_2 = str10[1].title().strip('^*')
up10_3 = str10[2].title().strip('(')
up10_4 = str10[3].title().strip('(^')
print(up10_1,up10_2,up10_3,up10_4,'\n'*2)

