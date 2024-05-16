n = 1
counter = 0
while True:
    temp = n
    summ = 0
    
    while temp !=0:
        fact = 1
        reminder = temp %10
        for v in range(2,reminder+1):
            fact *= v
        temp //=10
        summ += fact
    if n == summ:
        counter +=1
        if counter>=1 and counter<=3:
            print(n)
    if counter == 3:
        break
    n +=1