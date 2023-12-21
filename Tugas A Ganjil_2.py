'''
Tugas 1
'''

# Input waktu awal dlm format jam dan menit
waktu_awal = input('Masukkan waktu awal (hh:mm):')
jam_awal, mnt_awal = map(int,waktu_awal.split(':'))

# Input jumlah jam dan menit yg akan ditambahkan
jam_tmbhn = int(input('Masukkan jam yang ditambahkan:'))
mnt_tmbhn = int(input('Masukkan menit yang ditambahkan:'))

# Jumlahkan waktu
jam_tot = jam_awal + jam_tmbhn
mnt_tot = mnt_awal + mnt_tmbhn

#Penanganan jika mnt >60
if mnt_tot >= 60:
    jam_tot += 1
    mnt_tot -= 60

#Penanganan jika jam >24 (lbih dari sehari)
if jam_tot >= 24:
    jam_tot -= 24

# Format hasil dlm hh:mm
hasil = f"{jam_tot:02d}:{mnt_tot:02d}"

print(f"Waktu sekarang menunjukkan pukul {hasil}")


'''
Tugas 2
'''

# Input waktu awal dlm format jam dan menit
waktu_awal = input('Masukkan waktu awal (hh:mm):')
jam_awal, mnt_awal = map(int,waktu_awal.split(':'))

# Input jumlah jam dan menit yg akan dikurangi
jam_selisih = int(input('Masukkan jam dikurangi:'))
mnt_selisih = int(input('Masukkan menit dikurangi:'))

# Selisih waktu
jam_tot = jam_awal - jam_selisih
mnt_tot = mnt_awal - mnt_selisih

#Penanganan jika mnt >60
if mnt_tot < 0:
    jam_tot -= 1
    mnt_tot += 60

#Penanganan jika jam >24 (lbih dari sehari)
if jam_tot < 0:
    jam_tot += 24

hasil = f"{jam_tot:02d}:{mnt_tot:02d}"

print(f"Waktu sekarang menunjukkan pukul {hasil}")