# sum of factorical of each single digit in a given number is equal to the number then it is called special number

from factorialFunction import factorial

def isSpecial(n):
    summ = 0
    i = n
    while i !=0:
        rem = i % 10
        summ = summ+ factorial(rem)
        i //=10
    if summ == n:
        return True
    else:
        return False

if __name__ == '__main__':
    pass