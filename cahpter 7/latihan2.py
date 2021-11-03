#input
file =  open (str(input("masukan nama file = ")), "a")
inputdata = file.write(str(input("data yang mau dimasukan = ")))

while (0 < 1):
    yesornot = str(input('mau lagi (y/n) = '))
    if yesornot =='y':
        inputdata = file.write(str(input("data yang mau dimasukan = ", " ")))
    else:
        file.close()
        break