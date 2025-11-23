def sum_numbers(*args :int | float) -> int| float:
    """ Calculate sum"""
    return sum(args)
        
print(sum_numbers(1,2,3,4,5))
print(sum_numbers(1.2,2.8,3.7,4.9,5.1))