def withOutError(arg):
    def inner(a,b):
        if b!=0:
            arg(a,b)
        else:
            arg(b,a)
    return inner

@withOutError
#div=withoutError(div)

def div(a,b):
    print(a/b)

div(20,2)
div(20,0)