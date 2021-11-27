nilai = [{'nim' : 'A01', 'nama' : 'Agustina', 'mid' : 50, 'uas' : 80},
 	   {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
         {'nim' : 'A03', 'nama' : 'Chicha', 'mid' : 100, 'uas' : 50},
         {'nim' : 'A04', 'nama' : 'Donna', 'mid' : 20, 'uas' : 100},
	   {'nim' : 'A05', 'nama' : 'Fatimah', 'mid' : 70, 'uas' : 100}]

def daftarnilaimhs():
    print("=============================================================")
    print("NIM    NAMA          N.MID      N.UAS     N.AKHIR      STATUS")
    print("-------------------------------------------------------------")
    for x in range(len(nilai)):
        nilaiakh = round(((nilai[x]['mid']) + 2 * (nilai[x]['uas'])) / 3)
        if nilaiakh >= 60:
            STATUS = "LULUS"
        else:
            STATUS = "TIDAK LULUS"
        print(nilai[x]['nim'].ljust(7), end='')
        print(nilai[x]['nama'].ljust(8), end='')
        print(str(nilai[x]['mid']).rjust(11), end='')
        print(str(nilai[x]['uas']).rjust(11), end='')
        print(str(nilaiakh).rjust(12), end='')
        print((STATUS).rjust(12))
    print("-------------------------------------------------------------")
    
daftarnilaimhs()






