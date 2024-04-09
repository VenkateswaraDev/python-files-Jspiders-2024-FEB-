s = input("Enter a string = ")
sum = 0
for i in s:
    if i.isdigit():
        n=int(i)
        if n%2==0:
            sum +=n
print(sum)