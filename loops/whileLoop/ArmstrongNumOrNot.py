n = int(input("Enter a number = "))
sum =0 
i = n
l = len(str(n))
while i!=0:
    rem = i%10
    i = i//10
    sum = sum+rem**l
if sum == n:
    print("Armstrong number")
else:
    print("Not a Armstrong number")