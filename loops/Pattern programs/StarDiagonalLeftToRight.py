# print  diagonal * pattern as given below
'''
*
  *
    *
      *
        *
'''
n = int(input("enter a num = "))
for row in range(1,n+1):
    for col in range(1,n+1):
        if row==col:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()