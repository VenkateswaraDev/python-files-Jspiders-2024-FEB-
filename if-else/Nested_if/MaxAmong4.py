a = int(input("Enter 1st number =  "))
b = int(input("Enter 2nd number =  "))
c = int(input("Enter 3rd number =  "))
d = int(input("Enter 4th number =  "))

if a>b:
    if a>c:
        if a>d:
            print(a)
        else:
            print(d)
    else:
        if c>d:
            print(c)
        else:
            print(d)
else:
    if b>c:
        if b>d:
            print(b)
        else:
            print(d)
    else:
        if c>d:
            print(c)
        else:
            print(d)