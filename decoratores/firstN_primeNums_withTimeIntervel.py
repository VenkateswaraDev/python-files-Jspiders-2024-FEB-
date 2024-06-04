def timeDiff(arg):
    def inner():
        import time
        t1 = time.time()
        print(t1)
        arg()
        t2 = time.time()
        print(t2)
        print(f'Time intervel is {t2-t1}')
    return inner

@timeDiff
def primeNums():
    c = 0
    n = 2
    while True:
        for i in range(2,n//2+1):
            if n%i == 0:
                break
        else:
            print(n)
            c += 1
        if c == 10:
            break
        n +=1
        
primeNums()