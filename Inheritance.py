class Animal: # parent class
    def speak(self):
        print("Animal is speaking")

class Dog(Animal):
    def bark(self):
        print("Dog is barking")

class Cat(Animal):
    def meow(self):
        print("Cat is meowing")

d = Dog()
d.speak()  # Inherited from parent class animal
d.bark()

c = Cat()  # Inherited from parent class animal
c.speak()