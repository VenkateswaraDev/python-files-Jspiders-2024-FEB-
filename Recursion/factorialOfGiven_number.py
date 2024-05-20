def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n-1)

result = fact(int(input('Enter a number to find factorial = ')))
print(f'The factorial of given number is {result}')