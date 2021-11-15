nilaiMhs = [{'nim' : 'A01', 'nama' : 'Amir', 'mid' : 50, 'uas' : 80},
            {'nim' : 'A02', 'nama' : 'Budi', 'mid' : 40, 'uas' : 90},
            {'nim' : 'A03', 'nama' : 'Cici', 'mid' : 50, 'uas' : 50},
            {'nim' : 'A04', 'nama' : 'Dedi', 'mid' : 20, 'uas' : 30},
            {'nim' : 'A05', 'nama' : 'Fifi', 'mid' : 70, 'uas' : 40}]
def nilaiTinggi(nilaiMhs):
    a = 0
    b = {}
    d = []
    for c in nilaiMhs:
        uas = c.get('uas')
        mid = c.get('mid')
        nilaiakhir = (mid + 2*uas)/3
        d.append(nilaiakhir)
        if(nilaiakhir>a):
            a = nilaiakhir
            b['nama'] = c.get('nama')
            b['nim'] = c.get('nim')
    print('Nilai tertinggi diraih oleh', b['nama'] ,'(', b['nim'],')','dengan perolehan nilai',max(d))

nilaiTinggi(nilaiMhs)