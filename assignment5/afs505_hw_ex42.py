## An animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a class
class Dog(Animal):

    def __init__(self, name):
        ## name is-a attribute of self
        self.name = name

## Cat is-a class
class Cat(Animal):

    def __init__(self, name):
        ##name is-a attribute of self
        self.name = name

## Person is-a class
class Person(object):

    def __init__(self,name):
        ## name is-a attribute of self
        self.name = name

        ## No attribute for self.pet
        self.pet = None

## Employee is-a class
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## attribute of self is-a salary
        self.salary = salary

## Fish is-a class
class Fish(object):
    pass

## Salmon is-a class
class Salmon(Fish):
    pass

## Halibut is-a class
class Halibut(Fish):
    pass


## rover is-a object of class Dog
rover = Dog("Rover")

## satan is-a object
satan = Cat("Satan")

## mary is-a object of class Person
mary = Person("Mary")

## mary has-a Cat
mary.pet = satan

## frank is-a object of class Employee
frank = Employee("Frank", 120000)

## frank is-a object which has-a attribute object rover
frank.pet = rover

## flipper is-a object in the class Fish
flipper = Fish()

## crouse is-a object in the class Salmon
crouse = Salmon()

## harry is-a object in the class Halibut
harry = Halibut()
