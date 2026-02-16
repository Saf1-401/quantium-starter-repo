import csv

data_files = ['daily_sales_data_0.csv','daily_sales_data_1.csv','daily_sales_data_2.csv']

with open('../data/full_daily_sales_data.csv', mode='w', newline='') as csv_file_full:
  fieldnames = ['sales','date','region']
  csv_writer = csv.DictWriter(csv_file_full, fieldnames)
  csv_writer.writeheader()

  for file in data_files:
    with open("../data/"+file, mode='r') as csv_file:
      csv_reader = csv.DictReader(csv_file)
      for row in csv_reader:
        if row['product'] == 'pink morsel':
          sales = float(row['price'][1:]) * int(row['quantity'])
          csv_writer.writerow({'sales': sales, 'date': row['date'], 'region': row['region']})