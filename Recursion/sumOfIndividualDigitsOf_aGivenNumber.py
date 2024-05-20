def summ(n):
    if n == 0:
        return 0
    return n % 10 + summ(n//10)

result = summ(int(input("Enter a number to find sum of individual digits of that number = ")))
print(result)