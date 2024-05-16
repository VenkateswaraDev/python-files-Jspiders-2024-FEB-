# print  diagonal * pattern as given below
'''
        *
      *
    *
  *
*

'''
'''
n = int(input("enter a num = "))
for row in range(1,n+1):
    for col in range(1,n+1):
        if row+col == n+1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
# using spaces and stars method

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