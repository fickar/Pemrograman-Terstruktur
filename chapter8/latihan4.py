sayur =['bayam','kangkung','wortel','selada']
while 1 > 0:
    menu = str(input('MENU : ''\n'
                     'A. tambah sayur''\n'
                     'B. hapus sayur''\n'
                     'C. tampilkan sayur''\n''\n'
                     'pilihan anda = '))

    if menu =='a' or menu == 'A':
        sayurbaru = str(input("nama sayur yang ditambakan = "))
        sayur.append(sayurbaru)
        print('')
        print('')

    elif menu =='b' or menu == 'B':
        try:
            hapussayur = str(input("hapus sayur = "))
            sayur.remove(hapussayur)
            print('')
            print('')
        except ValueError:
            print('data tidak ditemukan')
            print('')
            print('')

    elif menu =='c' or menu == 'C':
        print('')
        print('')
        print(sayur)
        print('')


    else :
        break
