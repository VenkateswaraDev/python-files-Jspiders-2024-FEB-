from isPrimeFunction import isPrime
# function to print 
def primeNumbers(ll,ul):
    for n in range(ll,ul+1):
        if isPrime(n):
            print(n)

if __name__ == '__main__':
    ll = int(input("enter lower limit value = "))
    ul = int(input("enter upper limit value = "))
    primeNumbers(ll,ul)


