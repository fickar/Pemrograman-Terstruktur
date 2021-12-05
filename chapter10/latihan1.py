myfile = open('E:test.txt', 'r')
teks = myfile.readlines()
i = 0
ganjil = 0
genap = 0
for x in teks:
    if int(teks[i]) % 2 == 0:
        genap += 1
    else:
        ganjil += 1
    i += 1
print('Banyaknya bilangan genap :', genap)
print('Banyaknya bilangan ganjil:', ganjil)