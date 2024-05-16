from isPrimeFunction import isPrime
from reverseFunction import reverse

def paliPrimeNumbers(ll,ul):
    for n in range(ll,ul+1):
        if reverse(n) == n and isPrime(n):
            print(n)

if __name__=='__main__':
    ll = int(input('Enter lower limit value = '))
    ul = int(input('Enter upper limit value = '))
    paliPrimeNumbers(ll,ul)
    