import random
print("selamat datang di game tebak angka kami, coba tebak bilangan bulat antara 0 s/d 100")

import math
bilacak = random.randint(0,100)
peluang = 100

while peluang > 0:
    data = int(input("Masukan angka tebakan anda :"))
    if (data > bilacak):
        peluang -= 2
        print("Hehehe… Bilangan tebakan anda terlalu besar")

    elif(data < bilacak):
        peluang -= 2
        print("Hehehe… Bilangan tebakan anda terlalu kecil")

    elif(data == bilacak):
        print("SElAMAT, TEBAKAN ANDA BENAR YEAYYYY!!")
        print("SCORE ANDA :",peluang)

if (peluang == 0):
    print("Maaf kesempatan anda telah habis, anda kalah")




