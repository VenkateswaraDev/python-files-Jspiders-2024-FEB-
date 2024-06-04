def outer(arg): # decorator function
    print('outer is started')
    print(arg)
    def inner():
        print('inner is strted')
        arg()# old wish address
        print('inner is ended')
    print('outer is ended')
    return inner

@outer # wish = outer(wish address) # new wish address is inner address

def wish(): # decorated function
    print('wish is started')
    print('wish is ended')
    
wish()