numbers = input("Please enter three numbers, separated by commas: ")
formattedString = numbers.split(",")
print(formattedString)

int_format = []
for fs in formattedString:
    int_format.append(int(fs))

result = int_format[0] + int_format[1] + int_format[2]
print(result)
