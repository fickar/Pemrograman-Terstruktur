#menampilkan bilangan ganjil
print("bilangan bulat ganjil 0 - 100")
for x in range(100):
    if x % 2 == 1:
        print(x)

#menampilkan banyak bilangan ganjil
import math
bnykganjil = (x+1)/2
print("banyak bilangan ganjil ada :",bnykganjil)

#menampilkan jumlah bilangan ganjil
x = 0
for y in range(1, 101, 2):
    x = x + y

print("sn = {}".format(x))
