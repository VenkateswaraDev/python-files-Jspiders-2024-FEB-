#Creating object of a class inside the constructer of main class


class Car:
    def __init__(self,n,num,col):
        self.Cname = n
        self.Cnumber = num
        self.Ccolour = col
    def start(self):
        print('Car has started...........')
    def accelerate(self):
        print('accelerate car...............')
    def stop(self):
        print('Stop the car!!!')


class Driver:
    def __init__(self,n,id,ex):
        self.Dname = n
        self.Did = id
        self.Dexperience = ex
        na = input('Enter car name = ')
        no = input('Enter car number = ')
        c = input('Enter car colour = ')
        co = Car(na,no,c)
        self.Dcar = co
    def driving(self):
        print(f'{self.Dname} has entered in the car')
        self.Dcar.start()
        self.Dcar.accelerate()
        self.Dcar.stop()
        print(f'{self.Dname} has came out of the car')
        
        
D1 = Driver('venky',1234,2)
D1.driving()