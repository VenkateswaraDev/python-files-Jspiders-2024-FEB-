class Car:
    def __init__(self,cname,cnumber,ccolour):
        self.cname = cname
        self.cnumber = cnumber
        self.ccolour = ccolour
        
    def start(self):
        print(f'{self.cname} is started')
    
    def accelerate(self):
        print(f'{self.cname} is accerated')
        
    def stop(self):
        print(f'{self.cname} is stoped')
        
        
class Driver:
    def __init__(self,Dname,Did,Dexperience):
        self.Dname = Dname
        self.Did = Did
        self.Dexperience = Dexperience
        n = input('Enter car name = ')
        no = input('Enter car number = ')
        co = input('Enter car colour = ')
        x = Car(n,no,co)
        self.Dcar = x
    
    def driving(self):
        print(f'{self.Dname} has entered in the car')
        self.Dcar.start()
        self.Dcar.accelerate()
        self.Dcar.stop()
        
driver1 = Driver('venky',123,2)
driver2 = Driver('ram',345,1)

driver1.driving()
driver2.driving()