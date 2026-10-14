def cube(x):
    """Returns the cube of a number."""
    return x ** 3

def factorial(n):
    """Returns the factorial of a number."""
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

no = int(input("Enter a number to cube: "))
print(f"The cube of {no} is {cube(no)}")

no = int(input("Enter a number to find its factorial: "))
print(f"The factorial of {no} is {factorial(no)}")