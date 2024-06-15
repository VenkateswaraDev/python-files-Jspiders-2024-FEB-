''' we can perform Aggregation in 2 ways
        1. Creating object in main spae and using that in main class
        2. creating an object and using an object can be done in main class
'''
#Creating an object in main space and using it in main class will help you to use the object for multiple times.
class Address:
    def __init__(self,city,state,country):
        self.city = city
        self.state = state
        self.country = country
    def display_address(self):
        print('city is ',self.city)
        print('state is ',self.state)
        print('country is ',self.country)
        
location = Address('Bangolore','karnataka','india')

class Student:
    def __init__(self,n,a,c,ad):
        self.Sname = n
        self.Sage = a
        self.Sclass = c
        self.Saddress = ad
    def student_details(self):
        print(f'Name = {self.Sname}')
        print(f'age = {self.Sage}')
        print(f'class = {self.Sage}')
        print('*****Address*****')
        self.Saddress.display_address()
        
s1 = Student('venky',10,5,location)
s1.student_details()