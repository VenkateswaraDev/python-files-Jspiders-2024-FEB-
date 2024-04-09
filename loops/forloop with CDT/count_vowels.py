s=input("Enter a string = ")
vow = 'aeiouAEIOU'
count = 0
for i in s:
    if i in vow:
        count +=1
print(count)