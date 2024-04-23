n = int(input('enter a num = '))
rev = 0
i = n
while i!=0:
    d = i%10
    i = i//10
    rev = rev*10+d
print(rev)