list = []

def kuadrat(bil):
    n_bil = len(bil)
    for i in range(n_bil):
        pangkat = bil[i] * bil[i]
        list.append(pangkat)
    print(bil)
    print('hasil kuadrat = ', list)
    return list

bil = [2, 4, 5, 6]
kuadrat(bil)