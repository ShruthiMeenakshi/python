#Consider a dog
#Class can be defined as a dog (what dog is)
#Properties are: Name , Breed, age, behaviour (how it differs from others)
#Methods are bark, sleep, eat (Actions)

#object:
#Consider Fido and buddy are two different dogs 
#Properties: Consider Fido -> Name: Fido Breed: labrador age:3 while buddy->  Name: Buddy Breed: german shephard age:5


class Person:
    def __init__(self, name , age): # _ _ name _ _ this underscore indicates as a initialization to create attribute
        self.name = name
        self.age = age           # name and age are parameters while self is akeyword that helps to access attributes

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age

p1=Person("bob", 22) # p is a object that created it to be a person
print(p1.getName())
print(p1.getAge())

#OOPS Inheritance 

class Cars: #consider designing a base model car

    def __init__(bmw):
        bmw.wheels = 4
        bmw.seats = 5
    def drive(bmw):
        print("Driving BMW...")

class Sportscars(Cars):  #this means supercars class is inherit the properties of cars by calling it
    def __init__(bmw):
        super().__init__()      # the super class method executes the init method of parent class cars
        bmw.engine_power = "400 HP"
        bmw.seats = 2
    
    def drive(bmw):
        print("Driving a sports car...")


mycar = Cars()
mycar.drive()

mySportscar = Sportscars()
mySportscar.drive()