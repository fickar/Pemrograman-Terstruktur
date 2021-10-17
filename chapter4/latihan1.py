#persewaanmobil
print("selamat datang dipersewaan mobil kami")
print("mau sewa berapa lama?")

#input lama menyewa
jamsewa = int(input("dari jam :"))
menitsewa = int(input(" menit:"))
jamkembali = int(input("sampai jam:"))
menitkembali = int(input("jam:"))

#perhitungan
totaljam = jamkembali - jamsewa
totalmenit = menitkembali - menitsewa
totalpinjam = totaljam * 60 + totalmenit


#harga
if (totalpinjam == 720):
    print("200.000")
elif (totalpinjam < 720):
    print("200.000")
elif ("totalpinjam > 720"):
    totalpinjam = int((totalpinjam - 720)*166.67+200000)
    print("Rp",totalpinjam)






