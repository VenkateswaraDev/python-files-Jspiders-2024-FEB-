# finding range of prime numbers by using for loop inside for loop

ll = int(input('Enter lower range value = '))
ul = int(input("Enter upper range value = "))
print("ForLoop Inside ForLoop")
for num in range(ll,ul+1):
    if num>1:
        for i in range(2,(num//2)+1):
            if num%i == 0:
                break
        else:
            print(num)

# finding range of prime numbers by using while loop inside while loop
print("WhileLoop inside WhileLoop")
num = ll
while num<=ul:
    if num>1:
        i = 2
        while i<=num//2:
            if num%i == 0:
                break
            i +=1
        else:
            print(num)
    num +=1


# finding range of prime numbers by using for loop inside while loop
print("ForLoop inside WhileLoop")
num = ll
while num<=ul:
    if num>1:
        for i in range(2,num//2+1):
            if num%i == 0:
                break
        else:
            print(num)
    num+=1

# finding range of prime numbers by using while loop inside for loop
print("WhileLoop inside ForLoop")
for num in range(ll,ul+1):
    if num>1:
        i = 2
        while i<= num//2:
            if num%i==0:
                break
            i+=1
        else:
            print(num)