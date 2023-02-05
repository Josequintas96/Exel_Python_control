import yfinance as yf

print("Hello")

gg = yf.Ticker("DIS")

gg.history(period="max")

gg_in = gg.history_metadata["regularMarketPrice"]

print("PP: ", gg_in)

# gg_info = gg.info["regularMarketPrice"]
# gg_name = gg.info['marketCap']

# print("Docu: ", gg_info)
# print("Name: ", gg_name)



