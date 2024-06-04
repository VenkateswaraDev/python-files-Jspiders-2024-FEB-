def timeDiff(arg):
    def inner():
        import time
        t1 = time.time()
        print(t1)
        arg()
        t2 = time.time()
        print(t2)
        print(f'time difference = {t2-t1}')
    return inner

@timeDiff # evenNum = timeDiff(evenNum address) # updated evenNum to inner address
def evenNum():
    c = 0
    n = 1
    while True:
        if n%2 == 0:
            print(n)
            c +=1
        if c == 10:
            break
        n +=1
        
evenNum()