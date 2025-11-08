def fibonacci(n):
    """ Return the n fibonacci number for positive n

    Args:
        n (int): positive integer
    """
    if 0 <= n <= 1:
        return n
    
    n_minus1, n_minus2 = 1, 0
    result = None
    for f in range(n -1):
        result = n_minus2 +n_minus1
        n_minus2 = n_minus1
        n_minus1 =result
    return result
    
    
def fibonacci_recursive(n: int) -> int:
    """ Return the n fibonacci number for positive n

    Args:
        n (int): positive integer
    """
    if n == 0:
        return 0
    if n == 1:
         return 1;
    return fibonacci_recursive(n -1) + fibonacci_recursive(n - 2)

print(fibonacci_recursive(0))
print(fibonacci_recursive(1))
print(fibonacci_recursive(2))
print(fibonacci_recursive(3))
print(fibonacci_recursive(4))
print(fibonacci_recursive(5))

