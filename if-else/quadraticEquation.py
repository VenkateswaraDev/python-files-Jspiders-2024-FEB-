'''a=int(input('enter 1st number = '))
b= int(input('Enter 2nd number = '))
c= int(input('Enter 3rd number = '))
sqr = ((b**2)-4*a*c)**1/2
x= (-b+sqr)/2*a
x2=
print(x)'''
from math import sqrt


a = int(input("enter a : "))
b = int(input("enter b : "))
c = int(input("enter c : "))

s = (((b**2) + (4*a*c)))
sum = sqrt(s)


x1 = (-b + sum)/2*a
print("x1 is ",x1)

x2 = (-b - sum)/2*a
print("x2 is ",x2)