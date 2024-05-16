n = 1
pc = 0
while True:
    if n>1:
        for i in range(2,n//2+1):
            if n%i == 0:
                break
        else:
            pc +=1
            if pc>=6 :
                print(n)
    if pc==10:
        break
            
    n +=1