a = int(input("Enter 1st number = "))
b = int(input("Enter 2nd number = "))
n = int(input("enter a number upto = "))
if n == 1:
    print(a)
elif n == 2:
    print(a,b)
elif n>2:
    print(a,b, end=' ')
    for i in range(3,n+1):
        c = a+b
        print(c,end=' ')
        a,b = b,c
else:
    print("Enter positive digits only above 0 ")