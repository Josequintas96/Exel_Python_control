
f = open("stocks.txt", "r")
f2 = f.readlines()
print(f2)
y3 = []
for x in f2:
    y1 = x.strip()
    y2 = y1.split()
    print(y2[0])
    # y2[1] = str(int(y2[1])+1) 
    y3.append(y2)
    #print(x.strip())
f.close()

print("1. to increase")
print("2. to decrease")
print("3. Nothing")
kk = input("What action do you desired: " )

if int(kk)==1:
    print("\t Increse")
    for x in y3:
        x[1] = str(int(x[1])+1) 
elif int(kk)==2:
    print("\t Decrease")
    for x in y3:
        x[1] = str(int(x[1])-1) 
elif int(kk) ==0:
    print("\t Nothing")
    print("kk3: ",y3)
else:
    print("\t Wrong input")
    

print(y3)

f = open("stocks.txt", "w")
for x in y3:
    strX = x[0] + " " + x[1] +"\n"
    f.write(strX)
f.close()





