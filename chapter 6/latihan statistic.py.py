def sum(*n):
    sum = 0
    for data in n:
        sum+= data
    jumlah = sum
    print(jumlah)

def average(*n):
    average = 0
    i=0
    for x in n:
        average += x
        i += 1
    jumlah = average/i
    print(jumlah)

def maks(*n):
    nilaimax = max(n)
    print(nilaimax)

def minus(*n):
    nilaiminus = min(n)
    print(nilaiminus)



a = ("(5,10,4,9,30,16,2,11)")
#memasukan angka sesuai algoritma (a)
print (" ")
print (a)
print ("jumlah nilai =",end='')," ", sum(5,10,4,9,30,16,2,11)
print("jumlah rata-rata =", end='')," ", average(5,10,4,9,30,16,2,11)
print("nila maksimal =", end='')," ", maks(5,10,4,9,30,16,2,11)
print("nila minimal =", end='')," ",  minus(5,10,4,9,30,16,2,11)

print (" ")
print ("============================================================")
print (" ")


b = ("(81,98,12,83,45,77,69,30,56)")
#memasukan angka sesuai algoritma (b)
print (b)
print ("jumlah nilai =",end='')," ", sum(81,98,12,83,45,77,69,30,56)
print("jumlah rata-rata =",end='')," ", average(81,98,12,83,45,77,69,30,56)
print("nila maksimal =",end='')," ", maks(81,98,12,83,45,77,69,30,56)
print("nila minimal =",end='')," ", minus(81,98,12,83,45,77,69,30,56)

