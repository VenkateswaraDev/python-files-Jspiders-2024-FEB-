def display(n):
    print(n)
    if n==5:
        return
    display(n-1)

print(display(10))