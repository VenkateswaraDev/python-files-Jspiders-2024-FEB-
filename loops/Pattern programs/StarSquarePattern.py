# print Star Square pattern 
'''
*****
*****
*****
*****
*****
'''
n = int(input('Enter a num = '))
for row in range(1,n+1):
    for col in range(1,n+1):
        print('*',end='')
    print()
