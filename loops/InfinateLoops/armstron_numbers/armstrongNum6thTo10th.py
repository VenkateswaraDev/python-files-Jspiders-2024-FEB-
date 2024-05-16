n = 1
counter = 0
while True:
    i = n
    summ =0
    while i!=0:
        rem = i %10
        summ += rem**len(str(n))
        i //=10
    if n ==summ:
        counter +=1
        if counter>=6 and counter<=10:
            print(n)
    if counter == 10:
        break
    n +=1