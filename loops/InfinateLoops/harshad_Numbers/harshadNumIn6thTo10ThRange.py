n = 1
c = 0
while True:
    
    i = n
    summ = 0
    while i !=0:
        rem = i % 10
        summ += rem
        i //= 10
    if n % summ==0:
        c +=1
        if c>=6 and c<=10:
            print(n)
    if c == 10:
        break
    n +=1