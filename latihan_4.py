pndptn = int(input('Masukkan besaran pendapatan: '))

if pndptn <= 1000 :
    persentase = 0
elif pndptn <= 2000 :
    persentase = 10
elif pndptn <= 3000 :
    persentase = 20
elif pndptn <= 4000 :
    persentase = 30
elif pndptn <= 5000 :
    persentase = 40
elif pndptn >= 5001 :
    persentase = 50

bonus = pndptn*(persentase/100)
tot = pndptn+bonus

print('\nPendapatan : ', pndptn)
print(f'Persentase : {persentase}%')
print('Bonus : ', bonus)
print('Total Pendapatan : ', tot)


