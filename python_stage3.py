

f = open("stocks.txt", "r")
f2= f.read()
print(f2)
f.close()


f = open("stocks.txt", "r")
f2 = f.readlines()
print(f2)
for x in f2:
	print(x.strip())
f.close()
#print(f.read())
