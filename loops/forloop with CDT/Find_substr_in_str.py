s = input("Enter a string= ")
sub = input("Enter a sub string = ")
count = 0
for i in s:
    if i==sub:
        count +=1

print(count)