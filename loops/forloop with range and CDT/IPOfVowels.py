# print index positions of ovwels in given str

s= input("Enter a string = ")
v = 'AEIOUaeiou'
for ip in range (len(s)):
    if s[ip] in v:
        print(f'index position of vowel in given string is {ip}')