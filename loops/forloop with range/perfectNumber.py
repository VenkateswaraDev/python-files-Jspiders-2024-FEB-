# To check given number is perfect number or not
# Take a number from user to check
num = int(input("Enter a number to check perfect number or not = "))
#by assume if the user given number that does not contain any divisors, then i need to return 0
divisorSum = 0
# taking for loop with range to find the divisors of given number
# in range starting from 1 and ending will be (num//2) because there is no divisors of a number grater than half of the number.
for i in range (1,(num//2+1),1):
    if num%i==0:
        divisorSum += i
if divisorSum == num:
    print(f'{num} is a perfect number') 
else:
    print(f'{num} is not a perfect number')