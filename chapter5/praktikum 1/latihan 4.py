#inputdata
kodekaryawan = int(input("Masukkan kode karyawan  : "))
namakaryawan = str(input("Masukkan nama karyawan  : "))
golkaryawan  = str(input("Masukkan golongan       : "))

#gajipokok
gajiA = 10000000
gajiB = 8000000
gajiC = 7000000
gajiD = 5500000

#potongan
potonganA = '2.5%'
potonganB = '2%'
potonganC = '1.5%'
potonganD = '1%'

#totalpotongan
totpotA = (10000000 * 2.5/100)
totpotB = (8000000 * 2/100)
totpotC = (7000000 * 1.5/100)
totpotD = (5500000 * 1/100)

#gajibersih
gajibersihA = gajiA - totpotA
gajibersihB = gajiB - totpotB
gajibersihC = gajiC - totpotC
gajibersihD = gajiD - totpotD



if (golkaryawan == 'A'):
    print ("========================================")
    print (           "Struk Gaji Karyawan"          )
    print ("-----------------------------------------")
    print ("Nama Karyawan             :", namakaryawan)
    print ("Golongan                  :", golkaryawan)
    print ("----------------------------------------")
    print ("Gaji Pokok                :", gajiA)
    print ("Potongan","(",potonganA,")","        :"," ",  totpotA)
    print ("----------------------------------------- -")
    print ("Gaji Bersih adalah        : Rp.", gajibersihA)

elif (golkaryawan == 'B'):
    print("========================================")
    print("Struk Gaji Karyawan")
    print("-----------------------------------------")
    print("Nama Karyawan             :", namakaryawan)
    print("Golongan                  :", golkaryawan)
    print("----------------------------------------")
    print("Gaji Pokok                :", gajiB)
    print("Potongan","(", potonganB,")","          :","", totpotB)
    print("----------------------------------------- -")
    print("Gaji Bersih adalah        : Rp.", gajibersihB)

elif (golkaryawan == 'C'):
    print("========================================")
    print("Struk Gaji Karyawan")
    print("-----------------------------------------")
    print("Nama Karyawan             :", namakaryawan)
    print("Golongan                  :", golkaryawan)
    print("----------------------------------------")
    print("Gaji Pokok                :", gajiC)
    print("Potongan","(", potonganC,")","        :","", totpotC)
    print("----------------------------------------- -")
    print("Gaji Bersih adalah        : Rp.", gajibersihC)

elif (golkaryawan == 'D'):
    print("========================================")
    print("Struk Gaji Karyawan")
    print("-----------------------------------------")
    print("Nama Karyawan             :", namakaryawan)
    print("Golongan                  :", golkaryawan)
    print("----------------------------------------")
    print("Gaji Pokok                :", gajiD)
    print("Potongan", "(", potonganD, ")", "          :"," ", totpotD)
    print("----------------------------------------- -")
    print("Gaji Bersih adalah        : Rp.", gajibersihD)

