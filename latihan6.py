def sortstringbychar(mydata):
    for i in range(len(mydata)):
        for j in range(len(mydata)):
            if len(mydata[i])>len(mydata[j]):
                mydata[j], mydata[i] = mydata[i],  mydata[j]
    print(mydata)

mydata = ['apel','rambutan','jeruk',]
sortstringbychar(mydata)


