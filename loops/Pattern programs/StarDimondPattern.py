#Print star dimond pattern as shown below
'''
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *

'''
'''
n = int(input('Enter a number = '))
space = n-1
star = 1
for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print('*',end=' ')
    print()
    space -=1
    star +=2

for inrow in range(n-1,0,-1):
    space = n-inrow
    star = inrow*2-1
    for insp in range(1,space+1):
        print(' ',end=' ')
    for inst in range(1,star+1):
        print('*',end=' ')
    print()'''


#spaces and star method

n = int(input("Enter a number = "))
space = n//2
star = 1
for row in range (1,n+1):
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print('*',end=" ")
    print()
    if row<=n//2:
        space -=1
        star +=2
    else:
        space +=1
        star -=2