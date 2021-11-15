harga = dict(apel= 5000,
          jeruk= 8500,
          mangga= 7800,
          duku= 6500)

while 1>0:
    menu = str(input('MENU : ''\n'
                     'A. tambah data buah''\n'
                     'B. beli buah''\n'
                     'C. exit''\n'
                     '        ''\n'
                     'masukan pilihan anda = '))

    if menu == 'a'or menu == 'A':
        f = str(input("masukan data buah = "))
        g = int(input("masukan harga = "))
        harga.update({f: g})
        print(harga)
        print('')
        print('')

    elif menu == 'b' or menu =='B':
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
                print('')
                print('')
                break

    elif menu == 'c' or menu == 'C':
        break



