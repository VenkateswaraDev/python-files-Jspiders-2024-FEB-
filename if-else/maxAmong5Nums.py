num1 = int(input("Enter 1st number = "))
num2 = int(input("Enter 2nd number = "))
num3 = int(input("Enter 3rd number = "))
num4 = int(input("Enter 4th number = "))
num5 = int(input("Enter 5th number = "))

if num1>num2 and num1>num3 and num1>num4 and num1>num5:
    print(num1)
elif num2>num3 and num2>num4 and num2>num5:
    print(num2)
elif num3>num4 and num3>num5:
    print(num3)
elif num4>num5:
    print(num4)
else:
    print(num5)