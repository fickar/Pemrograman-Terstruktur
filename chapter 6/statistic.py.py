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



#masukan beberapa nilai
sum(1,2,3,4,5)
average(1,2,3,4,5)
maks(1,2,3,4,5)
minus(1,2,3,4,5)

