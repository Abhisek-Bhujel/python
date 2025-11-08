import csv

input_filename = 'country_info.txt'

with open(input_filename, encoding='utf-8', newline='') as countries_data:
    sample = ""
    for i in range(3):
       sample +=  countries_data.readline()
    country_dialect = csv.Sniffer().sniff(sample)
    countries_data.seek(0)
    reader = csv.reader(countries_data, dialect = country_dialect)
    for row in reader:
        print(row)
        
print('*' * 80)

attributes = ['delimiter',
              'doublequote',
              'escapechar',
              'lineterminator',
              'quotechar',
              'quoting',
              'skipinitialspace']

for attribute in attributes:
    print(f'{attribute}: {getattr(country_dialect, attribute)}');