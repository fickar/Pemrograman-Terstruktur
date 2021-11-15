
harga = dict(apel= '5000',
          jeruk= '8500',
          mangga= '7800',
          duku= '6500')

for x in range(0,1,1):
    hargamax = max(harga, key=harga.get)
    print(hargamax)

