n = int(input('enter a num = '))
rev = 0
i = n
while i!=0:
    rem = i%10
    i = i//10
    rev = rev*10+rem
if n == rev:
    print("plindrom")
else:
    print("not plindrom")