import yfinance as yf

print("Hello")

gg = yf.Ticker("SPY")

gg_info = gg.info["regularMarketPrice"]

print("Docu: ", gg_info)
