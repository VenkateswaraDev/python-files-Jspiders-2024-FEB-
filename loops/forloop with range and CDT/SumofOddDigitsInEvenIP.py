# find sum of odd digits present in the even index positions from given string

s = input("Enter a string = ")
sum = 0
for ip in range(len(s)):
    if s[ip].isdigit():
        if int(s[ip]) % 2 != 0 and ip % 2 == 0:
            sum += int(s[ip])
print(sum)