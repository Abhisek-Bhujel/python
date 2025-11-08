import csv

csv_filename = 'OlympicMedals_2020.csv'

with open(csv_filename, encoding='utf-8', newline='') as csv_file:
    header = csv_file.readline().strip('\n').split(',')
    print(f'Column: {header}')
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)
