# print sum of even digits present in odd index positions in given string

s = input("Enter a string = ")
sum = 0
for ip in range(len(s)):
    if s[ip].isdigit():
        if int(s[ip]) % 2 ==0 and ip % 2 != 0:
            sum += int(s[ip])
print(sum)