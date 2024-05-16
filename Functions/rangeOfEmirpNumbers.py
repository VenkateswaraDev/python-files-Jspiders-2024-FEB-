'''
Emirp number => Emirp number is a number which should satisfy the below conditions

1. given number should be prime
2. given number reverse is also should be prime
3. it should not be palindrom
'''
from isPrimeFunction import isPrime
from reverseFunction import reverse
def isEmirp(n):
    rev = reverse(n)
    if isPrime(n) and isPrime(rev) and rev != n:
        return True
    else:
        return False
    
def emirpNumbers(ll,ul):
    for n in range(ll,ul):
        if isEmirp(n):
            print(n)
            
if __name__ == '__main__':
    ll = int(input('Enter lower limit value = '))
    ul = int(input('Enter upper limit value = '))
    emirpNumbers(ll,ul)
    