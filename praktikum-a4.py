nim = ['2','3','1','0','3','1','0','3','1']
#nim2 = '231031031'
print(nim,'\n')
#print(nim2[1:3])

# akses item
print(f'item indeks 0:{nim[0]} ')
print(f'item indeks 4:{nim[4]} ')
print(f'item indeks terakhir: {nim[len(nim)-1]}\n')

# akses indeks negatif
print(f'item indeks terakhir: {nim[-1]}')
print(f'item indeks pertama: {nim[-len(nim)]}')
print(f'item indeks 6 [-3]: {nim[-3]}')
print(f'item indeks 4 [-5]: {nim[-5]}')
print(f'item indeks 7 [-2]: {nim[-2]}\n')

# akses indeks batas
print(f'item indeks 1,2,...: \n {nim[1:]}') #ambil semua data dari indeks 3
print(f'item indeks 3,4,...: \n {nim[3:]}')
print(f'item indeks 0,1,2: \n {nim[:3]}') #ambil 3 data dimulai dari indeks awal
print(f'item indeks 0,1,2,3: \n {nim[:4]}')
print(f'item indeks semua: \n {nim[:]}')

print(f'item indeks [:8]: \n {nim[:-1]}')
print(f'item indeks [:6]: \n {nim[:-3]}')

# pengirisan 
print(f'item indeks 1,2: \n {nim[1:3]}')
print(f'item indeks 2,3,4: \n {nim[2:5]}')
print(f'item indeks kosong: \n {nim[3:3]}') #klo sama kanan kirinya it kosong
print(f'item indeks [8:8] kosong: \n {nim[-1:-1]}')
print(f'item indeks [1:8] kosong: \n {nim[1:-1]}')
print(f'item indeks [2:7] kosong: \n {nim[2:-2]}\n\n')

print('\tLATIHAN LIST\n')

data = ['Nur Azisah Basir',2023,'Aktif']
nilai= [90,89,93,97]

print('Nama: '+ data[0])
print('angkatan:', data[1])
print('status: '+ data[2],'\n')

# >> Nur Azisah Basir status Kuliah: Aktif
print(f'{data[0]} status Kuliah: {data[2]}')

# >> Data terbesar nilai adalah: 97
print(f'Data terbesar nilai adalah: {max(nilai)}')

# >> Data terkecil nilai adalah: 89
print(f'Data terkecil nilai adalah: {min(nilai)}')

# >> Rata-rata nilai adalah: 92.25
print(f'Rata-rata nilai adalah: {sum(nilai)/len(nilai)}\n')

print('\tLATIHAN TUPLE\n')

data = ('Nur Azisah Basir',2023,'Aktif')
nilai = (90,89,93,97)

print(data[1])
print(data[-1])
print(nilai[1:-1])
print()
# >> Jumlah nilai mahasiswa adalah: 4
print(f'Jumlah nilai mahasiswa adalah: {len(nilai)}')

# >> Data terbesar nilai adalah: 97
print(f'Data terbesar nilai adalah: {max(nilai)}')

# >> Data terkecil nilai adalah: 89
print(f'Data terkecil nilai adalah: {min(nilai)}')

# >> Rata-rata nilai adalah: 92.25
print(f'Rata-rata nilai adalah: {sum(nilai)/len(nilai)}\n')

print('\tLATIHAN NESTED LIST\n')

data = [['Nur Azisah Basir',2023,'Aktif'],
        [90,89,93,97],
        [20,22],
        ['S1-Reguler','Ganjil\n']]

matkul = ['Matkul1','Matkul2','Matkul3','Matkul4']
sks    = [2,3,3,2]
#Tugas1: Tambahkan matkul dan sks ke dalam data (di akhir)
data.append(matkul)
data.append(sks)

#Mata kuliah 1: Matkul1 dengan jumlah 2 sks
print(f'Mata kuliah 1: {data[-2][0]} dengan jumlah {data[-1][0]} sks')
#Mata kuliah 2: Matkul2 dengan jumlah 3 sks
print(f'Mata kuliah 2: {data[-2][1]} dengan jumlah {data[-1][1]} sks')
#Mata kuliah 3: Matkul3 dengan jumlah 3 sks
print(f'Mata kuliah 3: {data[-2][2]} dengan jumlah {data[-1][2]} sks')
#Mata kuliah 4: Matkul4 dengan jumlah 2 sks
print(f'Mata kuliah 4: {data[-2][3]} dengan jumlah {data[-1][3]} sks')

data[4].append('Matkul5')
data[5].append(2)

#Mata kuliah 5: Matkul5 dengan jumlah...sks
print(f'Mata kuliah 5: {data[-2][4]} dengan jumlah {data[-1][4]} sks')

#Tambahkan 3 matkul dengan sks nya
data[4].append('Matkul6')
data[5].append(3)
data[4].append('Matkul7')
data[5].append(2)
data[4].append('Matkul8')
data[5].append(3)
# print(data)

# Mata kuliah 6: Matkul6 dengan jumlah .. sks
print(f'Mata kuliah 6: {data[-2][5]} dengan jumlah {data[-1][5]} sks')
# Mata kuliah 7: Matkul7 dengan jumlah .. sks
print(f'Mata kuliah 7: {data[-2][6]} dengan jumlah {data[-1][6]} sks')
# Mata kuliah 8: Matkul8 dengan jumlah .. sks
print(f'Mata kuliah 8: {data[-2][7]} dengan jumlah {data[-1][7]} sks\n')

# Tambahkan 8 nilai masing-masing
data[1].append(92)
data[1].append(91)
data[1].append(93)
data[1].append(94)
print(data)

print(data[0][0])
print(data[3][0])
print(data[2][0:],'\n')

# >> Tugas: Nama Mahasiswa Nur Azisah Basir dengan NIM: 231031031
print(f'Nama Mahasiswa {data[0][0]} dengan NIM: {"".join(nim)}')

# >> Program pendidikan Nur Azisah Basir: S1-Reguler
print(f'Program pendidikan {data[0][0]}: {data[3][0]}')

# >> Angkatan : 2023-Ganjil
print(f'Angkatan : {data[0][1]}-{data[3][-1]}')

# >> Jumlah nilai Nur Azisah Basir adalah: 4
print(f'Jumlah nilai {data[0][0]} adalah: {len(data[1])}')

# >> Data terbesar Nur Azisah Basir adalah: 97
print(f'Data terbesar nilai {data[0][0]} adalah: {max(data[1])}')

# >> Data terkecil Nur Azisah Basir adalah: 89
print(f'Data terkecil nilai {data[0][0]} adalah: {min(data[1])}')

# >> Rata-rata nilai Nur Azisah Basir adalah: 92.25
print(f'Rata-rata nilai {data[0][0]} adalah: {sum(data[1])/len(data[1])}\n')




