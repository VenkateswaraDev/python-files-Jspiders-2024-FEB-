''' we can perform Aggregation in 2 ways
        1. Creating object in main spae and using that in main class
        2. creating an object and using an object can be done in main class
'''
#Creating object of a class inside the constructer of main class
class Address:
    def __init__(self,city,state,country):
        self.city = city
        self.state = state
        self.country = country
    def display_address(self):
        print('city is ',self.city)
        print('state is ',self.state)
        print('country is ',self.country)
        
        
class Student:
    def __init__(self,n,a,c):
        self.Sname = n
        self.Sage = a
        self.Sclass = c
        ci = input('Enter city = ')
        s = input('Enter state = ')
        co = input('Enter country = ')
        ad = Address(ci,s,co)
        self.Saddress = ad
    def student_details(self):
        print(f'name = {self.Sname}')
        print(f'age = {self.Sage}')
        print(f'class = {self.Sclass}')
        print('*****Address*****')
        self.Saddress.display_address()
        
s1 = Student('Venky',15,10)
s1.student_details()
        
        