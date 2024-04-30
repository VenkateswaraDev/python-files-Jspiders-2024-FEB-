    i = num
        sum = 0
        l = len(str(num))
        while i>0:
            r = i%10
            sum = sum + r**l
            i = i//10
        if num == sum:
            print(num)
