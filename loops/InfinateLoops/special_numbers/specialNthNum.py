user_input = int(input("Enter a number = "))
num = 1
counter = 0
while True:
    temp = num
    summ = 0
    
    while temp !=0:
        fact = 1
        reminder = temp % 10
        for v in range(2,reminder+1):
            fact *= v
        temp //=10
        summ += fact
    if num == summ:
        counter +=1
    if counter == user_input:
        print(num)
        break
    num +=1
    