s = input("Enter a string = ")
esum = 0
osum = 0
for i in s:
    if i.isdigit():
        n=int(i)
        if n%2==0:
            esum += n
        else:
            osum += n

print(abs(esum-osum))