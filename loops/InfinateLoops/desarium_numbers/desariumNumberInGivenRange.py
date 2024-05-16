ll = int(input('Enter a number = '))
ul = int(input("Enter a number = "))

for n in range(ll,ul+1):
    i = n
    summ = 0
    l = len(str(i))
    while i != 0:
        rem = i % 10
        summ += rem ** l
        i //=10
        l -=1
    if n == summ:
        print(n)
    