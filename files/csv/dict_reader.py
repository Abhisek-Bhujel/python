import csv
input_filename = 'country_info.txt'

dialect = csv.excel
dialect.delimiter = '|'
countries = {}
with open(input_filename, encoding= 'utf-8', newline= '') as country_file:
    headings = country_file.readline().strip('\n').split(dialect.delimiter)
    dict_reader = csv.DictReader(country_file, delimiter='|', fieldnames=headings)
    for row in dict_reader:
        countries[row['Country'].casefold()] = row
        countries[row['CC'].casefold()] = row


print(countries)       
country = input("Which country's capital do you want to know? ")
capital = countries.get(country).get("Capital")
print(f"Capital of {country} is {capital}")