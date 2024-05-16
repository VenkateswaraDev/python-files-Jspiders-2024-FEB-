def reverse(n):
    rev = 0
    i = n
    while i !=0:
        rem = i%10
        rev = rev*10 + rem
        i //=10
    return rev

if __name__ == '__main__':
    pass