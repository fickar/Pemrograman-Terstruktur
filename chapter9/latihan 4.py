import string
import random

def ubahhuruf(teks, a):
    mylist = list(set(teks))
    output = []
    for i in range (a):
        q = ''.join(random.sample(mylist, len(mylist)))
        if q in mylist:
            continue
        else:
            output.append(q)
    print(output)

ubahhuruf('aku', 3)