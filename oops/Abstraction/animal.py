from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def move(self):
        pass
    
    @abstractmethod
    def speak(self):
        pass
    
class Dog(Animal):
    def move(self):
       print('This can walk')
    def speak(self):
        print('Bow Bow .....')
        
class Snake(Animal):
    def move(Self):
        print('They can crowl')
    def speak(self):
        print('ssssssssssssshhhhhhhh..')
        
do = Dog()
do.speak()
do.move()

so = Snake()
so.move()
so.speak()
