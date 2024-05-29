'''def prime(n):
    if n>1:
        for i in range(2,n//2+1):
            if n%i == 0:
                print(f'{n} is not a prime number')
                break
        else:
            print(f'{n} is a prime number')
    else:
        print(f'{n} is a prime number')
        
        
        
num = int(input("Enter a number = "))
prime(num)'''

def add(*a):
    summ = 0
    for num in a:
        if isinstance(num,int):
            summ += num
    print(summ)


add(10,'hai',40,60)
















