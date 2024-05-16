def isHarshad(n):
    i = n
    summ = 0
    while i !=0:
        rem = i % 10
        summ += rem
        i //=10
    if n%summ == 0:
        return True
    else:
        return False
    
if __name__ == '__main__':
    pass
        