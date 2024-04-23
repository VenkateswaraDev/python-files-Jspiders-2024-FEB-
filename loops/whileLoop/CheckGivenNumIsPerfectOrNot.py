num = int(input("enter a number = "))
ds = 0
i=1
while i<=num//2:
    if num % i ==0:
        ds += i
    i +=1
if ds == num:
    print("perfect number")
else:
    print("not a perfect")