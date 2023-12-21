nama = 'nur azisah basir'
NIM = '231031031'
meet = 'praktikum 3'
prodi = 'sistem informasi a'
email = 'nurazisahicha02@gmail.com'
sp = 50
print('-'*sp)
print(nama.center(sp).upper())
print(NIM.center(sp))
print('\n'*2)
print(meet.capitalize().rjust(sp))
print(prodi.title().rjust(sp))
print(email.rjust(sp))
print('-'*sp)
print('\n')
print(f'''Halo, nama saya {nama.capitalize()}, dengan NIM {NIM}
dari prodi {prodi.title()} ,ini adalah file {meet.capitalize()}.\nTerima kasih.\n''')
ttl = 'Pangkajene, 20 Oktober 2005'
alamat = 'Jl. Ganggawa No.151 c'
asal = 'Pangkajene, Sidrap'
hobi = 'Membaca novel'
tinggi = '152'
print(f'''Biodata saya :

Nama\t:{nama.title()}
NIM\t:{NIM}
Prod\t:{prodi.title()}
TTL\t:{ttl}
Alamat\t:{alamat}
Asal\t:{asal}
Hobi\t:{hobi}
Tinggi\t:{tinggi} cm\n\n''')
stat = 'sir issac newton Frankel'
up = stat.upper()
print(up)
up = up.split() #up mnjd list n item
print()
#target N SIR ISSAC
print(up[2])
print(up[2][0],up[0],up[1])
print()
#target NEWTON S
print(up[2],up[0][0],up[1][0])
print()
#target F SIR ISSAC NEWTON
print(up[-1][0],' '.join(up[0:-1]))
print()

stat2 = '&sir$ @issac# *newton.'
#target SIR ISSAC NEWTON
up2 = stat2.upper()
print(up2)
up2 = up2.split()
print(up2) #mnjd list
print(up2[0][1:-1],up2[1][1:-1],up2[2][1:-1])
'''SAMA JI'''
print(up2[0].strip('&$'),up2[1].strip('@#'),up2[2].strip('*.'))






 
