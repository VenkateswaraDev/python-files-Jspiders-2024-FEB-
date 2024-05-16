n = int(input("Enter a number = "))
c = 1
counter = 0
while True:
    i = c
    summ =0
    while i !=0:
        rem = i%10
        summ += rem**len(str(n))
        i //=10
    if c==summ:
        counter +=1
    if counter == n:
        print(c)
        break
    c +=1