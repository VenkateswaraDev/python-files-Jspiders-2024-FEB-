#check how many times the given sub string is present in the given string

s = input("Enter a string = ")
subs = input("Enter a sub string = ")
c=0
for ip in range(len(s)):
    if s[ip:ip+len(subs):] == subs:
        c += 1
print(c)