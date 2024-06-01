def outer(arg):
    print('Outer fuction started')
    print(arg)
    def inner():
        print('inner function is started')
        print(arg)
        arg()
        print('inner function ended')
    print('outer function ended')
    return inner


def greet():
    print('Greet function is started')
    print('Greet function is ended')
    
    
result = outer(greet)
result()