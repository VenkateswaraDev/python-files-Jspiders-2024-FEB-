def isArmStrong(n):
    i = n
    l = len(str(n))
    summ = 0
    while i !=0:
        rem = i % 10
        summ = summ+rem**l
        i //=10
    if summ == n:
        return True
    else:
        return False

if __name__ == '__main__':
    pass