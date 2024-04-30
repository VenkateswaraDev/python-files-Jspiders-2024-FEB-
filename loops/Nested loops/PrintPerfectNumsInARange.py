#print all perfect numbers in the given range
ll = int(input("Enter a starting range value = "))
ul = int(input("Enter a ending range value = "))
print("For loop inside For loop")
for num in range (ll,ul+1):
    sum = 0
    for i in range(1,num//2+1):
        if num%i==0:
            sum +=i
    if num == sum:
        print(num)

print("while loop inside while loop")
num = ll
while num<=ul:
    sum=0
    i=1
    while i<=num//2:
        if num%i ==0:
            sum +=i
        i+=1
    if num == sum:
        print(num)
    num+=1

print("For loop inside While loop")
num = ll
while num<=ul:
    sum = 0
    for i in range(1,num//2+1):
        if num%i==0:
            sum+=i
    if num == sum:
        print(num)
    num+=1

print("While loop inside For loop")
for num in range(ll,ul+1):
    sum = 0
    i = 1
    while i<=num//2:
        if num%i == 0:
            sum +=i
        i+=1
    if num == sum:
        print(num)