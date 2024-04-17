# find the sum of index positions of digits in given string

s = input("Enter a string = ")
sum = 0 
for ip in range (len(s)):
    if s[ip].isdigit:
        sum += ip
print(sum)