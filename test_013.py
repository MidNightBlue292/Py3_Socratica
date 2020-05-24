import csv
from datetime import datetime
original_path = 'google_stock_data.csv'
returns_path = 'google_returns_data.csv'
top_line = list()
data = dict()
with open(original_path) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            top_line = row
            line_count += 1
        else:
            # row = [date, open_price, high, low, close, volume, adj_close]
            data.clear()
            d = datetime.strptime(row[0], '%m/%d/%Y')
            data['Data'] = d
            data['Open'] = float(row[1])
            data['High'] = float(row[2])
            data['Low'] = float(row[3])
            data['Close'] = float(row[4])
            data['Volume'] = int(row[5])
            data['Adj_Close'] = float(row[6])
            line_count += 1

print(top_line)
for k, v in data.items():
    print(k, v)
print(f'Processed {line_count - 1} lines of data.')
