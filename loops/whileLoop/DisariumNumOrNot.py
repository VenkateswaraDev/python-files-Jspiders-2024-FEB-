n = int(input("Enter a number = "))
sum = 0
i = n
l = len(str(n))
while i!=0:
    rem = i %10
    i = i//10
    sum = sum+rem**l
    l -=1

if sum == n:
    print("Disarium number")
else:
    print("not a disarium number")