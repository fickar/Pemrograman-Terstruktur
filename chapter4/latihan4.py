inputjarakab = int(input("jarak a-b?"))
inputrkecab = int(input("rata-rata kec?"))
inputjarakbc = int(input("jarak b-c?"))
inputrkeccb = int(input("rata-rata kec?"))
inputwaktu = float(input("waktu berangkat?"))
inputwaktuistirahat = int(input("brp lama waktu istirahat?"))

#perhitungan
akeb = (inputjarakab*1000)/(inputrkecab*1000/60)
totalab = round(akeb)
bkec = (inputjarakbc*1000)/(inputrkeccb*1000/60)
totalbc = round(bkec)

totalwaktu = round(akeb + bkec + inputwaktuistirahat)
print(totalwaktu,'menit')
totaljam = (totalwaktu / 60)

#hasil
drakec = (inputwaktu + totaljam)
print('jam', drakec)



