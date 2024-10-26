import pandas as pd
google_stocks = pd.read_csv('/home/derf/PycharmProjects/Derfcave/google_stock.csv', index_col='Date')
#google_updated = list(google_stocks)
#print(google_stocks.head())
#google_stocks.info()
#google_stocks.info()
#google_stocks.shape()
#google_stocks.sort_values(by=['Open'], ascending=False)
(google_stocks['Low'] == 103.880180)



print(google_stocks)
