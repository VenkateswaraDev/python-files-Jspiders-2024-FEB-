#  given list = [10,11,12,13]
# output  ['even','odd','even','odd']

l = eval(input("Enter a list only containing numbers =  "))
for ip in range(len(l)):
    if l[ip] % 2 == 0:
        l[ip] = 'even'
    else:
        l[ip] = 'odd'
print(l)