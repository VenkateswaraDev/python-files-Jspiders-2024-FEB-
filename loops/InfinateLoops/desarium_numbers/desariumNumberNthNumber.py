
user_input = int(input('enter a number = '))
n=1
co = 0
while True:
    i = n
    summ = 0
    l = len(str(i))
    while i!=0:
        rem = i%10
        summ += rem**l
        i //=10
        l -=1
    if n == summ:
        co +=1
    if co == user_input:
        print(n)
        break
    n +=1