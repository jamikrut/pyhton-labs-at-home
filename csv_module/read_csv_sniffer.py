import csv

filename = 'username.csv'

with open(filename, 'r', encoding='UTF-8', newline='') as csv_file:
    # Sniffer
    sample = csv_file.read()
    file_dialect = csv.Sniffer().sniff(sample)
    # wracamy na początek pliku
    csv_file.seek(0)
    csv_file.readline().strip('\n').split(';')

    # przekazujemy dialekt który został znaleziony przez Sniffera
    reader = csv.reader(csv_file, quoting=csv.QUOTE_NONNUMERIC, dialect=file_dialect)

    for row in reader:
        print(row)
 