import csv

filename = 'username.csv'

our_dialect = csv.excel
our_dialect.delimiter = ';'

with open(filename, encoding='UTF-8', newline='') as user_file:
    # headers = ['one', 'two', 'three', 'four', 'five']
    #    reader = csv.DictReader(user_file, delimiter=';') #, fieldnames=headers)
    reader = csv.DictReader(user_file, dialect=our_dialect)

    for row in reader:
        print(row)
