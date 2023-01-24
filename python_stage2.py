import yfinance as yf

print("Hello")

gg = yf.Ticker("DIS")

gg_info = gg.info["regularMarketPrice"]

print("Docu: ", gg_info)


