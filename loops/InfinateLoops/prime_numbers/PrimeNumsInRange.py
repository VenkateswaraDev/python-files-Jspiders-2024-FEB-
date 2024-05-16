ll = int(input("Enter a number = "))
ul = int(input("Enter a number = "))
for n in range(ll,ul+1):
    if n>1:
        i = 2
        while i<=n//2:
            if n%i == 0:
                break
            i +=1
        else:
            print(n)