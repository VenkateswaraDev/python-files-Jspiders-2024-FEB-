from isArmStronFunction import isArmStrong

def armStrongNumbers(ll,ul):
    for n in range(ll,ul+1):
        if isArmStrong(n):
            print(n)
        
if __name__=='__main__':
    ll = int(input("Enter lower limit value = "))
    ul = int(input("Enter upper limit value = "))
    armStrongNumbers(ll,ul)
    