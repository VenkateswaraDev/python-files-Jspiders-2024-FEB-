n=int(input())
a=0
b=1

next=b
for i in range (1,n):
    print(next)
    
    a=b
    b=next
    next=a+b