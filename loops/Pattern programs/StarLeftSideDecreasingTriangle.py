# print star pattern of left side Decreasing triangle as show below
''' 

* * * * *
* * * *
* * *
* *
*

'''

n = int(input("Enter a number = "))
for row in range(1,n+1):
    for col in range(1,n+1):
        if row+col<=n+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()