from math import sqrt

def pythagoras(a, b, c):
    c = sqrt(a*a + b*b)
    return c

a = int(input("nilai a?"))
b = int(input("nilai b?"))

c = int(input("nilai c?"))

if c == pythagoras(a,b,c):
    print("a =", a,",", "b =", b,",", "c =", c,"->", "true")
else:
    print("a =", a,",", "b =", b,",", "c =", c, "->", "false")



