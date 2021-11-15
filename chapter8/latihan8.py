
harga = dict(apel= 5000,
          jeruk= 8500,
          mangga= 7800,
          duku= 6500)

c = []
def rata2():
    for key in harga:
        b = (harga[key])
        c.append(b)
    d = (sum(c))
    e = len(harga)
    ratarata = d/e
    print(ratarata)


rata2()