s = input("Enter a string = ")
vow = 'aeiouAEIOU'
count = 0
for i in s:
    if i.isalpha() and i not in vow:
        count +=1
print(count)