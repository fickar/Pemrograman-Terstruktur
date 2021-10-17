nilaibind = int(input("nilai bahasa indonesia?"))
nilaimtk = int(input("nilai matematika?"))
nilaiipa = int(input("nilai ipa?"))

if (0 <= nilaiipa <=100) and (0 <= nilaibind <=100) and (0 <= nilaimtk <=100):
    if (nilaiipa > 60) and (nilaimtk > 70) and (nilaibind > 60):
        print("lulus")
    else :
        print("tidaklulus")
        if (nilaiipa < 60):
            print("Nilai ipa  kurang dari 60")
        elif (nilaibind < 60):
            print("Nilai bahasa indonesia kurang dari 60")
        elif (nilaimtk < 70):
            print("Nilai matematika kurang dari 70")

else :
    print("tidak valid")