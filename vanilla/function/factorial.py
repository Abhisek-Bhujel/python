# def factorial(num: int) -> int:
#     """Calculate the factorial of given int """
#     if num == 0 or num == 1:   # base case
#         return 1
#     return num * factorial(num - 1)

def factorial(num: int) -> int:
    """
    Calculate the factorial of a non-negative integer using recursion.

    Args:
        num (int): A non-negative integer.

    Returns:
        int: The factorial of `num`.

    Raises:
        ValueError: If `num` is negative.
    """
    if num < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if num in (0, 1):
        return 1
    return num * factorial(num - 1)


print(factorial(7))