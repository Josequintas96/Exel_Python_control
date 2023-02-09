import yfinance as yf

print("Hello")

gg = yf.Ticker("DIS")



# gg.history(period="max")

# gg_in = gg.history_metadata["regularMarketPrice"]

# print("PP: ", gg_in)

try:
    info = gg.info['longName']
except:
    info = "DIS"

print("TT: ", info)

# for t in ["MSFT", "FAKE"]:
#     ticker = yf.Ticker(t)
#     print(ticker)
#     # # info = ticker.history_metadata["regularMarketPrice"]
#     # if (ticker.fast_info == None):
#     #     raise NameError("You did not input a correct stock ticker! Try again.")
#     # else:
#     #     info = ticker.history_metadata["regularMarketPrice"]
#     #     print("\n \nThe Ticker ", t, "  =>  " , info , " was chosen \n \n")

#     try:
#         info = ticker.fast_info['last_price']
#     except:
#         print(f"Cannot get info of {t}, it probably does not exist")
#         continue
#     print(t, " does exist")



# listX = ["Super", "Boris", "Bor", "Almond", "Dragon", "Zorro", "Zorra", "Pepe"]

# print(listX)

# listX.sort()

# print(listX)


# class Bob: 
#     name =""
    
#     def __init__(self, name):
#         self.name = name
        
#     def return_Bob(self):
#         return self.name
    
# ListBob = []
# Bob1 = Bob("Super")
# ListBob.append(Bob1)
# Bob2 = Bob("Boris")
# ListBob.append(Bob2)
# Bob3 = Bob("Bor")
# ListBob.append(Bob3)
# Bob4 = Bob("Almond")
# ListBob.append(Bob4)
# Bob5 = Bob("Dragon")
# ListBob.append(Bob5)
# Bob6 = Bob("Zorro")
# ListBob.append(Bob6)
# Bob7 = Bob("Zorra")
# ListBob.append(Bob7)
# Bob8 = Bob("Pepe")
# ListBob.append(Bob8)

# def printBob(listS):
#     for x in listS:
#         print(x.name + " => ", end="")
#     print()
        
# printBob(ListBob)

# ListBob.sort(key=lambda x: x.name, reverse=False)
# printBob(ListBob)






# # gg_info = gg.info["regularMarketPrice"]
# # gg_name = gg.info['marketCap']

# # print("Docu: ", gg_info)
# # print("Name: ", gg_name)



