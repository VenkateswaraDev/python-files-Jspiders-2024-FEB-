def summ(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return n+summ(n-1)

a = summ(5)
print(a)