n=int(input())
a=n
sum =0
rem =0
#i=n
while n!=0:
    rem = n%10
    sum +=rem**3
    n = n//10
print(sum)

if a==sum:
    print("Armstrong number")
else:
    print("Not a amrmstrong number")