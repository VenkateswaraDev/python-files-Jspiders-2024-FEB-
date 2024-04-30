ll = int(input("Enter starting range = "))
ul = int(input("Enter ending range = "))
for num in range (ll,ul+1):
    if num>=1:
        i = num
        sum = 0
        l = len(str(num))
        while i>0:
            r = i%10
            sum = sum + r**l
            i = i//10
        if num == sum:
            print(num)
