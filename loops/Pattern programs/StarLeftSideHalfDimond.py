# Print star pattern of left side dimond as shown below
'''
        *
      * *
    * * *
  * * * *
* * * * *
  * * * *
    * * *
      * *
        *

'''
n = int(input('Enter a number = '))
space = n//2
star = 1
for row in range(1,n+1):
    for sp in range(1,space+1):
        print(' ',end=' ')
    for st in range(1,star+1):
        print('*',end=' ')
    print()
    if row<=n//2:
        space -=1
        star +=1
    else:
        space +=1
        star -=1