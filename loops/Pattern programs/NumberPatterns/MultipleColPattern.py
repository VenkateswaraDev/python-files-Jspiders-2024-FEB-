#Print pattern as shown below
'''

1 
2 3 
4 5 6 7 
8 9 1 2 3 4 5 6 
7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 

'''
n = int(input("Enter a number = "))
cnum = 1
dummy = 1
for row in range(1,n+1):
    for col in range(1,cnum+1):
        print(dummy,end=' ')
        if dummy==9:
            dummy=1
        else:
            dummy+=1
    print()
    cnum +=cnum