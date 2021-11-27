mhs = ['K001:ROSIHAN ARI:1979-09-01:SOLO',
       'K002:ZULFIKAR H:2002-09-05:PURWOREJO',
       'K003:ANONYMOUS:XXXX-XX-XX:J*****']

print('=========================================================')
print('| NIM  | NAMA MAHASISWA  |   TGL LAHIR   | TEMPAT LAHIR| ')
print('---------------------------------------------------------')
for i in range (len(mhs)):
    a = mhs[i].split(':')
    tgl = a[2].split('-')
    c = (tgl[0])+("/")+(tgl[1])+("/")+(tgl[2])
    print(a[0].ljust(9),end='')
    print(a[1].ljust(18), end='')
    print(c.ljust(15), end='')
    print(a[3])
print('------------------------------------------------------------')