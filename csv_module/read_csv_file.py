import csv

filename = 'username.csv'

with open(filename, 'r', encoding='UTF-8', newline='') as csv_file:
    header = csv_file.readline().strip('\n').split(';')
    reader = csv.reader(csv_file, delimiter=';', quoting=csv.QUOTE_NONNUMERIC)
    for row in reader:
        print(row)
