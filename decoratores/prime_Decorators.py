def time_decorator(arg):
    def inner():
        import time
        t1=time.time()
        arg()
        t2=time.time()
        print(t2-t1)
    return inner

@time_decorator
def prime():
    cnt=0
    n1=2
    while(cnt<=10):
        
       
        if n1>1:
            for i in range (2,n1//2+1):
                if n1%i==0:
                    break
            else:
                print(n1)
                cnt+=1
        n1 +=1
                                  
prime() 
