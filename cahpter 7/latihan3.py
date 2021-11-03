print ('--------------------------------')
print ('   PROGRAM HITUNG RATA - RATA   ')
print ('--------------------------------')

x, jum, n = 0, 0, 0

while 1 > 0 :
    try :
        x = int(input("masukin angka = "))
    except ValueError:
        print('BUKAN BILANGAN BULAT')
        jum -= 0
        x = int(input("masukin angka = "))

    jum += x
    n += 1
    pilihan = str(input('lanjut (y/n) '))

    if pilihan =='n':
        ratarata = jum / n
        print('rata-rata', ratarata)
        break