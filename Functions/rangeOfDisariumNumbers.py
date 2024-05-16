from isDisariumFunction import isDisarium

def DisariumNumbers(ll,ul):
    for n in range(ll,ul+1):
        if isDisarium(n):
            print(n)
            
if __name__=='__main__':
    ll = int(input('Enter lower limit values = '))
    ul = int(input('Enter upper limit value = '))
    DisariumNumbers(ll,ul)