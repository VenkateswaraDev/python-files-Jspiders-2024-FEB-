def isPerfect(n):
    summ = 0
    for i in range(1,n//2+1):
        if n%i == 0:
            summ += i 
    if summ == n:
        return True
    else:
        return False
    
if __name__ == '__main__':
    pass