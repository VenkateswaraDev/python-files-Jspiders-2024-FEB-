from isPerfectFunction import isPerfect

def perfectNumbers(ll,ul):
    for n in range(ll,ul+1):
        if isPerfect(n):
            print(n)
    
if __name__ == '__main__':
    ll = int(input('Enter lower limit value = '))
    ul = int(input('Enter upper limit value = '))
    perfectNumbers(ll,ul)