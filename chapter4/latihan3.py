import math
jarak = int(input("jarak a ke b?"))

#sistemhitung
bnykbnsin = jarak / 12
print (bnykbnsin,"liter")


#jika kapasitas tangki 50 l
bnykngisi = bnykbnsin / 50
totalngisi = math.ceil(bnykngisi)
print ("pak budi harus mengisi sebanyak",totalngisi)