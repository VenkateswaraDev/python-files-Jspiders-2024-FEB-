# find sum of even index positions of odd digits present in a string

s = input("Enter a string = ")
sum = 0
for ip in range(len(s)):
    if s[ip].isdigit():
        if int(s[ip]) % 2 != 0 and ip % 2 == 0:
            sum += ip
print(sum)