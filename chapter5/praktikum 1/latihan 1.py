
nilaibind = int(input("nilai bahasa indonesia?"))
nilaimtk = int(input("nilai matematika?"))
nilaiipa = int(input("nilai ipa?"))

if (0 <= nilaiipa <=100) and (0 <= nilaibind <=100) and (0 <= nilaimtk <=100):
    if (nilaiipa > 60) and (nilaimtk > 70) and (nilaibind > 70):
        print("lulus")
    else :
        print("tidak lulus")
else :
    print("tidak valid")

