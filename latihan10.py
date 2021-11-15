
harga = dict(apel= 5000,
          jeruk= 8500,
          mangga= 7800,
          duku= 6500)

jum = 0
while 1 > 0:
    if 1 > 0:
        print(harga)
        a = (harga.get(input("Nama buah yang dibeli = ")))
        b = int(input("Berapa Kg             = "))
        print('=============================')
        c = a*b
    jum += c
    pilihan = str(input('lanjut (y/n) '))

    if pilihan =='n':
        print("total harga           =",jum)


