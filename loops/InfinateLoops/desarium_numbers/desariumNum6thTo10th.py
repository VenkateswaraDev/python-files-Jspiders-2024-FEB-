n = 1
c = 0
while True:
    i = n
    summ = 0
    l = len(str(i))
    while i !=0:
        rem = i % 10
        summ = summ+rem**l
        i = i//10
        l = l-1
    if n == summ:
        c +=1
        if c>=6 and c<=10:
            print(n)
    n +=1