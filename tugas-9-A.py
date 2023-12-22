'''
CONTOH TIPE DATA URUTAN DICTIONARY
'''


Biodata = {'nm':'Nur Azisah Basir',
           'nim':231031031,
           'kls':'SI23-A',
           'ttl':'Pangkajene, 20 Oktober 2005',
           'cp':{'WA':'089519562357',
                 '@':'nurazisahicha02@gmail.com',
                 'IG':'nrazisahb_'},
           'H':'Baca novel'}

print(f'''
Nama\t: {Biodata['nm']}
NIM\t: {Biodata['nim']}
Kelas\t: {Biodata['kls']}
TTL\t: {Biodata['ttl']}
Email\t: {Biodata['cp']['@']}
''')






