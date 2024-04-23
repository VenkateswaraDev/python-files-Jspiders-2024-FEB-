num = int(input("Enter a number = "))
fact = 1
i=2
if num>=0:

    while i<=num:
        fact *= i 
        i +=1
    print(fact)
else:
    print("Please enter positive values")