def armStrongNumber(n):
    global l
    if n == 0:
        return 0
    return (n % 10)**l + armStrongNumber(n//10)

user_input = int(input("Enter a number to find armstrong number or not  = "))
l = len(str(user_input))
result = armStrongNumber(user_input)
if user_input == result:
    print(f'Given number {user_input} is a armstrong number')
else:
    print(f'Given number {user_input} is not a armstrong number')