from isHarshadFunction import isHarshad

def harshadNumbers(ll,ul):
    for n in range(ll,ul+1):
        if isHarshad(n):
            print(n)


if __name__ == '__main__':
    ll = int(input('Enter lower value = '))
    ul = int(input('Enter upper value = '))
    harshadNumbers(ll,ul)