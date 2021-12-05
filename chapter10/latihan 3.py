text = open('e:fikar3.txt', 'r')
line = text.readlines()
dict = {}
listD = []
for i in range(len(line)) :
    a = line[i].split('|')
    a[2] = a[2].replace('\n', '')
    dict = {'nim' : a[0], 'nama' : a[1], 'alamat' : a[2]}
    listD.append(dict)
print(listD)