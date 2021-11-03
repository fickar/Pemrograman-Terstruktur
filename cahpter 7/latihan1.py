#input
input = str(input("masukan nama file = "))
file =  open (input, "r")

#output
print ('isi  file', input , 'adalah =')

print(file.read())