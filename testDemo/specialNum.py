def specialNum(n):
    summ = 0
    i = n
    while i!=0:
        rem = i%10
        fact = 1
        for j in range(1,rem+1):
            
            fact *= j
        summ = summ + fact
        i //=10
    return summ


print(specialNum(145))