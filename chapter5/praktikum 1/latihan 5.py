#inputdata
kodekaryawan = int(input("Masukkan kode karyawan  : "))
namakaryawan = str(input("Masukkan nama karyawan  : "))
golkaryawan  = str(input("Masukkan golongan       : "))
statusmenikah   = str(input("Apakah anda sudah menikah? [sudah/belum] : "))
if (statusmenikah == 'sudah'):
    statusmenikah = 'sudah menikah'
    tunjangansuamiistri = 1
    sudpnyanak = str(input("apakah sudah memiliki anak? [Y/N] : "))
    if (sudpnyanak == 'Y' or 'y'):
        jmlhanak = int(input("masukan jumlah anak? "))
    elif (sudpnyanak == 'N' or 'n'):
        jmlhanak = 0
elif (statusmenikah == 'belum'):
    tunjangansuamiistri = 0
    jmlhanak = 0

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

#tunjanganpasutri
tunjanganpasutri = 10/100
tunpasutriA = gajiA * (tunjanganpasutri * tunjangansuamiistri)
tunpasutriB = gajiB * (tunjanganpasutri * tunjangansuamiistri)
tunpasutriC = gajiC * (tunjanganpasutri * tunjangansuamiistri)
tunpasutriD = gajiD * (tunjanganpasutri * tunjangansuamiistri)

#tunjangananak
tunjangananak = 5/100
tunanakA = gajiA * (jmlhanak * tunjangananak)
tunanakB = gajiB * (jmlhanak * tunjangananak)
tunanakC = gajiC * (jmlhanak * tunjangananak)
tunanakD = gajiD * (jmlhanak * tunjangananak)

#gajikotor
gajikotorA = gajiA + tunpasutriA + tunanakA
gajikotorB = gajiB + tunpasutriB + tunanakB
gajikotorC = gajiC + tunpasutriC + tunanakC
gajikotorD = gajiD + tunpasutriD + tunanakD

#gajibersih
gajibersihA = gajikotorA - totpotA
gajibersihB = gajikotorB - totpotB
gajibersihC = gajikotorC - totpotC
gajibersihD = gajikotorD - totpotD


#printstrukgaji
if (golkaryawan == 'A'):
    print ("========================================")
    print (           "Struk Gaji Karyawan"          )
    print ("-----------------------------------------")
    print ("Nama Karyawan             :", namakaryawan)
    print ("Golongan                  :", golkaryawan )
    print ("Status Menikah            :", statusmenikah)
    if (statusmenikah == 'sudah menikah'):
        print("Jumlah anak               :", jmlhanak)
    print ("----------------------------------------")
    print ("Gaji Pokok                :", gajiA)
    print ("Tunjangan Suami/Istri     :", tunpasutriA)
    print ("Tunjangan Anak            :", tunanakA)
    print ("----------------------------------------- +")
    print ("Gaji Kotor                :", gajikotorA)
    print ("Potongan","(",potonganA,")","        :"," ",  totpotA)
    print ("----------------------------------------- -")
    print ("Gaji Bersih adalah        : Rp.", gajibersihA)

elif (golkaryawan == 'B'):
    print("========================================")
    print("Struk Gaji Karyawan")
    print("-----------------------------------------")
    print("Nama Karyawan             :", namakaryawan)
    print("Golongan                  :", golkaryawan)
    print("Status Menikah            :", statusmenikah)
    if (statusmenikah == 'sudah menikah'):
        print("Jumlah anak               :", jmlhanak)
    print("----------------------------------------")
    print("Gaji Pokok                :", gajiB)
    print("Tunjangan Suami/Istri     :", tunpasutriB)
    print("Tunjangan Anak            :", tunanakB)
    print("----------------------------------------- +")
    print("Gaji Kotor                :", gajikotorB)
    print("Potongan","(", potonganB,")","          :","", totpotB)
    print("----------------------------------------- -")
    print("Gaji Bersih adalah        : Rp.", gajibersihB)

elif (golkaryawan == 'C'):
    print("========================================")
    print("Struk Gaji Karyawan")
    print("-----------------------------------------")
    print("Nama Karyawan             :", namakaryawan)
    print("Golongan                  :", golkaryawan)
    print("Status Menikah            :", statusmenikah)
    if (statusmenikah == 'sudah menikah'):
        print("Jumlah anak               :", jmlhanak)
    print("----------------------------------------")
    print("Gaji Pokok                :", gajiC)
    print("Tunjangan Suami/Istri     :", tunpasutriC)
    print("Tunjangan Anak            :", tunanakC)
    print("----------------------------------------- +")
    print("Gaji Kotor                :", gajikotorC)
    print("Potongan","(", potonganC,")","        :","", totpotC)
    print("----------------------------------------- -")
    print("Gaji Bersih adalah        : Rp.", gajibersihC)

elif (golkaryawan == 'D'):
    print("========================================")
    print("Struk Gaji Karyawan")
    print("-----------------------------------------")
    print("Nama Karyawan             :", namakaryawan)
    print("Golongan                  :", golkaryawan)
    print("Status Menikah            :", statusmenikah)
    if (statusmenikah == 'sudah menikah'):
        print("Jumlah anak               :", jmlhanak)
    print("----------------------------------------")
    print("Gaji Pokok                :", gajiD)
    print("Tunjangan Suami/Istri     :", tunpasutriD)
    print("Tunjangan Anak            :", tunanakD)
    print("----------------------------------------- +")
    print("Gaji Kotor                :", gajikotorD)
    print("Potongan", "(", potonganD, ")", "          :"," ", totpotD)
    print("----------------------------------------- -")
    print("Gaji Bersih adalah        : Rp.", gajibersihD)

