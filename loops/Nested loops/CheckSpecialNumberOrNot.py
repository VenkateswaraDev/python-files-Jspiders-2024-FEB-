num = int(input("Enter a number to find given number is special num or not = "))
i = num
sum = 0
while i>0:
    r = i%10
    fact = 1
   
    for j in range(1,r+1):
        fact *=j
    sum = sum + fact
    i=i//10
if num == sum:
    print('special number')
else:
    print('not a special number')