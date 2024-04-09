l = eval(input("Give list which contain numbers = "))
n= len(l)
e_count=0
o_count=0
for i in range(0,n):
    if l[i]%2==0:
        e_count+=1
    else:
        o_count+=1
print(f'No.of even number in given list = {e_count}')
print(f'No.of odd number in given list = {o_count}')