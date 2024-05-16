ll = int(input("Enter a number = "))
ul = int(input("Enter a number = "))
for num in range(ll,ul+1):
    i = num
    summ =0
    while i !=0:
        rem = i%10
        summ += rem**len(str(num))
        i //=10
    if num == summ:
        print(num)
        