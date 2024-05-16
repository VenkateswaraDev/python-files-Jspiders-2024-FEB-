ll = int(input('Enter a num = '))
ul = int(input('Enter a num = '))

for n in range(ll,ul+1):
    i = n
    summ = 0
    while i !=0:
        rem = i % 10
        summ += rem
        i //=10
    if n % summ==0:
        print(n)