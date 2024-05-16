from isSpecialFunction import isSpecial

def specialNumbers(ll,ul):
    for n in range(ll,ul+1):
        if isSpecial(n):
            print(n)
            
if __name__ == '__main__':
    ll = int(input('Enter lower limt value = '))
    ul = int(input('Enter upper limit value  =  '))
    specialNumbers(ll,ul)