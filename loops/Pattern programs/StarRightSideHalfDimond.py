# Print star pattern of right side dimond as shown below

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
star = 1
for row in range(1,n+1):
    for st in range(1,star+1):
        print('*',end=' ')
    print()
    if row<=n//2:
        star +=1
    else:
        star -=1