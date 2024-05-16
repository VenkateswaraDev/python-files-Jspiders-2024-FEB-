def isPrefect(n):
    summ = 0
    fact = 1
    for j in range(2,n//2+1):
        if n % j == 0:
            fact += j
    summ +=fact
    if summ == n:
        return True
    else:
        return False

print(isPrefect(6))