# find sum of index positions of sub string in a given string


s = input("Enter a string = ")
subs = input("Enter a sub string = ")
sum=0
for ip in range(len(s)):
    if s[ip:ip+len(subs):] == subs:
        sum += ip
print(sum)