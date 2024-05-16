User_input = int(input('Enter a number = '))
n = 1
c = 0
while True:
    summ = 0
    i = n
    while i !=0:
        rem = i % 10
        summ += rem
        i //=10
    if n == summ:
        c +=1
    if n == User_input:
        print(n)
        break
    n +=1