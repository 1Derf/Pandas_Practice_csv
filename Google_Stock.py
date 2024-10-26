
# Playing with a CSV file using Python
import csv
from datetime import datetime
path = '/home/derf/PycharmProjects/Pandas_Practice/google_stock.csv'

file = open(path, newline='')
reader = csv.reader(file)
header = next(reader)  # The first line is the header

data = []

for row in reader:
    #row = [Date, Open, High, Low, Close, Volume, Adu.Close]
    date = datetime.strptime(row[0], '%m/%d/%Y')
    open_price = float(row[1])  # 'open' is a builtin function
    high_price = float(row[2])
    low_price = float(row[3])
    close = float(row[4])
    volume = int(row[5])
    adj_close = float(row[6])

    data.append([date, open_price, high_price, low_price, close, volume, adj_close])
    print(data[0])
returns_path ='/home/derf/PycharmProjects/Pandas_Practice/google_return.csv'
file = open(returns_path, 'w')
writer = csv.writer(file)
writer.writerow(['Date', 'Return'])

for i in range(len(data) -1):
    todays_row = data[i]
    todays_date = todays_row[0]
    todays_price = todays_row[-1]
    yesterdays_row = data[i+1]
    yesterdays_price = yesterdays_row[-1]
    daily_return = (todays_price - yesterdays_price) / yesterdays_price
    formatted_date = todays_date.strftime('%m/%d/%Y')
    writer.writerow([formatted_date, daily_return])

