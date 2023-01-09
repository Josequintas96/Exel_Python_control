
f = open("stocks.txt", "r")
f2 = f.readlines()
print(f2)
for x in f2:
    y1 = x.strip()
    y2 = y1.split()
    print(y2[0])
    #print(x.strip())
f.close()
#print(f.read())


