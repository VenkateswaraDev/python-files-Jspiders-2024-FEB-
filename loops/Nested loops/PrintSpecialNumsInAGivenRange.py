ll = int(input("Enter a lower range number = "))
ul = int(input("Enter upper range number = "))

for num in range(ll,ul+1):
    if num>0:
        i = num
        sum = 0
        while i>0:
            r = i%10
            fact = 1
            for j in range(1,r+1):
                fact *= j
            sum = sum+fact
            i = i//10
        if num == sum:
            print(num)
