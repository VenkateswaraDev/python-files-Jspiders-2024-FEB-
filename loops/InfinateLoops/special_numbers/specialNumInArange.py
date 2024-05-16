ll = int(input('Enter a number = '))
ul = int(input('Enter a number = '))
for n in range(ll,ul+1):
   if n>0: 
        i = n
        summ = 0
        while i !=0:
            fact = 1
            rem = i % 10
            for j in range(1,rem+1):
                fact *= j
            summ = summ+fact
            i = i//10
        if n == summ:
            print(n)