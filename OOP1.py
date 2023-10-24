class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def detail(self):
        print(self.name, "is studying")


p = Person("Alfonce", 23, "Male")
p.detail()