import math

list =[]
def datastat():
    try:
        n_input = int(input('masukan banyak bilangan yang ingin dimasukan = '))
    except ValueError:
        print("data anda tidak valid")
        n_input = int(input('masukan banyak bilangan yang ingin dimasukan = '))

    for i in range(0, n_input, +1):
        try:
            bil_input = int(input('masukan bilangan = '))
        except ValueError:
            print("data anda tidak valid")
            bil_input = int(input('masukan bilangan = '))

        list.append(bil_input)
    rata2 = sum(list)/n_input
    print("rerata = ",rata2)
    bilmax = max(list)
    print("nilai tertinggi = ",bilmax)
    bilmin = min(list)
    print("nilai terendah = ", bilmin)

datastat()