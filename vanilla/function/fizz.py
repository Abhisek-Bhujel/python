def fizz_buzz(i: int) -> str:
    """Return string based on the number divisibility

    Args:
        number (int): number to be checked

    Returns:
        str: returned based on the divisibility
    """
 
    if i%3 == 0 and i%5 ==0:
        return "fizz buzz"
    elif i%3 == 0:
        return "fizz"
    elif i%5 == 0:
        return "buzz"
    else:
        return str(i)
        
        
for i in range(1,100):
    print(fizz_buzz(i))
            