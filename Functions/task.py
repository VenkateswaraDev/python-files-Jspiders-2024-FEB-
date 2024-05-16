from rangeOfPrimeNumbers import primeNumbers
from isPrimeFunction import isPrime

def sumOfPrime(n):
    summ = 0
    for i in range(2,n+1):
        if isPrime(i):
            summ +=i
    return summ


def reduceToSingDigit(n):
    i = n
    summ = 0
    while i !=0:
        rem = i %10
        summ += rem
        i //=10
    if summ >=10:
       summ = reduceToSingDigit(summ)
    return summ
    

def replaceVowel(n):
    v = 'aeiouAEIOU'
    dummyStr = ''
    for i in range(0,len(n)):
        if n[i] in v:
            k = i*100
            s = sumOfPrime(k)
            r = str(reduceToSingDigit(s))
            dummyStr += r
        else:
            dummyStr += n[i]
    return dummyStr

name = input("Enter a string = ")
print(replaceVowel(name))
            
                       






  



