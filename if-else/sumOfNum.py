n=int(input())
sum =0
rem =0
#i=n
while n!=0:
    rem = n%10
    sum +=rem
    n = n//10
print(sum)