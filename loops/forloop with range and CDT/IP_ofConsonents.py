# print the index positions of the consonents 

s = input("Enter a string = ")
v = 'AEIOUaeiou'

for ip in range(len(s)):
    if s[ip].isalpha() and s[ip] not in v:
        print(ip)