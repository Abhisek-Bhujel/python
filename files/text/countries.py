input_filename = 'country_info.txt'
countries = {}
with open(input_filename) as country_file:
    country_file.readline()
    for row in country_file:
        data = row.strip("\n").split("|")
        country, capital, code, cc3, iac, timezone, currency = data
        # print( country, capital, cc, cc3, IAC, timezone, currency, sep="\n\t")
        country_dict = {
            "Name" : country,
            "Capital" : capital,
            "CC" : code,
            "CC3": cc3,
            "IAC": iac,
            "TimeZone" : timezone,
            "Currency" : currency
        }
        countries[country.casefold()] = country_dict
        countries[code,country.casefold()] = country_dict


print(countries)       
country = input("Which country's capital do you want to know? ")
capital = countries.get(country).get("Capital")
# capital = countries[country]['Capital']


print(f"Capital of {country} is {capital}")