import yfinance as yf

f = open("stocks.txt", "r")
f2 = f.readlines()
# print(f2)
f.close()

for x in f2:
    y1 = x.strip()
    y2 = y1.split()
    gg = yf.Ticker(y2[0])
    gg_info = gg.info["regularMarketPrice"]
    print(y2[0], ": $", gg_info)
    #print(x.strip())
