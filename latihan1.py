list = []
total_n = int(input("masukan banyak bilangan yang mau diinput = "))
for i in range(0, total_n, +1):
    bilangan = int(input('masukan angka = '))
    list.append(bilangan)

print('')
print(list)
list.sort(reverse=True)
print('')
print('jika diurutkan dari belakang ')
print('')
print(list)