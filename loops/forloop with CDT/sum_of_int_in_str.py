s = input("Enter a string = ")
sum = 0
for i in s:
    if i.isdigit():
        n = int(i)
        sum += n
print(sum)