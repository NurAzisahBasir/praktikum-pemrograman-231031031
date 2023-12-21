''' UTS
1. Buat variabel jenis list berikut.
    
    Bio =  ['Institut Teknologi Bacharuddin Jusuf Habibie', 0
            'Parepare', 1
            'Jurusan Sains', 2
            'kartu hasil studi mahasiswa', 3
            'Nama Lengkap', 4
            'NIM', 5
            'S1', 6
            'Sistem Informasi A', 7
            '2023-2024', 8
            'ganjil', 9
            'aktif', 10
            'Tanggal-Bulan-Tahun Lahir'] 11
#(NOTED: sesuaikan dengan data anda)


2. Buat variabel nested list berikut.

MK =   [['Matkul1','Matkul2','Matkul3','Matkul4','Matkul5','Matkul6','Matkul7','Matkul8'],
        [3,2,3,2,3,3,3,2],
        ['22A1209','22A1210','22A1211','22A1212','22A1213','22A1214','22A1215','22A1216'],
        [3.50,3.00,3.75,4.00,3.75,3.50,3.75,3.00]]

#(NOTED: Ubah Nama Matakuliah, Jumlah SKS, dan Nilai)

3. Buat Kode dengan hasil runing seperti berikut.


            INSTITUT TEKNOLOGI BACHARUDDIN JUSUF HABIBIE
                           JURUSAN SAINS
                    KARTU HASIL STUDI MAHASISWA
                          GANJIL 2023/2024

                    
Nama Lengkap    : NAMA LENGKAP
NIM             : NIM
Program/Prodi   : S1/Sistem Informasi A
Tahun Masuk     : 2023-Ganjil
Status          : Aktif
|--|--   12   --|--             31            --|-- 7 --|--    13   --|
-----------------------------------------------------------------------
No. Kode        |           Mata Kuliah         |  SKS  | Nilai (0-4) |
-----------------------------------------------------------------------
1   22A1209     | Matkul1                       |   3   |         3.50|
2   22A1210     | Matkul2                       |   2   |         3.00|
3   22A1211     | Matkul3                       |   3   |         3.75|
4   22A1212     | Matkul4                       |   2   |         4.00|
5   22A1213     | Matkul5                       |   3   |         3.75|
6   22A1214     | Matkul6                       |   3   |         3.50|
7   22A1215     | Matkul7                       |   3   |         3.75|
8   22A1216     | Matkul8                       |   2   |         3.00|
-----------------------------------------------------------------------
                                       TOTAL SKS:   21
-----------------------------------------------------------------------
|---------------------------------71-----------------------------------|
Summary:
Jumlah Mata Kuliah : 8 Mata Kuliah
Nilai Tertinggi    : 4.00  (22A1212 - Matkul4)
Nilai Terendah     : 3.00  (22A1211 - Matkul2)
IP Kumulatif       : 3.00
                                   
                                               Parepare, 25 Oktober 2023



                                                     NAMA LENGKAP      
                                                     ------------
'''



# Tulis Kode Jawaban di bawah!

Bio =  ['Institut Teknologi Bacharuddin Jusuf Habibie',
            'Parepare',
            'Jurusan Sains',
            'kartu hasil studi mahasiswa',
            'Nur Azisah Basir',
            '231031031',
            'S1',
            'Sistem Informasi A',
            '2023-2024',
            'ganjil',
            'aktif',
            '20-Oktober-2005']

MK =   [['Pengantar Teknologi Informasi','Pemgantar Pemrograman','Pendidikan Pancasila','Kalkulus Dasar','Pendidikan Bahasa Indonesia','Pendidikan Agama Islam','Wawasan CINTA dan IMTAQ','SAINS Terpadu'],
        ['3','3','2','2','2','3','2','3'],
        ['22A1209','22A1210','22A1211','22A1212','22A1213','22A1214','22A1215','22A1216'],
        ['3.50','3.00','3.75','4.00','3.75','3.50','3.75','3.00']]

jrk = '|--|--   12   --|--             31            --|-- 7 --|--    13   --|'
jrk = len(jrk)

print(f'''{Bio[0].center(jrk).upper()}
{Bio[2].center(jrk).upper()}
{Bio[3].center(jrk).upper()}
{(Bio[-3].upper()+' '+Bio[-4].replace('-','/')).center(jrk)}


Nama Lengkap\t: {Bio[4].upper()}
NIM\t\t: {Bio[5]}
Program/Prodi\t: {Bio[6]+'/'+Bio[7]}
Tahun Masuk\t: {Bio[-4][0:5]+Bio[-3].capitalize()}
Status\t\t: {Bio[-2].capitalize()}

''')
print('-'*(jrk))
print('No. '+'Kode'.ljust(12)+'|'+'Mata Kuliah'.center(31)+'|'+'SKS'.center(7)+'|'+'Nilai(0-4)'.center(13))
print('-'*(jrk))
print('1. '+'|'+MK[2][0].ljust(12)+'|'+MK[0][0].ljust(31)+'|'+MK[1][0].center(7)+'|'+MK[3][0].rjust(13))
print('2. '+'|'+MK[2][1].ljust(12)+'|'+MK[0][1].ljust(31)+'|'+MK[1][1].center(7)+'|'+MK[3][1].rjust(13))
print('3. '+'|'+MK[2][2].ljust(12)+'|'+MK[0][2].ljust(31)+'|'+MK[1][2].center(7)+'|'+MK[3][2].rjust(13))
print('4. '+'|'+MK[2][3].ljust(12)+'|'+MK[0][3].ljust(31)+'|'+MK[1][3].center(7)+'|'+MK[3][3].rjust(13))
print('5. '+'|'+MK[2][4].ljust(12)+'|'+MK[0][4].ljust(31)+'|'+MK[1][4].center(7)+'|'+MK[3][4].rjust(13))
print('6. '+'|'+MK[2][5].ljust(12)+'|'+MK[0][5].ljust(31)+'|'+MK[1][5].center(7)+'|'+MK[3][5].rjust(13))
print('7. '+'|'+MK[2][6].ljust(12)+'|'+MK[0][6].ljust(31)+'|'+MK[1][6].center(7)+'|'+MK[3][6].rjust(13))
print('8. '+'|'+MK[2][7].ljust(12)+'|'+MK[0][7].ljust(31)+'|'+MK[1][7].center(7)+'|'+MK[3][7].rjust(13))
print('-'*(jrk))

matakuliah, sks, kode_matakuliah, nilai = MK

a = MK[1]
b = [int(p) for p in a]
print('TOTAL SKS:'.rjust(49),' ',sum(b))
print('-'*(jrk),'\n'*2)

n = MK[3]
m = [float(q) for q in n]

print("Summary:")
print(f"Jumlah Mata Kuliah : {len(matakuliah)} Mata Kuliah")
print(f"Nilai Tertinggi    : {max(nilai)}  ({kode_matakuliah[nilai.index(max(nilai))]} - {matakuliah[nilai.index(max(nilai))]})")
print(f"Nilai Terendah     : {min(nilai)}  ({kode_matakuliah[nilai.index(min(nilai))]} - {matakuliah[nilai.index(min(nilai))]})")
print(f"IP Kumulatif       : {sum(m) / len(m)}\n")

print(f"{Bio[1].rjust(54)}, 25 Oktober 2023\n\n")
print(f"{Bio[4].upper().rjust(jrk)}")











