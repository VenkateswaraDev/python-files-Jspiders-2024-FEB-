s= input("Enter a string = ")
vow = 'aeiouAEIOU'
v_count=0
c_count=0
for i in s:
    if i.isalpha() and i not in vow:
        c_count +=1
    else:
        v_count +=1
print(v_count)
print(c_count)