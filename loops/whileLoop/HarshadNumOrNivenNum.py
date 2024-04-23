n = int(input("Enter a number = "))
sum = 0
i = n
while i!=0:
    rem = i%10
    i = i//10
    sum = sum + rem

if n % sum==0:
    print("Harshad number")
else:
    print("Not a harshad number")