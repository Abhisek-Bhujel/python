a  = int(input('Enter first number: '))
b = int(input('Enter second number: '))

try:
    print(a/b)
except ArithmeticError:
    print("ArithmeticError Occurred")
    
print("Program Executed")